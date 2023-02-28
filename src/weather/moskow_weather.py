import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Обозначения метеопараметров см. по адресу http://rp5.ru/archive.php?wmo_id=27612&lang=ru
filename = '../data/moskow.01.01.2023.31.01.2023.1.csv'

with open(filename, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    headers = None
    # Чтение дат и температур из файла.
    dates, highs = [], []

    for row in reader:
        # Пропустить строки, которые начинаются с символа #
        if row and not row[0].startswith('#'):
            # Определяем заголовки
            if not headers:
                headers = row
                continue

            current_date = datetime.strptime(row[0], "%d.%m.%Y %H:%M")
            high = float(row[1])
            dates.append(current_date)
            highs.append(high)

    # print(headers)

    # Нанесение данных на диаграмму.
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Форматирование диаграммы.
    plt.title('Температура воздуха в Москве', fontsize=16)
    plt.xlabel('Температура воздуха', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('Градусы Цельсия', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.grid(True)
    plt.show()
