import selenium as selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

class WebInterface:

    def __init__(self):

        pass

    def get_driver(self):

        options=webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("useAutomationExtension",False)
        options.add_argument("--test-type")
        options.binary_location="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

        self.driver=webdriver.Chrome(chrome_options=options)

    def go_to(self,link):

        self.driver.get(link)

    def enter_text(self,x_path,value,submit=False):

        input_element=self.driver.find_element_by_xpath(x_path)
        input_element.send_keys(value)
        if submit==True:
            input_element.submit()

    def xpath_click(self,x_path):

        input_element=self.driver.find_element_by_xpath(x_path)
        input_element.click()

    def text_click(self,text):
        
        input_element=self.driver.find_element_by_link_text(text)
        input_element.click()

    def load_insist(self,x_path,value):

        elementMatch=False
        while(elementMatch==False):
            try:
                target_element=self.driver.find_element_by_xpath(x_path)
                if target_element.text==value:
                    elementMatch=True
            except NoSuchElementException:
                pass
            time.sleep(0.1)

if __name__ == "__main__":

    #Instantiate Web Interface
    WI=WebInterface()

    #Instantiate the web driver
    WI.get_driver()

    #Navigate to Kijiji
    WI.go_to('https://www.kijiji.ca/')

    #Go to Toronto in Kijiji
    WI.xpath_click('//*[@id="SearchLocationPicker"]')
    WI.text_click('Ontario (M - Z)')
    WI.text_click('Toronto (GTA)')
    WI.text_click('City of Toronto')
    
    #Wait untill City of Toronto is loaded
    WI.load_insist('//*[@id="mainPageContent"]/div[1]/div[1]/span[3]/h1','City of Toronto')

    #Go to buy/sell
    WI.xpath_click('//*[@id="SearchCategory"]')
    WI.text_click('Buy & Sell')

    #Wait untill Buy & Sell in City of Toronto is loaded
    WI.load_insist('//*[@id="mainPageContent"]/div[1]/div[1]/span[4]/h1','Buy & Sell in City of Toronto')

    #Search for keyword
    WI.enter_text('//*[@id="SearchKeyword"]','Glenn',True)

    #Close/kill the driver
    #WI.driver.quit()
