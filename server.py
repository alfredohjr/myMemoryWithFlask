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



if __name__ == '__main__':
    app.run()