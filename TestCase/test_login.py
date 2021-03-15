from selenium import webdriver
import pytest
from Page_objects.loginPage import Login
from Utilitites.readProperities import ReadConfig
from Utilitites.customLogger import LogGen

class Test_001_Login:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()    #call the loggen method inside LogGen class


    @pytest.mark.regression

    def test_homepage_title(self, setup):
        self.logger.info("************Test Case 001***********")
        self.logger.info("************Verify Home Page Title***********")

        self.driver = setup
        self.driver.get(self.base_URL)
        acc_title = self.driver.title
        if acc_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************Home page Title is passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshoot\\"+"test_homepage_title.png")
            self.driver.close()
            self.logger.info("************Home page Title is failed***********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************Verify Login Test***********")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = Login(self.driver)        #create object lp to access class name Login
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************Login Page is passed***********")
        else:
            self.driver.close()
            self.logger.error("************Login Page is failed***********")
            assert False





