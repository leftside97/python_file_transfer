#!/bin/python

import socket, sys

class tcp_socket():
    def listen_on(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.s.bind((self.host, int(port)))
        self.s.listen(5)
        self.s, self.addr = self.s.accept()

    def connect_to(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, int(port)))

    def recive_all(self):
        data=b''
        while True:
            recvfile = self.s.recv(4096)
            if not recvfile: break
            data += recvfile
        return data

    def recive_data(self):
        return self.s.recv(1024)

    def send_all(self, data):
        self.s.sendall(data)

    def close(self):
        self.s.close()
        
        
def readfile(datei):
  data = open(datei, "rb").read()
  return data

def writefile(data, filename):
  with open(filename, "wb") as f:
    f.write(data)

if __name__ == "__main__":
  x = tcp_socket()
  try:
    if sys.argv[1] == "-s":
      x.connect_to(sys.argv[3], sys.argv[4])
      x.send_all(readfile( sys.argv[2]))
      x.close()

    if sys.argv[1] == "-r":
      x.listen_on(sys.argv[3])
      writefile(x.recive_all(), sys.argv[2])
      x.close()
  except:
    print("send file  :", sys.argv[0], "-s [file] [ip] [port]")
    print("recive file:", sys.argv[0], "-r [file] [port]")
    sys.exit()


