import requests
from bs4 import BeautifulSoup

# Выполняем GET-запрос к странице
response = requests.get('https://news.google.com/home')

# Парсим HTML-код страницы с помощью BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все ссылки на новости на странице
news_links = [link['href'] for link in soup.find_all('a', href=True) if '/articles/' in link['href']]

# Выводим список ссылок на новости
print(news_links)

# https://news.google.com/articles/CBMiJWh0dHBzOi8vd3d3LmludGVyZmF4LnJ1L3J1c3NpYS84OTczMjLSASJodHRwczovL3d3dy5pbnRlcmZheC5ydS9hbXAvODk3MzIy?hl=ru&gl=RU&ceid=RU%3Aru

# https://news.google.com/articles/
# CBMiSmh0dHBzOi8vd3d3Lm55dGltZXMuY29tL2xpdmUvMjAyMy8wNC8yMy93b3JsZC9zdWRhbi1raGFydG91bS1maWdodGluZy1uZXdz0gEA?hl=en-US&gl=US&ceid=US%3Aen

# for : https://news.google.com/articles/ + news_links[]