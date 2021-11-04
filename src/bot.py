from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import constants
import time
from selenium.common.exceptions import NoSuchElementException
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
        xpath = '//*[@id="app"]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div'
        if not self.hasXpath(xpath):
            return False
        return self.driver.find_element_by_xpath(xpath).text == 'Waiting for studies.'
    
    def hasXpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except:
            return False
    
    # def check_exists_by_xpath(self, xpath):
    #     try:
    #         self.driver.find_element_by_xpath(xpath)
    #     except NoSuchElementException:
    #         return False
    #     return True

    def find_studies(self):
        time.sleep(10)
        pygame.mixer.init()
        sound = pygame.mixer.Sound(constants.SOUND_ON_STUDY)
        while True:
            if self.is_waiting_for_studies():
                time.sleep(random.randint(constants.MIN_REFRESH_TIME - 7, constants.MAX_REFRESH_TIME - 7))
                self.driver.refresh()
                time.sleep(7)
                print('No studies found')
            else:
                print('Study found')
                sound.play()
                self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[1]/ul/li/div').click()
                time.sleep(1)
                xpath = '//*[@id="app"]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/form/button'
                self.driver.find_element_by_xpath(xpath).click()
                if not self.hasXpath(xpath):
                    sound.play()
                    break
                else:
                    time.sleep(2)
                    # not_interest_xpath = '//*[@id="app"]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/a'
                    self.driver.refresh()
                    time.sleep(random.randint(constants.MIN_REFRESH_TIME - 6, constants.MAX_REFRESH_TIME - 6))