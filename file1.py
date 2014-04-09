#!/usr/bin/python

import sys

def Cat1(filename):
    f = open(filename, 'rU')
    lines = f.readlines() # converts file to list of lines
    print lines
    f.close()

def Cat2(filename):
    f = open(filename, 'rU')
    text = f.read() # reads entire file in one string
    print text,
    f.close()


def Cat(filename):
    f = open(filename, 'rU')
    for line in f:
        print line,
    f.close()    
    
def main():
#    Cat(sys.argv[1])
#    Cat1(sys.argv[1])
    Cat2(sys.argv[1])
        
if __name__ == '__main__':
    main() 