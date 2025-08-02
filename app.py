from flask import Flask 
app = Flask(__name__)

@app.route("/<int:number>")
def prime(number):
    primes = ""
    for i in range(1,number+1):
       primes = primes + str(i) + "," 
    return primes

if __name__ == "__main__":
    app.run()