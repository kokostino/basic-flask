from flask import Flask
from flask import jsonify
app = Flask(__name__)

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1,2,5,10,20,50.100,200] # value of coins in Eur cents
    coin_lookup = {200: "zwoa Euro", 100: "Oa Euro", 50: "Fuchztgerl", 20: "Zwanzgerl", 10: "Zehnerl", 5: "Fuenferl", 2: "Zwoa Cent", 1: "Oa Cent"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num:coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/change/<euro>/<cents>')
def changeroute(euro, cents):
    print(f"Make Change for {euro}.{cents}")
    amount = f"{euro}.{cents}"
    result = change(float(amount))
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)