from pathlib import Path
import logging

import requests
import shutil
import instaloader

GURU_SHOTS_PREFIX = 'https://photos.gurushots.com/unsafe/0x0/05797d3a3394fa193a4986b0f86e87df/3_'
GURU_SHOTS_SUFFIX = '.jpg'
INSTA_ACCOUNT_NAME = 'hubble_bubble_photo'


def get_instagram_photos(path):
    logging.info('downloading photos from instagram')
    loader = instaloader.Instaloader(post_metadata_txt_pattern='', download_comments=False, save_metadata=False)

    profile = instaloader.Profile.from_username(loader.context, INSTA_ACCOUNT_NAME)
    posts = profile.get_posts()

    for post in posts:
        loader.download_post(post, target=Path(path))


def get_guru_photos(path):
    logging.info('downloading photos from guru')
    urls = []
    ids = get_guru_photos_ids()

    for item in ids:
        url = GURU_SHOTS_PREFIX + item + GURU_SHOTS_SUFFIX
        response = requests.get(url, stream=True)
        response.raw.decode_content = True
        with open(f'{path}/guru.{item}{GURU_SHOTS_SUFFIX}', 'wb') as out_file:
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


def get_reddit_photos(path):
    logging.info('downloading photos from reddit')
    url = "https://www.reddit.com/user/hubblepen.json"

    response = requests.request("GET", url, data="", headers={'User-agent': 'your bot 0.1'})

    for child in response.json()['data']['children']:
        data = child['data']

        if 'url' not in data:
            continue

        url = data['url']
        if url.endswith(GURU_SHOTS_SUFFIX):
            response = requests.get(url, stream=True)
            response.raw.decode_content = True
            file_name = 'reddit.' + url.split('/')[-1]
            with open(f'{path}/{file_name}', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response


def get_all_photos(path):
    get_guru_photos(path)
    get_reddit_photos(path)
    get_instagram_photos(path)


get_all_photos('/home/pi/Pictures')
