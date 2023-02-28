import json

from plotly import offline
from plotly.graph_objs import Layout


# Изучение структуры данных.
filename = '../data/significant_month.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']

    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        title = eq_dict['properties']['title']
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)

    # Нанесение данных на карту.
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [5 * mag for mag in mags],
            'color': mags,
            'colorscale': 'Reds',
            'colorbar': {'title': 'Магнитуда'},
        },
    }]
    my_layout = Layout(title='Глобальные землетрясения',
                       geo=dict(
                           projection_type='natural earth',
                           showcoastlines=True,
                           showcountries=True,
                           countrycolor='grey'
                       ))

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')
