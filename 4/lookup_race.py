#!/usr/bin/env python3

##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##

import timeit

def something():
    string = "";
    for number in range(1, 10):
        string += str(number);
    return string;

def main():
    print(timeit.timeit(something));

if __name__ == "__main__": main();
