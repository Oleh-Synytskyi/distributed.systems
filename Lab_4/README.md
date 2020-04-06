# Lab_4(Seminar 3): Remote Method Invocation
In the lab work let's get acquainted and start the server and client, also check what commands work
# Using
- Java 13
- Maven 
# Run Server and Client

1) Run Server

In order to start the server we use this command

mvn package exec:java -Dexec.args="1000" specify port
run using start.cmd 

@echo off
:start
cmd /C mvn package exec:java -Dexec.args="1000"
goto start

![img1]()

2) Run Client
In order to start the server we use this command

mvn package exec:java -Dexec.args="127.0.0.1 1000" specify port and localhost
run using run.cmd 

![img2]()

# Using Commands

1) We enter a command in the client  help  and output the available commands

![img3]()

- ping  - test the ability of the source computer to reach a server;
- echo  - display line of text/string that are passed as an argument;
- login - establish a new session with the server;
- list  - list all users on the server;
- msg   - send a message to a specific user;
- file  - send a file to a specific user;
- exit  - close the client.

2) You must authorize a client to send messages and use commands

![img4]()

3) We launch the second client

![img5]()

4) to send messages we use the msg command "message"

![img6]()

5) Using the command exit

![img7]()
