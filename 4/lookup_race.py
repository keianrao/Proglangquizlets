#!/usr/bin/env python3

import random
import timeit

def pop_random(a_seq):
    choice = random.choice(a_seq);
    a_seq.remove(choice);
    return choice;

def main():
    # Initialise test data for this run
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

    # Initialise hash dictionary and associative list
    hash_dict = dict()
    assoc_list = []

    # Okay, start the test.
    random.seed();
    while len(test_data) > 0:
        # Pop random pair from test data and add into both
        (key, value) = pop_random(test_data);
        hash_dict[key] = value;
        assoc_list.append((key, value)); # sic.

        def hash_dict_lookup():
            if key not in hash_dict:
                assert False;
        def assoc_list_lookup():
            for (curr_key, _) in assoc_list:
                if curr_key == key: return;
            assert False;

        # Measure lookup runtime
        hash_dict_time = timeit.timeit(hash_dict_lookup, number = 5);
        assoc_list_time = timeit.timeit(assoc_list_lookup, number = 5);

        if hash_dict_time < assoc_list_time:
            print("Hash dict wins at size " + str(len(hash_dict)));
            print("hash dict " + str(hash_dict_time) + " sec");
            print("assoc list " + str(assoc_list_time) + " sec");
            print(hash_dict);
            return;

if __name__ == "__main__": main();
