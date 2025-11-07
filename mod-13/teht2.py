#tee funktio, joka hakee sql lauseella icao-koodilla lentokentän ja tulostaa halutut asiat
import mysql.connector
from flask import Flask, request


conn = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='PekkaonTyhmä09',
         autocommit=True
         )




app = Flask(__name__)
@app.route('/kenttä/<ident>')
def kenttä(ident):
    cursor = conn.cursor(dictionary=True)
    sql = "Select ident as icao, name, municipality from airport where ident  = %s"
    cursor.execute(sql, (ident,))
    vastaus = cursor.fetchall()
    
    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)   