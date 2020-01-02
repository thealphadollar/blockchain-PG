from collections import OrderedDict
import binascii

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

"""Transaction class that each user sends to the blockchain network."""

class Transaction:
    def __init__(self, sndr_pub_key, sndr_priv_key, rcvr_pub_key, amt):
        """
        Create a transaction.
        
        Arguments:
            sndr_pub_key {[str]}
            sndr_priv_key {[str]}
            rcvr_pub_key {[str]}
            amt {[int]}
        """
        self.sndr_pub_key = sndr_priv_key
        self.sndr_priv_key = sndr_priv_key
        self.rcvr_pub_key = rcvr_pub_key
        self.amt = amt
    
    def __getattribute__(self, name):
        return self.data[name]

    def toDict(self):
        return OrderedDict({'sndr_pub_key' : self.sndr_pub_key,
                            'rcvr_pub_key': self.rcvr_pub_key,
                            'amt': self.amt})

    def sign_trans(self):
        """
        Sign the transaction using sender's private key.
        """
        priv_key = RSA.importKey(binascii.unhexlify(self.sndr_priv_key))
        signer = PKCS1_v1_5.new(priv_key)
        hsh = SHA.new(str(self.toDict()).encode())
        return binascii.hexlify(signer.sign(hsh).decode())

        