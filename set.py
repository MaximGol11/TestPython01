import requests


def set_postman():
    url = "https://smarty.mail.ru/api/v1/persons/set?oauth_token=2tbQtCJ6H9g4fjU4eH5jkrZRrw2qmfHVNCGYopbGSmTYoKJpPu&oauth_provider=mcs"

    payload = {'meta': '{"space": "1", "images": [{"name": "file", "person_id": 2}]}'}

    files = [('file', ('ded1.jpg', open('C:\\Users\\Maximgo\\OneDrive\\Desktop\\egor\\gorshok_solo.jpg', 'rb'), 'image/jpeg'))]

    headers = {
        'accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.json())