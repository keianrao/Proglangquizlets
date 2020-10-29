#!/bin/sh

# I use quite a bit of helper functions in this script.
# Basically all of them are reusable (generic) - but, I'll just
# introduce each right before I use them for the first time.



# Fill default values for columns if needed

test -n "$NAME_1" || NAME_1="Name"
test -n "$NAME_2" || NAME_2="Role"
test -n "$WIDTH_1" || WIDTH_1=32
test -n "$WIDTH_2" || WIDTH_2=16
test -n "$WIDTH_3" || WIDTH_3=0
test -n "$WIDTH_4" || WIDTH_4=0



# Validate column widths

regexMatch() { echo "$2" | egrep -q "$1"; }

isNaturalNumber() regexMatch "^[0-9]+$" "$1"

abort() { test -z "$1" || echo "$1" >&2; exit ${EXIT_CODE:-1}; }

isNaturalNumber "$WIDTH_1" || abort "Column 1 width is invalid!"
isNaturalNumber "$WIDTH_2" || abort "Column 2 width is invalid!"
isNaturalNumber "$WIDTH_3" || abort "Column 3 width is invalid!"
isNaturalNumber "$WIDTH_4" || abort "Column 4 width is invalid!"



# Print title line

stringWidth() { printf "%s" "$1" | wc --chars; }

truncateString()
{
    isNaturalNumber "$2" || failAssert "'$2' is not a valid string width"

    if test $2 -eq 0
        then echo ""
    elif test $(stringWidth "$1") -lt $2
        then echo "$1"  # No truncation needed
    else
        substringLength=$(expr $2 '-' 2)
        printf "%s%s\n" "$(echo "$1" | cut -c-$substringLength)" ".."
    fi
}

# Now that we have truncateString, let's truncate the column names first.
NAME_1="$(truncateString "$NAME_1" $WIDTH_1)"
NAME_2="$(truncateString "$NAME_2" $WIDTH_2)"
NAME_3="$(truncateString "$NAME_3" $WIDTH_3)"
NAME_4="$(truncateString "$NAME_4" $WIDTH_4)"

# Then print the title line.
printf \
    "%-4s%-${WIDTH_1}s%-${WIDTH_2}s%-${WIDTH_3}s%-${WIDTH_4}s\n" \
    "#" "${NAME_1}" "${NAME_2}" "${NAME_3}" "${NAME_4}"
# The format string is one of these for each column: '%-${WIDTH}s'.
# For example, a WIDTH of 40 makes this '%-40s'.
# - Recall that '%s' is the specifier for a string.
# - The '-' flag after '%' makes it left justified.
# - The numerical $WIDTH after '-' specifies the field width.
# What we're doing here is delegating to trusty printf, older-than-me.
# Were it not around.. we can implement right-padding ourselves.



# Okay, go ahead and start reading input and translating.

currentLine=1
while IFS=: read VALUE_1 VALUE_2 VALUE_3 VALUE_4
do
    VALUE_1="$(truncateString "$VALUE_1" $WIDTH_1)"
    VALUE_2="$(truncateString "$VALUE_2" $WIDTH_2)"
    VALUE_3="$(truncateString "$VALUE_3" $WIDTH_3)"
    VALUE_4="$(truncateString "$VALUE_4" $WIDTH_4)"

    printf \
        "%-4s%-${WIDTH_1}s%-${WIDTH_2}s%-${WIDTH_3}s%-${WIDTH_4}s\n" \
        "$currentLine" "${VALUE_1}" "${VALUE_2}" "${VALUE_3}" "${VALUE_4}"

    currentLine=$(expr $currentLine '+' 1)
done
