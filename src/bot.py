from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import constants
import time
import random
import pygame


class Bot():
    def __init__(self):
        options = Options()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(options = options, executable_path = constants.CRHOMEDRIVER_PATH)

    def login(self, username, password):
        self.driver.get(constants.PROLIFIC_LOGIN)
        # Input do Username
        self.driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
        # Input da password
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/div/input').send_keys(password)
        # Botão de login
        self.driver.find_element_by_xpath('//*[@id="login"]').click()

    def is_logged_in(self):
        return self.driver.current_url == constants.PROLIFIC_STUDIES
    
    def is_waiting_for_studies(self):
        return self.hasXpath and self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div').text == 'Waiting for studies.'
    
    def hasXpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

    def find_studies(self):
        time.sleep(10)
        pygame.mixer.init()
        sound = pygame.mixer.Sound('/usr/share/sounds/freedesktop/stereo/phone-incoming-call.oga')
        while True:
            if self.is_waiting_for_studies():
                self.driver.refresh()
                print('No studies found')
                time.sleep(random.randint(constants.MIN_REFRESH_TIME, constants.MAX_REFRESH_TIME))
            else:
                print('Study found')
                sound.play()