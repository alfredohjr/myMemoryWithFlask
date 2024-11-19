import requests
import random

def run(method):

    val = random.randint(0, 5)

    if method.upper() == 'GET':

        fake_id = random.randint(0, 50)

        response = requests.get(f'http://127.0.0.1:5000/numero{val}/fifo')
        print(val, response.json())
    elif method.upper() == 'POST':
        print(f'POST {val}')
        response = requests.post(
            f'http://127.0.0.1:5000/numero{val}', 
            json={'name': 'teste'}
        )

if __name__ == '__main__':
    run('get')
    for _ in range(10000):
        choice = random.choice(['post', 'get'])
        run(choice)
    run('get')
