import sqlite3
from multiprocessing import Pool

def process_profile(profile):
    # код для обработки профиля
    pass

if __name__ == '__main__':
    # устанавливаем соединение с базой данных
    conn = sqlite3.connect('Profile.db')
    cursor = conn.cursor()

    # получаем список профилей из базы данных
    cursor.execute("SELECT * FROM CookieProfile")
    profiles = cursor.fetchall()

    # запускаем обработку профилей в пуле процессов
    with Pool(processes=5) as pool: # ограничиваем число процессов пятью
        pool.map(process_profile, profiles)

    # закрываем соединение с базой данных
    cursor.close()
    conn.close()
