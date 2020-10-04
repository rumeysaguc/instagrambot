from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
from adres import email,password

url = 'https://www.instagram.com/accounts/login/'
browser = webdriver.Chrome()

class Instagram:
    def __init__(self, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get(url)
        self.browser.maximize_window()
        time.sleep(3)
        emailInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(email)
        passwordInput.send_keys(password)
        buton = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
        buton.click()


instgrm = Instagram(email, password)
instgrm.signIn()


