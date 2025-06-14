import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    driver = webdriver.Remote(command_executor='http://31.207.74.100:4444/wd/hub', options=options)
    #driver = webdriver.Remote(command_executor='http://31.207.74.100:4444', options=options)
    yield driver
    if driver:
        driver.quit()
