from flask import Flask 
app = Flask(__name__)

@app.route("/<int:number>")
def even_func(number):
    primes = ""
    for i in range(1,number+1):
        if(i % 2 == 0):
            primes = primes + str(i) + ","
    return primes

if __name__ == "_main__":
    app.run(debug=True)