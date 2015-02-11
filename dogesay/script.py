from argparse import ArgumentParser
import pkgutil
from . import *

parser = ArgumentParser(description="Cowsay for a new generation.")
parser.add_argument("-f", "--file", metavar="<input file>",
                    help="Use text file as input (ignores subsequent clauses)")
parser.add_argument("clauses", nargs="*",
                    help="things you want doge to say")
def main():
    args            = parser.parse_args()
    doge_face_data  = pkgutil.get_data("dogesay", "static/doge.txt")
    doge_face_lines = doge_face_data.decode().split("\n")

    clauses_source  = args.clauses if args.file == None else open(args.file, "r")

    for clause in clauses_source:
        clause      = random_whitespace()+doge_syntax(clause.strip())

        generate_ejacs(doge_face_lines)
        random_insert_clause(clause, doge_face_lines)

    for line in doge_face_lines:
        print(line)
