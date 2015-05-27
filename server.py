import socket
import sys


class server:
  #costruttore
  def __init__(self, porta):
    # crea un socket INET di tipo STREAM
    self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.uscito=False
    # associa il socket a un host pubblico
    self.serversocket.bind((socket.gethostname(), porta))
    print porta, socket.gethostname()
    # diventa un socket server
    self.serversocket.listen(5)
    # accetta le connessioni dall'esterno
    (socketclient, address) = self.serversocket.accept()
    
    # ora fa qualcosa con il socket client
    print socketclient, address
    #socketclient.send('Write something')
    while 1:
      data= socketclient.recv(1024)
      if not data:
        break
      else:
        print data
       
        
        
    self.serversocket.close()
      
#server

#avvio il server sulla porta 4000
prova=server(5003)

