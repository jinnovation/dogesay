#!/usr/bin/python

from argparse import ArgumentParser
from random   import randrange

DOGE_PREFIXES = ["such", "much", "so", "many", "wow"]
DOGE_EJACULATES = ["wow"]

DOGE_FACE_FILE = open("static/doge.txt","r")

WOW_CHANCE = 7

def num_words(clause):
    numwords = 0
    for word in clause.split():
        numwords += 1
    return numwords

def doge_syntax(clause):
    if num_words(clause) > 1:
        return clause
    else:
        return DOGE_PREFIXES[randrange(0,len(DOGE_PREFIXES))]+" "+clause

    
if __name__ == "__main__":
    parser = ArgumentParser(description="Cowsay for a new generation.")
    parser.add_argument("inputfile", metavar="<input file>")

    clausefile = open(parser.parse_args().inputfile, "r")

    for clause in clausefile:
        clause = clause.strip()
        move_next_iter = False

        while not move_next_iter:
            if randrange(0,10) > WOW_CHANCE:
                # TODO: work with "wow" as the clause
                print(DOGE_EJACULATES[randrange(0,len(DOGE_EJACULATES))])
            move_next_iter = True

        # TODO: work with clause as the clause
        clause = doge_syntax(clause)
        print(clause)

    for line in DOGE_FACE_FILE:
        print(line.rstrip())
