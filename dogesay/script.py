from argparse import ArgumentParser
import pkgutil
import random
from random   import randrange, choice

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


parser = ArgumentParser(description="Cowsay for a new generation.")
parser.add_argument("clauses", nargs="*",
                    help="things you want doge to say")
def main():
    args            = parser.parse_args()
    doge_face_data  = pkgutil.get_data(__name__, "static/doge")
    doge_face_lines = doge_face_data.decode('utf8').split("\n")

    clauses_source  = args.clauses

    indices = random.sample(range(len(doge_face_lines)), len(clauses_source))

    for clause, index in zip(clauses_source, indices):
        clause      = random_whitespace()+doge_syntax(clause.strip())

        generate_ejacs(doge_face_lines)
        doge_face_lines[index] += (random_whitespace() + clause)

    for line in doge_face_lines:
        print(line)

if __name__ == "__main__":
    main()
