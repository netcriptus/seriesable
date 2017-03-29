import requests

from seriesable.celery import app
from tv_shows.models import TvShow


@app.task(name='collect_shows')
def collect_shows:
    base_url = 'http://api.tvmaze.com/shows'
    page = 1

    response = requests.get(base_url, params={'page': page})
    while response.status_code == 200:
        shows_list = response.json()
        for show in shows_list:
            TvShow.objects.get_or_create(name=show['name'],
                                         summary=show['summary'],
                                         tv_rage_id=show['id'],
                                         genres=show['genres'],
                                         show_type=show['type'],
                                         premiered=show['premiered'],
                                         image=show.get('image', {}).get('original'),
                                         language=show['language'],
                                         networks=show['network'],
                                         tv_rage_rating=show['rating'].get('average', 0),
                                         runtime=show['runtime'],
                                         schedule=show['schedule'],
                                         status=show['status'])
        page += 1
        response = requests.get(base_url, params={'page': page})
