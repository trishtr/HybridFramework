import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")     #read data from config.ini file

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "base_URL")        #get method to retrieve data
        return url
    @staticmethod
    def getUserName():
        username = config.get("common info", "username")
        return username
    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
