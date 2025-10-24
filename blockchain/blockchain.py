from flask import Flask, render_template,jsonify
from argparse import ArgumentParser
from datetime import time
from flask_cors import CORS

class Blockchain:
    def __init__(self):
        #initiating the class
        self.transactions = []
        self.chain = []
        self.create_block(0,'0000'
                          )
    def create_block(self, nonce, previous_hash):
        block = {
            'blocknumber': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.transactions,
            'nonce': nonce,
            'previous_hash':previous_hash
        }
        # reset block transactions
        self.transactions = []
        self.chain.append(block)
        return block

Blockchain = Blockchain()

#initiating the node
app = Flask(__name__)
CORS(app)

@app.route("/") # adds the root page/home page route to flask
# everything under the route belongs to the route until new route is added
def index():
    # returns the rendered page
    return render_template("./index.html")

@app.route("/home")

def Home():
    return index()

@app.route("/generate/transactions", methods=["POST"])

def generate_transaction():
    response = {"massage":"ok"}
    return jsonify(response),201

if __name__ == '__main__':

   parser = ArgumentParser()
   ''' adss an argument using parser "-p" specifies the port then sets 
   the default port to 5001 if other wise was not specified and sets the port type to integer'''
   parser.add_argument('-p','--port',default = 5001, type = int, help = "port")
   args = parser.parse_args() # parses the arguments
   port = args.port # specifies a port ??
   app.run(host = "127.0.0.1", port=port, debug = True) #runs the flask app in debug mode