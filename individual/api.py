'''
    api.py
    Soren Kaster
    4/20/2025

'''

import csv
import flask
import json
import argparse

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hey, is this thing on? Try /help to see more...'

@app.route('/help')
def help():
    return flask.render_template('help.html')

@app.route('/<athletename>/<height>')
def get_count(athletename, height):
    count = 0
    list = []
    if '-' in athletename:
        parts = athletename.split('-')
        formated_name = f'{parts[1].capitalize()}, {parts[0].capitalize()}'
    with open('data/MIAC_data.csv') as f:
        reader = csv.reader(f)
        for performance_row in reader:
            if formated_name in performance_row[7]:
                if performance_row[8] == 'Pole Vault':
                    if height <= performance_row[10]:
                        list.append(f'{formated_name} jumped {performance_row[10]} on {performance_row[2]}')
                        count += 1

    list.insert(0,f'{formated_name} cleared over {height} meters {count} times!')
    return json.dumps(list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Flask API implementation, enter a specificed host and port, otherwise use the default localhost 9999.')
    parser.add_argument('--host', default='localhost', help='the host on which this application is running. Default = localhost')
    parser.add_argument('--port', type=int, default=9999, help='the port on which this application is listening. Default = 9999')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
