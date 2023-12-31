from selenium.webdriver.chrome.service import Service
from pages.locators import Locators
from selenium import webdriver
from config import PATH
import pytest


@pytest.fixture()
def browser():
    """
    Функция-фикстура для инициализации браузера
    """
    driver = Service(PATH)
    driver = webdriver.Chrome(service=driver)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture()
def auth(browser):
    """
    Функция-фикстура для авторизации пользователя в приложении
    """
    auth = Locators(browser)
    return auth