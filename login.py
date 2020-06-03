

from selenium import webdriver
from getpass import getpass
from time import sleep


def sign_in(username, password):
    driver = webdriver.Chrome(executable_path= 'C:\\Users\\Soraya Wete\\.wdm\\drivers\\chromedriver\\83.0.4103.39\\win32\\chromedriver.exe')
    url = "https://www.instagram.com/"
    driver.get(url)
    driver.maximize_window()

    username_box = driver.find_element_by_xpath("//input[contains(@aria-label, 'Phone number')]")\
        .send_keys(username)
    pwd_box = driver.find_element_by_xpath("//input[contains(@aria-label, 'Password')]")\
        .send_keys(password)
    login_button = driver.find_element_by_xpath("//button[contains(@class, 's')]/div")\
        .click()
    sleep(4)                        #4 seconds latency, in case of poor internet connection

#click "Not Now" on save password notification box
#Equally click on "Not Now" on the alert notification box
    savepwd_notification_box = driver.find_element_by_xpath("//button[contains(@class, 'yW')]")
    if savepwd_notification_box.is_displayed():
        savepwd_notification_box.click()
        sleep(1)
    alert_notification_box = driver.find_element_by_xpath("//button[contains(@class, 'H')]")
    if alert_notification_box.is_displayed():
        alert_notification_box.click()
    sleep(2)                       #2 seconds latency, in case of poor internet connection
    driver.close()
    driver.quit()


sign_in(input("Enter your e-mail or username: "), getpass('Enter your password: '))
