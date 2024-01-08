import socket
import sys

def create_socket():
    try:
        global host
        global port 
        global s #socket
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation fail, error: " + str(msg))

#Binding socket & listening for connections
def bind_socket():
    try:
        global host
        global port 
        global s #socket
        
        print("Binding Port: " + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Binding Socket fail, error: " + str(msg)+ "Trying again")
        bind_socket()

#Establishing connection       
def socket_accept():
    conn, address = s.accept()
    print("Connection established, " + "IP " + address[0] + " Port "+ str(address[1]))
    send_command(conn)
    conn.close()

#Sending command to client
def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit" :
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

