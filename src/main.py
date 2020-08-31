import requests
import shutil

GURU_SHOTS_PREFIX = 'https://photos.gurushots.com/unsafe/0x0/05797d3a3394fa193a4986b0f86e87df/3_'
GURU_SHOTS_SUFFIX = '.jpg'


def guru_download_photos(path):
    urls = []
    ids = get_guru_photos_ids()

    for item in ids:
        url = GURU_SHOTS_PREFIX + item + GURU_SHOTS_SUFFIX
        response = requests.get(url, stream=True)
        response.raw.decode_content = True
        with open(f'{path}/{item}{GURU_SHOTS_SUFFIX}', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    return urls


def get_guru_photos_ids():
    ids = []

    url = "https://gurushots.com/rest/get_photos_public"

    payload = "limit=8011&member_id=05797d3a3394fa193a4986b0f86e87df&sort=desc&start=0&type=photos"
    headers = {
        'cookie': "_tmid=5f4d3d0d2e2e5",
        'x-api-version': "8",
        'x-env': "WEB",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/plain, */*",
        'x-requested-with': "XMLHttpRequest"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    for item in response.json()['items']:
        ids.append(item['id'])

    return ids


guru_download_photos('/home/matishadow/tmp/photos')
