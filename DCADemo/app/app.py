from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

def production() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'volve'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM production')
    row = cursor.fetchone()
    print(f'Row is {row}')
    rows=[]

    while row is not None:
        print(row)
        print("row")
        #rows.append(row)
        row = cursor.fetchone()
    cursor.close()
    connection.close()

    return "hello"


@app.route('/')
def index() -> str:
    #return json.dumps({'production': production()})
    return production()

if __name__ == '__main__':
    app.run(host='0.0.0.0')