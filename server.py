from flask import Flask, request

DB = {}

app = Flask(__name__)

@app.route('/<database>', methods=['GET','POST'])
def hello_world(database):

    if request.method == 'GET':
        if database in DB:
            return DB[database]['data']
        return []
    
    elif request.method == 'POST':
        data = request.json
        if database in DB:
            data['id'] = DB[database]['count']
            DB[database]['data'].append(data)
            DB[database]['count'] += 1
        else:
            DB[database] = {'data': [data], 'count': 1}
            DB[database]['count'] += 1
        return {'message': 'success'}


if __name__ == '__main__':
    app.run()