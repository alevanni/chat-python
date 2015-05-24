import socket
import sys


class server:
  #costruttore
  def __init__(self, porta):
    # crea un socket INET di tipo STREAM
    self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # associa il socket a un host pubblico
    self.serversocket.bind((socket.gethostname(), porta))
    print porta, socket.gethostname()
    # diventa un socket server
    self.serversocket.listen(5)
    while 1:
      # accetta le connessioni dall'esterno
      (socketclient, address) = self.serversocket.accept()
      # ora fa qualcosa con il socket client
      print socketclient, address
    #while  
    self.serversocket.close()
  #avviaserver
#server

#avvio il server sulla porta 4000
prova=server(4000)

