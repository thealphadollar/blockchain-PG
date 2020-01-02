"""Flask app to manage interactions with the blockchain network."""

from transaction import Transaction

import json
import binascii

from flask import Flask, render_template, request
import Crypto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transaction/create')
def newTransaction():
    if request.method == 'POST':
        sender_pub = request.form['sender_address']
        sender_priv = request.form['sender_private_key']
        recv_pub = request.form['recipient_address']
        val = request.form['amount']
        
        trans = Transaction(sender_pub, sender_priv, recv_pub, val)
        return json.dumps({
            'transaction': Transaction.toDict(),
            'signature': Transaction.sign_trans()
        })

    else:
        return render_template('make_transaction.html')

@app.route('/transaction/list')
def listTransaction():
    return render_template('view_transaction.html')

@app.route('/wallet/create')
def newWallet():
    random_generator = Crypto.Random.new().read
    rsa_priv = Crypto.PublicKey.RSA.generate(1024, random_generator)
    public_key = rsa_priv.publickey()
    return json.dumps({
        'private_key': binascii.hexlify(rsa_priv.exportkey(format='DER')).decode(),
        'public_key': binascii.hexlify(public_key.exportkey(format='DER')).decode(),
    })