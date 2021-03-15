class searchCustomer:
    txt_email_xpath = "//*[@id='SearchEmail']"
    txt_firstName_xpath = "//*[@id='SearchFirstName']"
    txt_lastName_xpath = "//*[@id='SearchLastName']"
    btn_search_xpath = "//*[@id='search-customers']"
    tbl_search_xpath = "//table[@role='grid']"     #"//*[@id='customers-grid_wrapper']"
    tbl_xpath = "//*[@id='customers-grid']"
    tbl_rows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tbl_cols_xpath = "//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):   #constructor
        self.driver = driver
    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txt_lastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_lastName_xpath).send_keys(lastname)
    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txt_firstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_firstName_xpath).send_keys(firstname)
    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def getNumRows(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_rows_xpath))

    def getNumCols(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_cols_xpath))

    def searchCustomersByEmail(self, email):
        flag = False
        for r in range (1, self.getNumRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            email_id = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag
    def searchCustomersByName(self, name):
        flag = False
        for r in range (1, self.getNumRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            name_id = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name_id == name:
                flag = True
                break
        return flag







