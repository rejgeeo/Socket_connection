import socket
import sys
import time

global s

execStartTime = time.time()
execStartTimeClock = time.asctime()
print("Starting execution @ " + str(execStartTimeClock))
failedConnections = 0

for count in range(1,1000):
    starttime = time.asctime()
    starttimeCPU = time.time()
    print("Opening conection " + str(count) + " times @ " + str(starttime))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" %(err))

    host_ip = '159.89.172.14'   # DigitalOcean Droplet instance
    # host_ip = '10.15.1.129'
    # host_ip = '192.168.43.70'

    port = 9999
    try:
        print("Connecting to Server")
        s.connect((host_ip, port))
    except socket.error as err:
        print("Connection to server failed with error %s" %(err))
        failedConnections += 1
        continue
    cmd = 'hi'
    s.send(str.encode(cmd))
    while True:
    # connecting to the server
        data= str(s.recv(1024))
        if 'hello' in data:
            s.send(str.encode('quit'))
        elif 'invalid' in data:
            print("invalid cmd", end="")
            cmd = input()
            s.send(str.encode(cmd))
            continue
        else:
            stoptime = time.asctime()
            stoptimeCPU = time.time()
            connectiontime = stoptimeCPU - starttimeCPU
            print("closing connection " + str(count) + " " + str(stoptime))
            print("Connection duration was : {:.4f} sec".format(connectiontime))
            s.close()
            break

execStopTime = time.time()
execStopTimeClock = time.asctime()
execTime = execStopTime - execStartTime
# execTimeMin, execTimeSec = divmod(execTime,60)
execTimeMin, execTimeSec = divmod(execTime,60)
execTimeMin = int(execTimeMin)
execTimeHour, garbage = divmod(execTimeMin,60)
execTimeHour = int(execTimeHour)
execTimeMs = int((execTimeSec - int(execTimeSec)) * 10000)
execTimeSec = int(execTimeSec)
print("Execution time for executing {:d} loops is: {:d}:{:d}:{:d}.{:d} mins, and {:d} times socket connection failed".format(count,execTimeHour,execTimeMin,execTimeSec,execTimeMs,failedConnections))
