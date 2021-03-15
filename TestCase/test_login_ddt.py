from selenium import webdriver
import pytest
from Page_objects.loginPage import Login
from Utilitites.readProperities import ReadConfig
from Utilitites.customLogger import LogGen
from Utilitites import XLUtilities
import time

class Test_002_Login:
    base_URL = ReadConfig.getApplicationURL()
    path = ".//TestData/logindata.xlsx"
    logger = LogGen.loggen()    #call the loggen method inside LogGen class

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************TC_002_DDT_Login***********")
        self.logger.info("************Verify Login DDT Test***********")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = Login(self.driver)        #create object lp to access class name Login

        self.rows = XLUtilities.getRowCount(self.path, 'Sheet1')
        print("Number of Rows", self.rows)

        lst_status = []
        for r in range(2, self.rows):
            self.user = XLUtilities.readData(self.path, 'Sheet1', r, 1)
            print(self.user)
            self.password = XLUtilities.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassWord(self.password)
            self.lp.clickLogin()
            time.sleep(5)


            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********Pass*******")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("********Fail*******")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("********Fail*******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("********Pass*******")
                    lst_status.append("Pass")
                print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("********Login_Test_DDT_Pass******")
            self.driver.close()
            assert True
        else:
            self.logger.info("********Login_Test_DDT_Fail********")
            self.driver.close()
            assert False

        self.logger.info("***********End of Login DDT test********")
        self.logger.info("***********Completion of Login DDT test*********");





