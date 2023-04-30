from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import sqlite3

# Открываем соединение с базой данных
conn = sqlite3.connect('profile.db')
cursor = conn.cursor()

# Получаем список профилей из базы данных
cursor.execute('SELECT * FROM `cookie_profile`')
profiles = cursor.fetchall()

# Запускаем браузер с помощью драйвера Chrome
driver = webdriver.Chrome('/path/to/chromedriver')

# Создаем сессию для каждого профиля
for profile in profiles:
    # Получаем Cookie профиля из базы данных
    cookie = profile[2]

    # Если есть Cookie, передаем их в сессию браузера
    if cookie:
        driver.get('https://news.google.com/home')
        for c in cookie.split('; '):
            name, value = c.split('=', 1)
            driver.add_cookie({'name': name, 'value': value})

    # Получаем список ссылок на новости из модуля Requests
    news_links = ['https://news.google.com/articles/CBMi1234']  # здесь вам нужно использовать свой код из модуля Requests для получения списка ссылок на новости

    # Выбираем случайную ссылку на новость из списка
    random_link = random.choice(news_links)

    # Переходим по выбранной ссылке
    driver.get(random_link)

    # Прокручиваем страницу с рандомной задержкой
    for i in range(random.randint(1, 5)):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(random.randint(1, 3))

    # Сохраняем Cookie профиля в базу данных
    cookie = '; '.join([f'{cookie["name"]}={cookie["value"]}' for cookie in driver.get_cookies()])
    cursor.execute('UPDATE `cookie_profile` SET `cookie` = ?, `last_run` = ?, `run_count` = `run_count` + 1 WHERE `id` = ?', (cookie, time.time(), profile[0]))
    conn.commit()

# Закрываем браузер и соединение с базой данных
driver.quit()
cursor.close()
conn.close()
