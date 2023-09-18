from config import *
import pytest

# Открывается страница с формой "Авторизация"
def test_authorization_is_exists(auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# Пункт меню "Почта" кликабелен и открывает форму авторизации по почте и паролю
def test_mail_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    assert auth.find_element(auth.LOCATOR_INPUT_MAIL)


# Базовая позитивная проверка авторизации по валидным телефону/почте и паролю.
# По умолчанию при открытии страницы открыта форма авторизации по телефону -- таб "Телефон"
# При вводе почты таб "Телефон" переключается на таб "Почта"
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_valid_data(auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Негативный тест авторизации по валидным телефону/почте и невалидному паролю. Появляется сообщение об ошибке.
@pytest.mark.fail_if_captcha
@pytest.mark.parametrize('username', [valid_phone, valid_email], ids=['valid phone', 'valid email'])
def test_auth_fake_password(auth, username):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, username)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, fake_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# Негативный тест авторизации по пустому полю ввода телефона и валидному паролю. Появляется сообщение об ошибке.
# Негативный тест авторизации по пустому полю ввода телефона и пустому полю пароля. Появляется сообщение об ошибке.
@pytest.mark.parametrize('password', [valid_password, ''], ids=['valid password', 'invalid password (empty input)'])
def test_auth_empty_phone(auth, password):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_PHONE)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG


# Негативный тест авторизации по пустому полю ввода почты и валидному паролю. Появляется сообщение об ошибке.
def test_auth_empty_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_MAIL_MSG


# Негативный тест авторизации по пустому полю ввода логина и валидному паролю. Появляется сообщение об ошибке
def test_auth_empty_login(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LOGIN_MSG


# Негативный тест авторизации по пустому полю ввода лицевого счета и валидному паролю.
# Появляется сообщение об ошибке.
def test_auth_empty_ls(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LS_MSG


# Ссылка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
def test_forgot_password(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# Ссылка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
def test_register(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION


# Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Почта"

@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Логин"
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_login(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# Позитивная проверка авторизации по валидному телефону и паролю при вводе телефона в таб "Лицевой счет"
@pytest.mark.fail_if_captcha
def test_auth_valid_phone_tab_ls(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, valid_phone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, valid_password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert active_tab_name == 'Телефон'
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# Позитивная проверка перехода на страницу авторизации через соц. сеть Вконтакте
def test_auth_social_network_vk(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_VK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_VK)


# Позитивная проверка перехода на страницу авторизации через соц. сеть Однокласники
def test_auth_social_network_ok(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_NETWORK_OK)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_OK)


# Позитивная проверка перехода на страницу авторизации через почтовый клиент Mail.ru
def test_auth_social_mail(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_MAIL)
    assert auth.find_element(auth.LOCATOR_IDENTIFIER_MAIL)


# Позитивная проверка перехода на страницу авторизации через сервис клиент Yandex ID
def test_auth_social_yandex(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
    if auth.find_element(auth.LOCATOR_SOCIAL_YANDEX):
        auth.click_element(auth.LOCATOR_SOCIAL_YANDEX)
        assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)
    else:
        assert auth.find_element(auth.LOCATOR_IDENTIFIER_YANDEX)


# Позитивная проверка перехода на страницу пользовательского соглашения
def test_agreement_is_clickable(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_AGREEMENT)
    windows = auth.driver.window_handles
    auth.driver.switch_to.window(windows[-1])
    assert auth.find_element(auth.LOCATOR_AGREEMENT_ROOT)