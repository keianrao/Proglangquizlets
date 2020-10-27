#!/usr/bin/env python3

def main():
    dinner = {
        "appetiser": "soup",
        "main": {
            "staple": "rice",
            "meat": "fried tofu",
            "vegetables": "bitter gourd"
        },
        "drink": "tea"
    };
    # That should be a nested dictionary, in Python..

    def printAtomics(dictionary, prefix = ""):
        for key in dictionary:
            value = dictionary[key];
            if type(value) is dict:
                nextprefix = prefix + key + ".";
                printAtomics(value, nextprefix);
            else:
                print("{}{} = {}".format(prefix, key, value));

    printAtomics(dinner);


if __name__ == "__main__":
    main()
