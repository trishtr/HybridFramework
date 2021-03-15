from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "ie":
        driver = webdriver.IE()
        print("Launching on IE")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching on Firefox")
    else:
        driver = webdriver.Chrome()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####PYtest HTML Report
#It s hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'HybridFramework'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Trish'
#It s hook for delete/ modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


