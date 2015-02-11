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
