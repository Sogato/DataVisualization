from plotly import offline
from plotly.graph_objs import Bar, Layout

from dice import Dice


# Создание двух кубиков D6.
die_1 = Dice()
die_2 = Dice()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
mex_result = die_1.num_sides + die_2.num_sides + 1
for value in range(2, mex_result):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
x_values = list(range(2, mex_result))
data = [Bar(x=x_values, y=frequencies)]

layout_config = {'text': 'Результаты броска двух D6 кубиков 1000 раз',
                 'font': {'size': 24},
                 }
x_axis_config = {'title': {'text': 'Результат', 'font': {'size': 20}},
                 'tickfont': {'size': 16},
                 'dtick': 1
                 }
y_axis_config = {'title': {'text':'Частота выпадения', 'font': {'size': 20}},
                 'tickfont': {'size': 16},
                 }
my_layout = Layout(title=layout_config,
                   xaxis=x_axis_config,
                   yaxis=y_axis_config
                   )

title_font = {'size': 24}
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
