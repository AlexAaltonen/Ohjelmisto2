# (jaollinen 4 ja ei 100)          jaollinen 400 sadalla

from flask import Flask, request
import math

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    if luku < 2:
        isPrime = False
    else: 
        isPrime = True
    for i in range(2, int(math.sqrt(luku)) + 1):
        if luku % i == 0:
            isPrime = False
    
    vastaus = {
        "Number": luku,
        "isPrime": isPrime
    }
    return vastaus
   
app.run(use_reloader=True, host='127.0.0.1', port=3000)   
