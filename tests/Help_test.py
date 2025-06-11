from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
import allure
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'


@allure.suite('Вкладка "Помощь"')
@allure.title('Проверка корректности перехода в раздел "Рекламный кабинет"')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
