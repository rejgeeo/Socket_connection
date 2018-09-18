Use this Client Server Socket program to test connections.

The client program creates a single socket with server and sends a simple hello protocol.

Server uses a single thread to accept and listen to socket connections and responds to hello protocol.

Connection is closed by Server once the handshake is completed.

Client reconnects and repeats the procedure for n times

Code fully written in Python.
Server hosted in a Digital Ocean droplet instance