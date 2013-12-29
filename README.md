# Dogesay #

Cowsay for a new generation!

Dogesay is based on the ridiculous [doge](http://knowyourmeme.com/memes/doge)
meme.

It takes in, as its argument, either:
* a collection of either single words or full clauses; or
* a text file containing a new-line delineated list of either single words or
  full clauses.

From this, it generates doge with the trademark text (randomly arranged around
doge).
  
Per doge convention, the script generates a random amount of "wow" to stick in
alongside the user-provided clauses.

## Example ##

`python dogesay.py -f ex/example.txt`
![Dogesay scrot](ex/ex_scrot.jpg?raw=true)

`python dogesay.py "computer science wow" "shibe" "hacker ethic" "free as in freedom" "GNU"`

## Acknowlegement ##

I snagged the doge graphic from
[user thiderman's `doge` project](https://github.com/thiderman/doge).

## TODO ##
* Implement text generation on doge's left as well as right (kind of low on my
  priorities; it's turning out to be a total nightmare to deal with)
* If you look at source, I include an option for ASCII doge that I haven't
  gotten around to implementing just yet
* Option to take in strings as command-line arguments (as well as from file)
* Pretty text colors
