from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# You need to have selenium and phantomjs installed
# All that time.sleeps are just to fool fb

def fblogin(email, password):
    driver.get("https://facebook.com")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()
    try:
        driver.find_element_by_xpath('//*[@id="findFriendsNav"]').text == True
        print 'Logged.'
    except:
        print 'Fuck zuckenberg.'
        driver.quit()

def fbpost(fpname, newpost):
    i = 0
    driver.get("https://www.facebook.com/" + fpname + "/publishing_tools/")
    print 'Fanpage loaded.'
    driver.find_element_by_xpath('//*[@id="facebook"]').click()
    time.sleep(120) #1
    driver.find_element_by_xpath('//span/div/div[2]/div[1]/div/div[1]/span[2]/button').click()
    time.sleep(60) #2
    while i < 5:
        try:
            driver.find_element_by_xpath('//div[2]/div[2]/div/div/div/div/div[2]/div').send_keys(newpost)
            driver.find_element_by_xpath('//div[4]/div[2]/div/div[2]/div/div/button').click()
            print 'Post added.'
            driver.save_screenshot('screen.png')
            time.sleep(60) #3
            break
        except:
            i += 1
            print 'Error while adding, sry bro. Gimme 15 secs.'
            driver.save_screenshot('screen.png')
            time.sleep(15)
    if i == 5:
        print 'Sorry, maybe next time...'
        driver.save_screenshot('screen.png')

        
