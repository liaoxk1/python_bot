# -*- coding: utf-8 -*-
"""
Auto fill daily temperature and health status for Company Covid-19 Control
The code sleep(2) after each step is for illustration purpose

@author: kyle
"""

from selenium import webdriver
from time import sleep

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def auto_fill(self):
        self.driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=2jxJBV94SU-zRcLM5aDh76XCRUl0ORpHpjYu8mZbPqBUQ1NMU1JDRVNITjlIME5RMFFBQ1RRNjY0VS4u')        
        sleep(1)
     
        btn_temp = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/label/span/span')
        btn_temp.click()
        
        btn_next1 = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div/button')
        btn_next1.click()
        sleep(1)
        
        btn_wfh = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[10]/div/label/span/span')
        btn_wfh.click()
        
        btn_yea = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/label/span/span')
        btn_yea.click()
       
        btn_next2 = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/button')
        btn_next2.click()     
        sleep(1)
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/input')
        pw_in.send_keys('40204886')
        
        btn_next3 = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/button')
        btn_next3.click()
        sleep(1)
        
        btn_good = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/label/span/span')
        btn_good.click()
        
        btn_normal = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/label/span/span')
        btn_normal.click()
        
        btn_submit = self.driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/button')
        btn_submit.click()
        
bot = Bot()
bot.auto_fill()