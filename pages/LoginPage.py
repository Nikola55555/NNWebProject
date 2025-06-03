from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FIELD = (By.XPATH, "//input[@id='field_email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='field_password']")
    TAB_LOGIN = (By.XPATH, "//a[@data-l='t,login_tab']")
    TAB_QR_CODE_SWITCHER = (By.XPATH, "//a[@data-l='t,qr_tab']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//input[@class='button-pro __wide']")
    QR_CODE_LOGIN_BUTTON = (By.XPATH, "//span[@class='qr-button-label']")
    REGISTER_LINK = (By.XPATH, "//div[@class='external-oauth-login-footer']/a[@data-l='t,register']")
    VK_ID_LOGIN_BUTTON = (By.XPATH, "//a[@data-l='t,vkc']")
    MAIL_RU_LOGIN_BUTTON = (By.XPATH, "//a[@data-l=t',mailru']")
    YANDEX_LOGIN_BUTTON = (By.XPATH, "//a[@data-l='t,yandex']")


class LoginPageHelper(BasePage):
    pass
