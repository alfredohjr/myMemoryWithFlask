from flask import Flask, request

DB = {}

app = Flask(__name__)

@app.route('/<string:database>', methods=['GET','POST'])
def hello_world(database):

    if request.method == 'GET':
        if database in DB:
            return DB[database]['data']
        return []
    
    elif request.method == 'POST':
        data = request.json
        data['id'] = DB[database]['count'] if database in DB else 1

        if database in DB:
            DB[database]['data'].append(data)
        else:
            DB[database] = {'data': [data]}

        DB[database]['count'] = data['id'] + 1

        return {'message': 'success'}

@app.route('/<string:database>/<int:id>', methods=['GET','PUT','DELETE'])
def hello_world_id(database, id):

    if database not in DB:
        return {'message': 'not found'}

    if request.method == 'GET':
        for data in DB[database]['data']:
            if data['id'] == id:
                return data
        return []
    
    elif request.method == 'PUT':
        data = request.json

        for i, d in enumerate(DB[database]['data']):
            if d['id'] == id:
                data['id'] = id
                DB[database]['data'][i] = data
                return {'message': 'success'} 
        return {'message': 'not found'}
    
    elif request.method == 'DELETE':
        for i, data in enumerate(DB[database]['data']):
            if data['id'] == id:
                DB[database]['data'].pop(i)
                return {'message': 'success'}
        return {'message': 'not found'}

@app.route('/<string:database>/fifo', methods=['GET'])
def hello_world_fifo(database):

    if database not in DB:
        return {'message': 'not found'}

    if request.method == 'GET':
        if DB[database]['data']:
            return DB[database]['data'].pop(0)
        return []

if __name__ == '__main__':
    app.run()