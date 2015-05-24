import socket
import sys


class client:
  def __init__(self, host):
    #costruisco il sockt del client
    self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    self.sock.connect((host, 4000))


prova=client("alessia-Aspire-5536")
