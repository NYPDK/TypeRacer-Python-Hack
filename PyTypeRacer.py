from selenium import webdriver
import time, re

# Delay between typed characters (default 0.1)
delay = 0.1

browser = webdriver.Chrome()
browser.get('https://play.typeracer.com/')

# Detects when the countdown is over
def start():
    timer = True
    while timer == True:
        try:
            count_down = browser.find_element_by_xpath('//*[@class="countdownPopup horizontalCountdownPopup"]')
            print('Waiting for countdown')
        except:
            timer = False
            print('Count down complete! Starting!')
            time.sleep(1)
            main()
        time.sleep(0.5)

# Handles all the logic
def main():
    typeBar = browser.find_element_by_class_name('txtInput')
    word1 = browser.find_element_by_xpath('(//*[@unselectable="on"])[1]').text
    word2 = browser.find_element_by_xpath('(//*[@unselectable="on"])[2]').text

    try:
        word4 = browser.find_element_by_xpath('(//*[@unselectable="on"])[4]').text
        word3 = browser.find_element_by_xpath('(//*[@unselectable="on"])[3]').text

        word_check = (word1 + word2 + ' ' + word3 + ' ' + word4)
        word_complete = re.sub(' , ', ', ', word_check)
        print('Words: \n' + word_complete)
        for char in word_complete:
            typeBar.send_keys(char)
            time.sleep(delay)
        loop()
    except:
        try:
            word3 = browser.find_element_by_xpath('(//*[@unselectable="on"])[3]').text

            word_check = (word1 + word2 + ' ' + word3)
            word_complete = re.sub(' , ', ', ', word_check)
            print('Words: \n' + word_complete)
            for char in word_complete:
                typeBar.send_keys(char)
                time.sleep(delay)
            loop()
        except:
            word_check = (word1 + word2)
            word_complete = re.sub(' , ', ', ', word_check)
            print('Words: \n' + word_complete)
            for char in word_complete:
                typeBar.send_keys(char)
                time.sleep(delay)
            loop()

# Used to re-run the script
def loop():
    time.sleep(1)
    input('Press enter to race again! (Make sure to close any popup windows first!)')
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
time.sleep(5)
browser.find_element_by_link_text('Enter a typing race').click()
time.sleep(3)
start()