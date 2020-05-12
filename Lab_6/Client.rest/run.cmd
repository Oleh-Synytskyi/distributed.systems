@echo off
:start
cmd /C mvn clean package exec:java -Dexec.args="http://localhost:8800"
goto start