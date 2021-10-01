"""
SecureMessaging.py

NAMES: Mia McDuffie, Andrew Xie

Run as client: python3 SecureMessaging.py [Server IP] [Server Port]
Run as server: python3 SecureMessaging.py [Server Port]

"""

import sys
import socket
import os
from threading import Thread

import pyDH

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

QUEUE_LENGTH = 1
SEND_BUFFER_SIZE = 2048



class SecureMessage:

    IS_SERVER = False
    IS_CLIENT = False
    shared_key = 0
    shared_key_2 = 0

    def __init__(self, server_ip=None, server_port=None):
        """Initialize SecureMessage object, create & connect socket,
           do key exchange, and start send & receive loops"""

        # create IPv4 TCP socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect as client
        if server_ip and server_port:
            self.s.connect((server_ip, server_port))
            self.IS_CLIENT = True

        # connect as server
        elif server_port and not server_ip:
            self.s.bind(('', server_port))
            self.s.listen(QUEUE_LENGTH)
            self.s, _ = self.s.accept()
            self.IS_SERVER = True

        # Run Diffie-Hellman key exchange
        self.key_exchange()

        # start send and receive loops
        self.recv_thread = Thread(target=self.recv_loop, args=())
        self.recv_thread.start()
        self.send_loop()

    def send_loop(self):
        """Loop to check for user input and send messages"""
        while True:
            try:
                user_input = input().encode("ISO-8859-1")
                sys.stdout.flush()
                message = self.process_user_input(user_input)
                self.s.send(message[:SEND_BUFFER_SIZE])
            except EOFError:
                self.s.shutdown(socket.SHUT_RDWR)
                os._exit(0)

    def recv_loop(self):
        """Loop to receive and print messages"""
        while True:
            recv_msg = self.s.recv(SEND_BUFFER_SIZE).decode("ISO-8859-1")
            if recv_msg:
                message = self.process_received_message(recv_msg)
                sys.stdout.write("\t" + message + "\n")
                sys.stdout.flush()
            else:
                os._exit(0)

    def key_exchange(self):
        """TODO: Diffie-Hellman key exchange"""

        client_to_server = pyDH.DiffieHellman() #random number
        server_to_client = pyDH.DiffieHellman()

        cs_pubkey = client_to_server.gen_public_key() #gen a public key
        sc_pubkey = server_to_client.gen_public_key()
        

        self.s.send((str(cs_pubkey)).encode("ISO-8859-1")[:SEND_BUFFER_SIZE]) # takes strings and turns it to bytes 
        their_public  = int(self.s.recv(SEND_BUFFER_SIZE).decode("ISO-8859-1")) #telling how much to receive #takes bytes and turns it to strings
        self.shared_key = client_to_server.gen_shared_key(their_public) #[:32]
        
        
        self.s.send((str(sc_pubkey)).encode("ISO-8859-1")[:SEND_BUFFER_SIZE])
        their_public_2 = int(self.s.recv(SEND_BUFFER_SIZE).decode("ISO-8859-1"))
        self.shared_key_2 = server_to_client.gen_shared_key(their_public_2) #[:32] #take the first 32 bytes or 16

        #print(self.shared_key)

        #At secret key stage - Any more steps?

        
    
    #msg + split + nonce + split + tag

    def process_user_input(self, user_input):
        """TODO: Add authentication and encryption"""
        if (self.IS_SERVER == True):
            key = self.shared_key_2.encode("ISO-8859-1")
            key = key[0:16]
            cipher = AES.new(key, AES.MODE_EAX) 

        elif (self.IS_CLIENT == True):
            key = self.shared_key.encode("ISO-8859-1")
            key = key[0:16]
            cipher = AES.new(key, AES.MODE_EAX) #potentially shorten key to 16 or 32
   
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(user_input)
        recv_msg = ciphertext + " ".encode("ISO-8859-1") + nonce + " ".encode("ISO-8859-1") + tag #send this message

        return recv_msg #its in bytes

    def process_received_message(self, recv_msg):
        # """TODO: Check message integrity and decrypt"""

        # #Check message integrity (Should HMAC be used here and how?)

        # #unjumble recv_msg 
        marker1 = -1
        marker2 = -1

        for x in range(len(recv_msg)):
            if (recv_msg[x] == " "):
                if (marker1 != -1):
                    marker2 = x
                else:
                    marker1 = x
        
        nonce = recv_msg[marker1+1: marker2]
        nonce = nonce.encode("ISO-8859-1")
        # # #Decryption
        
        if (self.IS_SERVER == True):
            key = self.shared_key.encode("ISO-8859-1") #turn into bites
            key = key[0:16] #first 16 bytes
            cipher = AES.new(key, AES.MODE_EAX, nonce)
        elif (self.IS_CLIENT == True):
            key = self.shared_key_2.encode("ISO-8859-1")
            key = key[0:16]
            cipher = AES.new(key, AES.MODE_EAX, nonce)
        plaintext = cipher.decrypt(recv_msg[0: marker1].encode("ISO-8859-1"))  # recv_msg?
        

        return plaintext.decode("ISO-8859-1") #Is this correct return value?


def main():
    """Parse command-line arguments and start client/server"""

    # too few arguments
    if len(sys.argv) < 2:
        sys.exit(
            "Usage: python3 SecureMessaging.py [Server IP (for client only)] [Server Port]")

    # arguments for server
    elif len(sys.argv) == 2:
        server_ip = None
        server_port = int(sys.argv[1])

    # arguments for client
    else:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])

    # create SecureMessage object
    secure_message = SecureMessage(
        server_ip=server_ip, server_port=server_port)


if __name__ == "__main__":
    main()

