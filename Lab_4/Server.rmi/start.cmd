@echo off
:start
cmd /C mvn package exec:java -Dexec.args="1000"
goto start