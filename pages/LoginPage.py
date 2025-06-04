import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FIELD = (By.XPATH, "//input[@id='field_email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='field_password']")
    TAB_LOGIN = (By.XPATH, "//a[@data-l='t,login_tab']")
    TAB_QR_CODE_SWITCHER = (By.XPATH, "//a[@data-l='t,qr_tab']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//input[@class='button-pro __wide']")
    QR_CODE_LOGIN_BUTTON = (By.XPATH, "//span[@class='qr-button-label']")
    RESTORY_LINK = (By.XPATH, "//a[@data-l='t,restore']")
    REGISTER_LINK = (By.XPATH, "//div[@class='external-oauth-login-footer']/a[@data-l='t,register']")
    VK_ID_LOGIN_BUTTON = (By.XPATH, "//a[@data-l='t,vkc']")
    MAIL_RU_LOGIN_BUTTON = (By.XPATH, "//a[@data-l='t,mailru']")
    YANDEX_LOGIN_BUTTON = (By.XPATH, "//a[@data-l='t,yandex']")
    ERROR_TEXT = (By.XPATH, "//div[@class='input-e login_error']")
    GO_BACK_BUTTON = (By.XPATH, "//*[@data-l='t,cancel']")
    SUPPORT_BUTTON = (By.XPATH, "//div[@class='external-oauth-login-help portlet_f']")
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')



class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.TAB_LOGIN)
        self.find_element(LoginPageLocators.TAB_QR_CODE_SWITCHER)
        self.find_element(LoginPageLocators.SUBMIT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_LINK)
        self.find_element(LoginPageLocators.VK_ID_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_RU_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.SUBMIT_LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле логин')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()


    @allure.step('Заполняем поле пароль')
    def type_password(self, password):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

