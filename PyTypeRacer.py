from selenium import webdriver
import time, re

default_delay = 0.105
usr_delay = input('Enter a delay value (Press enter to use default: ' + str(default_delay) + '): ')

if usr_delay != '':
    print('\nDelay set to ' + str(usr_delay))
    delay = float(usr_delay)
else:
    print('\nNo delay specified - using default delay of ' + str(default_delay))
    delay = default_delay

browser = webdriver.Chrome(service_log_path='NUL')
browser.get('https://play.typeracer.com/')

# Detects when the countdown is over
def start():
    timer = True
    while timer == True:
        try:
            browser.find_element_by_xpath('//*[@class="txtInput txtInput-unfocused"]')
            print('Waiting for countdown')
        except:
            timer = False
            print('Count down complete! Starting!\n')
            main()
        time.sleep(0.5)

# Handles all the logic
def main():
    try:
        typeBar = browser.find_element_by_class_name('txtInput')
        word1 = browser.find_element_by_xpath('//*[@id[starts-with(., \'nhwMiddlegwt\')]]').text
        word2 = browser.find_element_by_xpath('//*[@id[starts-with(., \'nhwRightgwt\')]]').text
        wordcomma = browser.find_element_by_xpath('//*[@id[starts-with(., \'nhwMiddleCommagwt\')]]').text

        word_check = (word1 + wordcomma + ' ' + word2)
        word_complete = re.sub(' , ', ', ', word_check)
        print('Words: \n' + word_complete)
        for char in word_complete:
            typeBar.send_keys(char)
            time.sleep(delay)
        loop()
    except:
        typeBar = browser.find_element_by_class_name('txtInput')
        word1 = browser.find_element_by_xpath('//*[@id[starts-with(., \'nhwMiddlegwt\')]]').text
        word2 = browser.find_element_by_xpath('//*[@id[starts-with(., \'nhwRightgwt\')]]').text

        word_check = (word1 + ' ' + word2)
        word_complete = re.sub(' , ', ', ', word_check)
        print('Words: \n' + word_complete)
        for char in word_complete:
            typeBar.send_keys(char)
            time.sleep(delay)
        loop()

# Used to re-run the script
def loop():
    time.sleep(2)
    input('\n\n\nPress enter to race again! \n(Make sure to close any pop-up windows first!)\n\n\n')
    print('Bot started, joining race!')
    try:
        browser.find_element_by_link_text('Enter a typing race').click()
        time.sleep(3)
        start()
    except:
        browser.find_element_by_link_text('Race Again »').click()
        time.sleep(1)
        try:
            browser.find_element_by_link_text('No thanks :(').click()
            time.sleep(3)
            start()
        except:
            time.sleep(3)
            start()

# Initial start
time.sleep(1.5)
input('\n\n\nPress enter to begin \n(Wait until you are done loading and are on the menu screen)\n\n\n')
print('Bot started, joining race!')
try:
    browser.find_element_by_link_text('Enter a typing race').click()
except:
    print('You need to wait for the site to finish loading!!!\nExiting program!')
    time.sleep(3)
time.sleep(1)
browser.find_element_by_link_text('change display format').click()
time.sleep(1)
browser.find_element_by_xpath('(//*[@type="radio"])[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@title="close this popup"]').click()
start()
