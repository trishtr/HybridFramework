import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_submenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAdd_new_customer_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txt_Email_xpath = "//*[@id='Email']"
    txt_Password_xpath = "//*[@id='Password']"
    txt_firstname_xpath = "//*[@id='FirstName']"
    txt_lastname_xpath = "//*[@id='LastName']"
    rd_male_id = "Gender_Male"
    rd_female_id = "Gender_Female"
    txt_DOB_xpath = "//*[@id='DateOfBirth']"
    txt_companyname_xpath = "//*[@id='Company']"
    checkbox_taxexempt_id = "IsTaxExempt"
    txt_newsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div"
    lst_txt_newsletter1_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    lst_txt_newsletter2_xpath = "//*[@id='b88510f8-12dc-46b9-a51d-c05298917f94']"
    txt_customer_roles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lst_Administrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lst_Moderator_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lst_Guests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lst_Registered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lst_Vendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    dr_manager_vendor_xpath = "//*[@id='VendorId']"
    txt_Admin = "//*[@id='AdminComment']"
    btn_save = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"


    lst_Register_del_btn_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"



    def __init__(self, driver):       #constructor, take driver from actual TC to initiate to local driver
        self.driver = driver
    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_submenu_xpath).click()
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAdd_new_customer_xpath).click()
    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txt_Email_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txt_Password_xpath).send_keys(password)
    def setCustomerRole(self, role):
        self.driver.find_element_by_xpath(self.txt_customer_roles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listrole = self.driver.find_element_by_xpath(self.lst_Registered_xpath)
        elif role == "Administrators":
            self.listrole = self.driver.find_element_by_xpath(self.lst_Administrators_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lst_Register_del_btn_xpath).click()
            self.listrole = self.driver.find_element_by_xpath(self.lst_Guests_xpath)
        elif role == "Forum Moderator":
            self.listrole = self.driver.find_element_by_xpath(self.lst_Moderator_xpath)
        elif role == "Vendors":
            self.listrole = self.driver.find_element_by_xpath(self.lst_Vendors_xpath)
        else:
            self.listrole = self.driver.find_element_by_xpath(self.lst_Registered_xpath)
        time.sleep(3)
        #self.listrole.click() cannot perform
        self.driver.execute_script("arguments[0].click();", self.listrole)  #JV script alternative ways to perform click action for this list
    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.dr_manager_vendor_xpath))
        drp.select_by_visible_text(value)
    def setGender(self,gender):
        if gender =="Male":
            self.driver.find_element_by_id(self.rd_male_id).click()
        elif gender =="Female":
            self.driver.find_element_by_id(self.rd_female_id).click()
        else:
            self.driver.find_element_by_id(self.rd_male_id).click()
    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(fname)
    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lname)
    def DOB(self, dob):
        self.driver.find_element_by_xpath(self.txt_DOB_xpath).send_keys(dob)
    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txt_companyname_xpath).send_keys(comname)
    def checkTaxExempt(self):
        self.driver.find_element_by_id(self.checkbox_taxexempt_id).click()

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txt_Admin).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_save).click()

















