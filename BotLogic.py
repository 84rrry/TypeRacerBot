
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import  time 
#A function to find the website
def findtext(text):
    start = 'The race is about to start!Guest(you)'
    end = 'change display format'
    s=text.rfind(start)
    e=text.rfind(end)
    text=text[s+len(start):e]
    return text[text.rfind('wpm')+3:]
#A function to type
def fasterThanYou(WPM,text,driver):
    #controls typing speed
    charsPerSec=round(WPM*5/60,2)
    # pyautogui.PAUSE = round(1/charsPerSec,3)
    # pyautogui.PAUSE =0.0
    # print(pyautogui.PAUSE)
    try:
        typingField=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'txtInput')))
    
    except :
        os.system('cls')
        print( 'something went wrong try again!')
    for char in text:
        # pyautogui.press(char)
        typingField.send_keys(char)
        time.sleep(1/(charsPerSec*1.5))
    
    
def TypeRacerbot(speed):
    #set the web driver 
    driver = webdriver.Edge()
    driver.maximize_window() # For maximizing window
    #Gettin to the website 
    driver.get('https://play.typeracer.com/')

    try:
        button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,'Enter a Typing Race')))
        print ("Page is ready!")
    except TimeoutException:
        print( "Loading took too much time!")
    button.click()
    time.sleep(5)
    html=driver.page_source
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.get_text()
    text=findtext(text)
    timer=driver.find_element(By.XPATH,'/html/body/div[4]/div/table/tbody/tr/td/table/tbody/tr/td[3]/div/span').text[1:]
    print('Secondes to go:',timer)
    time.sleep(int(timer)+1) 
    fasterThanYou(speed,text,driver)     
    time.sleep(15)
# driver.quit()


