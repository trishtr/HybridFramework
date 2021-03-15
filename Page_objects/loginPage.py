from selenium import webdriver
class Login:
    txt_username_id = "Email"
    txt_password_id = "Password"
    btn_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logout_link_text = "Logout"

    def __init__(self,driver):
        self.driver = driver
    def setUserName(self, username):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)
    def setPassWord(self, password):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()
