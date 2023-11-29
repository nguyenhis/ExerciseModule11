from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
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
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
