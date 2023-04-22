import requests

import set


def print_hi(name, age):
    # Use a breakpoint in the code line below to debug your script.
    if age < 18:
        print(f'Hi, baby {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    else:
        print(f'Hi, man {name}')


def post_request():
    url = 'https://reqres.in/api/users/2'

    data = {'username': 'john_doe', 'password': 'password123'}

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('User created successfully')
    else:
        print('Failed to create user')


def get_request():
    url = 'https://reqres.in/api/users/2'

    response = requests.get(url)

    if response.status_code == 200:
        print('User created successfully')
    else:
        print('Failed to create user')


def set_request():
    url = 'https://smarty.mail.ru/api/v1/persons/set'
    oauth_token = '2tbQtCJ6H9g4fjU4eH5jkrZRrw2qmfHVNCGYopbGSmTYoKJpPu'
    oauth_provider = 'mcs'

    headers = {'accept': 'application/json'}

    # files = {"file": open("C:\\Users\\Maximgo\\OneDrive\\Desktop\\wallpapers\\ded1.jpg", "rb")}
    files = [
        ('file', ('ded1.jpg', open('C:\\Users\\Maximgo\\OneDrive\\Desktop\\wallpapers\\ded1.jpg', 'rb'), 'image/jpeg'))
    ]

    meta1 = {"space": "1", "images": [{"name": "file", "person_id": 1}]}

    data = {"meta": str(meta1)}

    response = requests.post(url, headers=headers, data=data, files=files,
                             params={'oauth_token': oauth_token, 'oauth_provider': oauth_provider})

    print(response.json())



def recognize_request():
    url = "https://smarty.mail.ru/api/v1/persons/recognize?oauth_token=2tbQtCJ6H9g4fjU4eH5jkrZRrw2qmfHVNCGYopbGSmTYoKJpPu&oauth_provider=mcs"

    payload = {'meta': '{"space": "1", "create_new": false, "images": [{"name": "file", "person_id": 1}]}'}
    files = [
        ('file', ('kish.jpeg', open('C:\\Users\\Maximgo\\OneDrive\\Desktop\\egor\\kish.jpeg', 'rb'), 'image/jpeg'))
    ]
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.json())


if __name__ == '__main__':
    set.set_postman()
    recognize_request()

