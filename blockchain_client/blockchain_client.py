from flask import Flask, render_template
from argparse import ArgumentParser


class Transaction:
    def __init__(self, sender_public_key, sender_private_key, recipient_public_key, amount):
        self.sender_public_key = sender_public_key
        self.sender_private_key = sender_private_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount



#initiating the node
app = Flask(__name__)

@app.route("/") # adds the root page/home page route to flask
# everything under the route belongs to the route until new route is added
def index():
    # returns the rendered page
    return render_template("./index.html")

@app.route("/home")

def Home():
    return index()
@app.route("/make/transactions")

def MakeTransactions():
    return render_template("./make_transactions.html")

@app.route("/view/transactions")

def ViewTransactions():
    return render_template("./ViewTransactions.html")

@app.route("/wallet/new")

def new_wallet():
    return ""

if __name__ == '__main__':

   parser = ArgumentParser()
   ''' adss an argument using parser "-p" specifies the port then sets 
   the default port to 5001 if other wise was not specified and sets the port type to integer'''
   parser.add_argument('-p','--port',default = 8000, type = int, help = "port")
   args = parser.parse_args() # parses the arguments
   port = args.port # specifies a port ??
   app.run(host = "127.0.0.1", port=port, debug = True) #runs the flask app in debug mode