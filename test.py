import sys
import os
import time
from selenium import webdriver #Selenium Webdriverをインポートして

driver = webdriver.Chrome("./chromedriver.exe") #Chromeを動かすドライバを読み込み
driver.get("https://twitter.com/yume120440")

def main():

    tag = input()

    test = driver.find_elements_by_xpath("//" + tag)

    for a in test:
        print(a.text)

    print("\n")
    os.system('PAUSE')

while True:
    try:
        main()
    except:
        pass
