# Lab_7: (Seminar06.) Message Queues

# Used:

- Java 8
- Maven

# Run Server and Client

1) Run server as following:

    mvn clean compile exec:java -D exec.args="0.0.0.0 61616"

- arguments(args) can be yours (you need to enter the host and port), and you can omit them (the server will run with "localhost 616161" settings by default).

![1](https://github.com/Oleh-Synytskyi/distributed.systems/tree/master/Lab_7/Images/1.png)


2) Run client as following:

    mvn clean compile exec:java -D exec.args="localhost 61616"
- arguments may be yours, but you need to enter the host and port of the server according to which the server is running;

![2](https://github.com/Oleh-Synytskyi/distributed.systems/blob/master/Lab_7/Images/2.png)

# Used Commands

- help - Shows a list of commands
- echo Testing sending message. Enter the command and message for echo:
    echo message for testing
- login - Log in on server or create new user. Has 2 parameters (login, password)
- msg - Send message to user. Has 2 parameters (recipient login, message(string))
- file - Send file to user. Has 2 parameters (recipient login, path to file)
- exit - Shutdown the client (no parameters);
         
 ![3](https://github.com/Oleh-Synytskyi/distributed.systems/blob/master/Lab_7/Images/3.png)
 ![4](https://github.com/Oleh-Synytskyi/distributed.systems/blob/master/Lab_7/Images/4.png)
 ![5](https://github.com/Oleh-Synytskyi/distributed.systems/blob/master/Lab_7/Images/5.png)
