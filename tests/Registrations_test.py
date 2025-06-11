from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
import allure
from pages.RegistrationPage import RegistrationPageHelperHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Регистрация пользователя по телефону')
@allure.title('Проверка корректности телефонного кода выбранной страны в поле "Номер телефона"')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone__field_value()
    assert Actual_country_code == Selected_country_code