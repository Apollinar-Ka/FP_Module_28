from faker import Faker

# Основной URL тестируемого сайта
URL = 'https://b2c.passport.rt.ru'

# Путь к вебдрайверу
# PATH = './chromedriver.exe'
PATH = "напишите свой путь к вебдрайверу"

# Валидные данные для авторизации
valid_email = 'напишите свой валидный email'
valid_phone = 'напишите свой валидный телефон'
valid_password = 'напишите свой валидный пароль'

# Невалидные данные для авторизации
fake = Faker()
fake_password = fake.password()