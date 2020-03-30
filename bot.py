

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os



class TypingBot:

    def __init__(self, URL, WPM):

        self.driver = webdriver.Chrome()
        self.URL = URL
        self.WPM = WPM
        self.full_text = ""
        self.driver.get(self.URL)
        print('constructed')

    def initPage(self):
        """Loads page."""
        try:
            # gets typeingbox
            WebDriverWait(self.driver,60).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gwt-Anchor"))
            )
            print('inited')
        except TimeoutException:
            print('failed to init page')

    def enterRace(self):
        """Clicks Enter race button from start screen."""

        #ctrl+Alt+I = start race keyboard shortcut
        self.driver.find_element_by_tag_name("body").send_keys(
            Keys.CONTROL+Keys.ALT+'i')  # enters race from default page
        self.driver.find_element_by_tag_name("body").send_keys(
            Keys.CONTROL + Keys.ALT + 'k') # enters race from invite

        #enter race
        try:
            WebDriverWait(self.driver,60).until(
                EC.visibility_of_element_located((By.CLASS_NAME,"gameStatusLabel"))
            )
            print('entered race')
        except TimeoutException:
            print('could not enter race')

    def race(self):
        """race"""
        try:
            # -- get text --
            time.sleep(1)
            self.getText()

            # -- wait for countdown --
            input_field = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input.txtInput")))

            # -- type letter --
            for letter in self.full_text:
                input_field.send_keys(letter)
                time.sleep(self.time)
        except TimeoutException:
            print('could not enter race')
        print("- Typing complete!")

    # -- todo --
    def wait(self) :
        """wait until next race is joinable, the countdown to next race
           will be displayed before race moves
        """
        span = ""
        while span != "You will":
            span =  WebDriverWait(self.driver,60).until(
                EC.visibility_of_element_located((By.CLASS_NAME,"timeDisplayCaption"))
            ).text
            print('hello')
            print(span)
            span = span[:8]
            print(span)
            time.sleep(1)
        time.sleep(10)

    def getText(self):
        """Function to return a list of the text.
            span[0] is first letter of first word span[1] remaining of first word
            span[2] is all remaining text
        """
        try:
            span = self.driver.find_elements_by_xpath("//span[@unselectable='on']")
            puncs = ['!', '.', ',', '?', '-', "'", ':']

            # edge cases: first word 1 letter, punctuation mark after word
            if len(span) == 2:
                if any(p in span[1].text[0] for p in puncs):
                    self.full_text = span[0].text + span[1].text
                else:
                    self.full_text = span[0].text + " " + span[1].text
            elif any(p in span[2].text[0] for p in puncs):
                self.full_text = span[0].text + span[1].text + span[2].text

            else:
                self.full_text = span[0].text + span[1].text + " " + span[2].text
            self.full_text += " "

            #calculate time for each letter
            ajdWPM = random.randint(self.WPM+25, self.WPM+29) #ajusted for lag
            print(ajdWPM-27)
            CPM = ajdWPM*5 # charcters per minute
            CPS = CPM/60 # characters per second
            self.time = (1/CPS)

        except TimeoutException:
            print('could not get text\n')








