import requests
from getpass import getpass

def get_dates():
    global headers
    BASE_URL = 'https://olimp.miet.ru/ppo_it_final/date'
    headers = {'X-Auth-Token': 'ppo_8_11126'}
    response = requests.get(f"{BASE_URL}", headers=headers)
    dates = response.json()['message']
    return dates

def get_data_dates():
    global headers
    ndates = []
    dates = get_dates()
    for i in dates:
        ndates.append([i[:2], i[3:5], i[6:]])
        
    gdata = []

    for i in ndates:
        data = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={i[0]}&month={i[1]}&year={i[2]}', headers=headers)
        gdata.append([i, data.json()])

    return gdata

def check_data(data):
    headers = {'X-Auth-Token': 'ppo_8_11126'}
    d = requests.post(f'https://olimp.miet.ru/ppo_it_final', headers=headers, data=data)
    return d
