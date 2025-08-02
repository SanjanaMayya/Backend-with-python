from flask import Flask 
app = Flask(__name__)

@app.route("/<int:number>")
def primefunc(number):
    primes = ""
    for i in range(2,number+1):
        for n in range(2,i):
            if(i % n == 0):
                break
        else:
            primes = primes + str(i) + ","
    
    return primes

if __name__ == "_main__":

    app.run(debug=True)
