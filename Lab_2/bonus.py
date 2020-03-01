import os
import sys
while True:
    command = input('Input command: ')
    if command == 'exit':
        sys.exit(0)
    parameter = input("Input parameters: ")
    if command == 'ping':
        os.system('ping'+' '+ parameter)
    if command == 'echo':
        os.system('echo'+' '+ parameter)
    if command == 'dir':
        os.system('dir'+' '+ parameter)
    if command == 'exit':
        os.system('exit'+' '+ parameter)
