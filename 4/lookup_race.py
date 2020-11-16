#!/usr/bin/env python3

import random
import timeit

def pop_random(a_seq):
    choice = random.choice(a_seq);
    a_seq.remove(choice);
    return choice;

def main():
    test_data = [
        ("key", "value"),
        ("name", "value"),
        ("compiled", "down"),
        ("interpreted", "down"),
        ("transpiled", "up"),
        ("quotations", "prose"),
        ("crochets", "music"),
        ("pronunciation", "pronounce"),
        ("enunciation", "enunciate"),
        ("asia", "large"),
        ("europe", "large"),
        ("svalbard", "large"),
        ("studio bedroom", "large"),
        ("お言葉", "for good measure")
    ];

if __name__ == "__main__": main();
