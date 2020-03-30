from bot import TypingBot
from selenium.common.exceptions import TimeoutException
import time
import sys

# parameters (180 for fast)
WPM = 60000  # randomized
URL = 'https://play.typeracer.com?rt=1ydrug3bdp'



def main(URL, WPM):
    TP = TypingBot(URL, WPM)
    try:
        TP.initPage()
        TP.enterRace()
        # todo - don't make account
        TP.race()

    except TimeoutException:
        print('error occured')
    time.sleep(2)
    k
    TP.driver.quit()


if __name__=="__main__":
    main(URL, WPM)





