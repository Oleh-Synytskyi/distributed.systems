@echo off
:start
cmd /C mvn package exec:java -Dexec.args="127.0.0.1 1000"
goto start