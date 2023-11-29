#1
import json

import math
from flask import Flask, request, Response

# returns True/False whether the given argument is prime
def primality_test(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True

#print(primality_test(int(input("Give a number ? "))))


app = Flask(__name__)


@app.route('/prime_number/<numberstring>')
def calculate_prime(numberstring):
    try:
        number = int(numberstring)
        response = {
            "Number" : number,
            "isPrime" : primality_test(number)
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

@app.route('/prime_number')
def error_stub():
    try:
        number = 666
        response = {
            "Message" : "Prime beast!",
            "Number" : number,
            "isPrime" : primality_test(number)
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response



@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#2
from flask import Flask
import mysql.connector

app = Flask(__name__)

db_connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='pass_word'
)

def get_airport_info_from_db(icao_code):
    cursor = db_connection.cursor()
    sql = "SELECT ident, name, iso_country FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport_info = get_airport_info_from_db(icao_code.upper())

    if airport_info:
        response = {
            "ICAO": airport_info[0],
            "Name": airport_info[1],
            "Location": airport_info[2],
        }
        return f'{{"ICAO":"{response["ICAO"]}", "Name":"{response["Name"]}", "Location":"{response["Location"]}"}}'
    else:
        return '{"error": "Airport not found"}', 404

if __name__ == '__main__':
    app.run(debug=True)
