from selenium import webdriver
import pytest
import time
from Page_objects.SearchCustomerPage import searchCustomer
from Utilitites.readProperities import ReadConfig
from Utilitites.customLogger import LogGen
from Page_objects.loginPage import Login
from Page_objects.AddCustomerPage import AddCustomer
class Test_001_Login:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("******Test_004_SearchCustomerByEmail******")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)  # create object lp to access class name Login
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.logger.info("********Login successful********")

        self.logger.info("********Starting Search*********")

        self.addcus = AddCustomer(self.driver) # create object to access method in add customer class
        self.addcus.clickOnCustomerMenu()
        self.addcus.clickOnCustomerMenuItem()

        self.logger.info("**********Searching********")

        self.searchcus = searchCustomer(self.driver)
        self.searchcus.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcus.clickSearch()
        time.sleep(5)
        status = self.searchcus.searchCustomersByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("************ TC _search customer by email completed *******")

        self.driver.close()