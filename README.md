# Dogesay #

[![License MIT](http://img.shields.io/:license-mit-blue.svg)](http://jinnovation.mit-license.org/)
[![Gratipay](http://img.shields.io/gratipay/jinnovation.svg)](https://gratipay.com/jinnovation/)
[![Coverage Status](https://coveralls.io/repos/jinnovation/dogesay/badge.svg)](https://coveralls.io/r/jinnovation/dogesay)
[![PyPI](https://img.shields.io/pypi/dm/dogesay.svg)](https://pypi.python.org/pypi/dogesay)

## Author Notes (2020/07/25)

This project was put together by baby me back in college out of boredom. The
code is frankly dreadful, and the project I stole the doge from, 
[`doge`](https://github.com/thiderman/doge), is honestly much better anyway.


## Overview

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

## Install

`pip install dogesay`

## Example ##

`dogesay -f ex/example.txt`
![Dogesay with file as input](ex/ex_scrot_fileinput.jpg?raw=true)

`dogesay "computer science wow" "shibe" "hacker ethic" "free as in
freedom" "GNU"`
![Dogesay with direct arguments](ex/ex_scrot_directarg.jpg?raw=true)

## Acknowlegement ##

I snagged the doge graphic from
[user thiderman's `doge` project](https://github.com/thiderman/doge).

# License
The MIT License (MIT)

Copyright (c) 2013-2015 Jonathan Jin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
