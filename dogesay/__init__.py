#!/usr/bin/python

from argparse import ArgumentParser
from random   import randrange, choice

import pkgutil

DOGE_PREFIXES   = ["such", "much", "so", "many", "wow", "very"]
DOGE_EJACULATES = ["wow"]

WOW_CHANCE = 8
MAX_WHITESPACE = 15
MIN_WHITESPACE = 2

def doge_syntax(clause):
    return clause if len(clause.split())>1 else choice(DOGE_PREFIXES)+" "+clause

used_indices = []
def random_select_no_repeat(max, ref_pool):
    index =  randrange(0,max)
    while index in ref_pool:
        index =  randrange(0,max)
    ref_pool.append(index)
    return index

def random_insert_clause(clause, img_file):
    insert_index = random_select_no_repeat(len(img_file), used_indices)
    img_file[insert_index] += (random_whitespace()+clause)

def random_whitespace():
    return randrange(MIN_WHITESPACE, MAX_WHITESPACE)*" "

def generate_ejacs(output):
    while randrange(0,10) > WOW_CHANCE:
        random_insert_clause(choice(DOGE_EJACULATES), output)
    
def doge():
    parser = ArgumentParser(description="Cowsay for a new generation.")
    parser.add_argument("-f", "--file", metavar="<input file>",
                        help="Use text file as input (ignores subsequent clauses)")
    parser.add_argument("clauses", nargs="*",
                        help="things you want doge to say")

    args = parser.parse_args()

    doge_face_lines = pkgutil.get_data("dogesay", "static/doge.txt").decode().split("\n")

    clauses_source = args.clauses if args.file == None else open(args.file, "r")

    for clause in clauses_source:
        clause = random_whitespace()+doge_syntax(clause.strip())

        generate_ejacs(doge_face_lines)

        random_insert_clause(clause, doge_face_lines)

    for line in doge_face_lines:
        print(line)
