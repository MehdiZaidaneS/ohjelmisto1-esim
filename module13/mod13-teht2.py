import json

import mysql.connector
from flask import Flask, Response

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="mehdizaidane1",
    database="flight_game",
    autocommit= True
)

app = Flask(__name__)

@app.route('/kentta/<ICAO>')
def kentta(ICAO):
    try:
        ICAO = ICAO
        cursor = connection.cursor()
        sql = f"SELECT name, municipality FROM airport WHERE ident= '{ICAO}'"
        cursor.execute(sql)

        name = cursor.fetchone()

        response = {
            "ICAO": ICAO,
            "Name": name[0],
            "Municipality": name[1]
        }

        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }

        json_response = json.dumps(response)
        http_response = Response(json_response, status=400, mimetype='application/json')
        return http_response



@app.errorhandler(404)
def page_not_found(error):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(json_response, status=404, mimetype='application/json')
    return http_response



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)




