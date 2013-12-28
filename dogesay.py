#!/usr/bin/python

from argparse import ArgumentParser
from random   import randrange, choice

DOGE_PREFIXES = ["such", "much", "so", "many", "wow"]
DOGE_EJACULATES = ["wow"]

DOGE_FACE_FILE = open("static/doge.txt","r").read().splitlines()

WOW_CHANCE = 5

def num_words(clause):
    return len(clause.split())

def doge_syntax(clause):
    if num_words(clause) > 1:
        return clause
    else:
        return DOGE_PREFIXES[randrange(0,len(DOGE_PREFIXES))]+" "+clause

def insert(clause, img_file):
    img_file[randrange(0,len(img_file))] += (" " + clause)
    
if __name__ == "__main__":
    parser = ArgumentParser(description="Cowsay for a new generation.")
    parser.add_argument("inputfile", metavar="<input file>")
    parser.add_argument("-a", "--ascii", action="store_true", help="Use ASCII doge")

    clauses_file = open(parser.parse_args().inputfile, "r")

    for clause in clauses_file:
        clause = clause.strip()
        move_next_iter = False

        while not move_next_iter:
            if randrange(0,10) > WOW_CHANCE:
                insert(DOGE_EJACULATES[randrange(0,len(DOGE_EJACULATES))],
                       DOGE_FACE_FILE) 
            move_next_iter = True

        clause = doge_syntax(clause)
        insert(clause, DOGE_FACE_FILE)

    for line in DOGE_FACE_FILE:
        print(line)
