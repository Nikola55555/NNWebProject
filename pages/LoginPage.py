from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FIELD = (By.XPATH, "//input[@id='field_email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='field_password']")
    BUTTON_ENTER_TOP = (By.XPATH, "//a[@data-l='t,login_tab']")
    BUTTON_QR_CODE_TOP = (By.XPATH, "//a[@data-l='t,qr_tab']")
    BUTTON_ENTER_OK = (By.XPATH, "//input[@class='button-pro __wide']")
    BUTTON_ENTER_BY_QR_CODE = (By.XPATH, "//span[@class='qr-button-label']")
    BUTTON_LOGIN = (By.XPATH, "//div[@class='external-oauth-login-footer']/a[@data-l='t,register']")
    BUTTON_ENTER_BY_VK_ID = (By.XPATH, "//a[@data-l='t,vkc']")
    BUTTON_ENTER_BY_MAIL = (By.XPATH, "//a[@data-l=t',mailru']")
    BUTTON_ENTER_BY_MAIL = (By.XPATH, "//a[@data-l='t,yandex']")


class LoginPageHelper(BasePage):
    pass
