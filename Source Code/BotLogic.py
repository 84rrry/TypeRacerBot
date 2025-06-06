import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

def findtext(text):
    """A function to parse the text from the page source."""
    start = 'The race is about to start!Guest(you)'
    end = 'change display format'
    s = text.rfind(start)
    e = text.rfind(end)
    text = text[s+len(start):e]
    return text[text.rfind('wpm')+3:]

def fasterThanYou(WPM, text, driver):
    """A function to type the text at a given speed."""
    charsPerSec = round(WPM * 5 / 60, 2)
    try:
        # Wait for the input field to be available and then find it
        typingField = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.txtInput')))
        
        # Type each character with a calculated delay
        for char in text:
            typingField.send_keys(char)
            # The delay is slightly adjusted to feel more natural
            time.sleep(1 / (charsPerSec * 1.5))
    except TimeoutException:
        print('Something went wrong, could not find the typing field!')


def get_webdriver(browser_choice):
    """Initializes and returns the selected webdriver."""
    if browser_choice == '1':
        print("Initializing Google Chrome...")
        return webdriver.Chrome()
    elif browser_choice == '2':
        print("Initializing Mozilla Firefox...")
        return webdriver.Firefox()
    elif browser_choice == '3':
        print("Initializing Microsoft Edge...")
        return webdriver.Edge()
    else:
        # Fallback to a default browser if the choice is somehow invalid
        print("Invalid browser choice. Defaulting to Edge.")
        return webdriver.Edge()


def TypeRacerbot(browser, speed):
    """Main function to run the TypeRacer bot."""
    driver = None # Initialize driver to None to ensure it's defined for the finally block
    try:
        # Set up the web driver based on user choice
        driver = get_webdriver(browser)
        driver.maximize_window()
        
        # Navigate to the website 
        driver.get('https://play.typeracer.com/')

        # Wait for the "Enter a Typing Race" link and click it
        enter_race_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Enter a Typing Race')))
        enter_race_button.click()
        print("Page is ready and race is entered!")

        # This sleep is part of the original logic to allow the race to load
        time.sleep(5)
        
        # Use BeautifulSoup to parse the page as per the original logic
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        text = soup.get_text()
        text_to_type = findtext(text)
        print('\nText to type has been loaded.')

        # Find the countdown timer and wait for it to finish
        # This uses a more reliable selector to avoid the original error
        timer_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'countdownPopup')]//span[@class='time']"))
        )
        timer = timer_element.text[1:] # Get text like ':03' and slice to '03'
        print('Seconds to go:', timer)
        time.sleep(int(timer) + 1)
        
        print("Race has started. Typing now...")
        
        # Start typing
        fasterThanYou(speed, text_to_type, driver)     
        
        print('\nBot has finished typing. The script will close in 15 seconds.')
        time.sleep(15)

    except TimeoutException:
        print("Loading took too much time or an element could not be found!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the driver quits even if an error occurs
        if driver:
            driver.quit()