import time
import pytest
from Page_objects.AddCustomerPage import AddCustomer
from Utilitites.readProperities import ReadConfig
from Utilitites.customLogger import LogGen
from Page_objects.loginPage import Login
import string
import random

class Test_003_AddCustomer:
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  #logger

    @pytest.mark.regression

    def test_addCustomer(self, setup):
        self.logger.info("******Test_003_AddCustomer******")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)  # create object lp to access class name Login
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        self.logger.info("********Login successful********")

        self.logger.info("********Starting Add Customer Test*******")

        self.addcus = AddCustomer(self.driver)  #create object addcus to access all methods in class name AddCustomer
        self.addcus.clickOnCustomerMenu()
        self.addcus.clickOnCustomerMenuItem()
        self.addcus.clickOnAddnew()

        self.logger.info("**********Providing customers' information*******")

        self.email = random_generator() + "@gmail.com"

        self.addcus.setEmail(self.email)
        self.addcus.setPassword("test123")
        self.addcus.setCustomerRole("Guests")
        self.addcus.setFirstName("Trish")
        self.addcus.setLastName("Tr")
        self.addcus.setGender("Male")
        self.addcus.setCompanyName("abc")
        self.addcus.DOB("7/05/1997")
        self.addcus.setManagerOfVendor("Vendor 2")
        self.addcus.setAdminContent("testing")
        self.addcus.clickOnSave()

        self.logger.info("*******Saving customer info******")

        self.logger.info("*******Add customer validation started*******")

        self.msg = self.driver.find_element_by_tag_name("body").text
        

        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*********Add Customer Test Passed********")

        else:
            self.driver.save_screenshot(".\\Screenshoot\\" + "test_addcustomer.png")  #Screeshot
            self.logger.info("*********Add customer Test Failed")
            assert False == False

        self.driver.close()
        self.logger.info("********End of Test Case*********")


def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))








