import requests
import random

def run(method):

    val = random.randint(0, 5)

    if method.upper() == 'GET':
        response = requests.get(f'http://127.0.0.1:5000/numero{val}')
        print(response.json())
    elif method.upper() == 'POST':


        response = requests.post(
            f'http://127.0.0.1:5000/numero{val}', 
            json={'name': 'teste'}
        )

if __name__ == '__main__':
    run('get')
    for _ in range(10000):
        run('post')
    run('get')
