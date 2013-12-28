#!/usr/bin/python

from argparse import ArgumentParser
from random   import randrange, choice

DOGE_PREFIXES   = ["such", "much", "so", "many", "wow", "very"]
DOGE_EJACULATES = ["wow"]

DOGE_FACE_PATHS = {"norm" : "static/doge.txt",
                   "ascii": "static/doge_ascii.txt"}

WOW_CHANCE = 5
MAX_WHITESPACE = 15

def doge_syntax(clause):
    if len(clause.split()) > 1:
        return clause
    else:
        return DOGE_PREFIXES[randrange(0,len(DOGE_PREFIXES))]+" "+clause

def insert(clause, img_file):
    img_file[randrange(0,len(img_file))] += (" " + clause)

def random_whitespace():
    return randrange(0,MAX_WHITESPACE)*" "
    
if __name__ == "__main__":
    parser = ArgumentParser(description="Cowsay for a new generation.")
    parser.add_argument("inputfile", metavar="<input file>")
    parser.add_argument("-a", "--ascii", action="store_true",
                        help="Use ASCII doge")

    args = parser.parse_args()

    doge_face_path = DOGE_FACE_PATHS["ascii" if args.ascii else "norm"]
    doge_face_file = open(doge_face_path, "r").read().splitlines()

    clauses_file = open(args.inputfile, "r")

    for clause in clauses_file:
        clause = random_whitespace()+doge_syntax(clause.strip())
        move_next_iter = False

        while not move_next_iter:
            if randrange(0,10) > WOW_CHANCE:
                insert(DOGE_EJACULATES[randrange(0,len(DOGE_EJACULATES))],
                       doge_face_file) 
            move_next_iter = True

        insert(clause, doge_face_file)

    for line in doge_face_file:
        print(line)
