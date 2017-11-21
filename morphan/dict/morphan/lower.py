import sys

lin = sys.stdin.readline()
while (lin):
    if len(lin) >= 2:
        print(lin.lower().strip())
    lin = sys.stdin.readline()
