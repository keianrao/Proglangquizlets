#!/usr/bin/env python3

def main():

    # (1)

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


    # (2)

    def printAtomics(dictionary, prefix = ""):
        for key in dictionary:
            value = dictionary[key];
            if type(value) is dict:
                nextprefix = prefix + key + ".";
                printAtomics(value, nextprefix);
            else:
                print("{}{} = {}".format(prefix, key, value));

    printAtomics(dinner);


    print("----------");


    # (3), (4)

    class CustomDictionary(dict):
        def __str__(self):
            def get_kv_strings(key):
                value = self[key];

                if type(value) is CustomDictionary:
                    # I couldn't find a way to avoid this typecheck to
                    # actively add prefxies where needed. A helper function
                    # '__str2__' may have helped, but I interpret the
                    # problem as allowing only one override.

                    prefix = f"{key}.";
                    stringified_kv_lines = str(value);
                    return (
                        prefix +
                        stringified_kv_lines.replace("\n", f"\n{prefix}")
                    );
                    # This code doesn't have a very Pythonic look..

                else: return f"{key} = {value}";

            return '\n'.join([get_kv_strings(key) for key in self]);

    dinner2 = CustomDictionary();
    dinner2["appetiser"] = "soup"
    dinner2["main"] = CustomDictionary();
    dinner2["main"]["staple"] = "rice";
    dinner2["main"]["meat"] = "fried tofu";
    dinner2["main"]["vegetables"] = "bitter gourd";
    dinner2["drink"] = "tea";
    # There's probably a better way to do this?

    print(dinner2);


if __name__ == "__main__":
    main()
