import selenium
from selenium import webdriver
import time
import os
from configparser import ConfigParser
from datetime import date


class profile_updater:
    
    def get_url(self,driver,url):
        driver.get(url)
        self.logger('*** Naukri Profile Opened Successfully ***')
        time.sleep(2)

    def credential(self,driver,usr,paswd):
        try:
            driver.find_element_by_id('usernameField').send_keys(usr)
            self.logger('Username Entered ... ')
        except:    
            driver.find_element_by_id('usernameField').send_keys(usr)
            self.logger('Retrying Username ... ')
        try:
            driver.find_element_by_id('passwordField').send_keys(paswd)
            self.logger('Password Entered ... ')
        except:
            driver.find_element_by_id('passwordField').send_keys(paswd)
            self.logger('Retrying Password ... ')
        try:
            driver.find_element_by_xpath('//div[@class="col s12"]').find_element_by_xpath('//button[@class="waves-effect waves-light btn-large btn-block btn-bold blue-btn textTransform"]').click()
            time.sleep(6)
        except:
            driver.find_element_by_xpath('//div[@class="col s12"]').find_element_by_xpath('//button[@class="waves-effect waves-light btn-large btn-block btn-bold blue-btn textTransform"]').click()
        try:
            driver.find_element_by_xpath('//div[@class="col s12 dp-wrapper center"]').click()
            self.logger('Naukri Profile Opened !')
            time.sleep(5)
        except:
            driver.find_element_by_xpath('//div[@class="col s12 dp-wrapper center"]').click()
            self.logger('Naukri Profile Opened !')
        
    def uploader(self,driver,file):
        file_upload = driver.find_element_by_xpath('//div[@class="uploadCont"]').find_element_by_xpath('//input[@type="file"]')
        file_upload.send_keys(os.getcwd()+'\\'+file)
        time.sleep(2)
        self.logger('New Resume uploaded ... ')
        self.logger('*** Naukri Profile updated Successfully ***')
        time.sleep(2)

    def logger(self,text):
        filename = 'log_'+str(date.today())+'.txt'
        if os.path.exists('log\\'+filename)==False:
            file = open('log\\'+filename,'w')
            file.write(text)
            file.write('\n')
        else:
            file = open('log\\'+filename,'a')
            file.write(text)
            file.write('\n')
        file.close()    


if __name__ == "__main__":

    obj = profile_updater() #Create a object.
    print('Object created for profile updater')
    conf_parse = ConfigParser()
    print('Object created for Config parser')
    
    driver = webdriver.Chrome('chromedriver.exe')
    print('Chrome driver loaded successfully ... ')

    #Reading the contents of CONFIG File
    CONFIG_FILE = 'config\\config.ini'
    conf_parse.read(CONFIG_FILE)
    url = conf_parse.get("URL","url")
    obj.get_url(driver,url)
    print('Url entered ... ')
    
    username = conf_parse.get("USERNAME","username")
    password = conf_parse.get("PASSWORD","password")
    obj.credential(driver,username,password)
    print('Username and Password entered ... ')
    
    logger = conf_parse.get("LOGGER","log_file")
    obj.logger(logger)
    print('Logger file called ... ')
    
    input_file = conf_parse.get("INPUT FILE","file_name")
    obj.uploader(driver,input_file)
    print('Updated resume uploaded ... ')
    driver.close()