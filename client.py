import socket
import sys


class client:
  def __init__(self, host):
    #costruisco il sockt del client
    self.esci=False
    self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    self.sock.connect((host, 5003))
    #data=self.sock.recv(1024)
    #print data
    while not self.esci:
      data=raw_input("Manda al server:")
      if data != 'quit':
        self.sock.sendall(data)
      else :
        self.esci=True
        self.sock.sendall('connessione interrotta')
    self.sock.close()

prova=client("alessia-Aspire-5536")
