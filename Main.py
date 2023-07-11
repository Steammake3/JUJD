from Inter import *

def main():
    file = open("hello.jujd")
    readable = file.read().splitlines()
    interpret(readable)
    file.close()

main()