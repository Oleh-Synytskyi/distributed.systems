# Lab_6(Seminar 05) Rest Web Service

# Used:

- Java 8
- Maven

# Run Server and Client

1. Run server is next arguments:

    mvn clean compile exec:java -D exec.args="localhost 8080"

2.  Run client used arguments

    mvn clean compile exec:java -D exec.args="http://localhost:8080"
 
3.  arguments may be yours, but you need to enter the url of the rest server location according to address which the server is running;

# Used Commands

- login - Log in on server or create new user (login user_login user_password)

- echo - Testing sending message. Enter the command and message for echo (echo message for testing)

- ping - Testing connection (no parameters)

- msg - Send message to user.
(msg to_user text message for another user)

- exit - Shutdown the client (no parameters);
