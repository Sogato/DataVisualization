import requests

from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Сохранение ответа API в переменной.
resource_dict = r.json()
repo_dicts = resource_dict['items']
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"Автор: {owner}<br />Описание: {description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Самые популярные проекты Python на GitHub',
    'titlefont': {'size': 24},
    'xaxis': {'title': 'Репозиторий',
              'titlefont': {'size': 20},
              'tickfont': {'size': 14},
              },
    'yaxis': {'title': 'Звёзды',
              'titlefont': {'size': 20},
              'tickfont': {'size': 14},
              },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
