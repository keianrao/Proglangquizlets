#!/usr/bin/env python3

import sys
from auth import logged_in, login, IncorrectPasswordException


def handle(line):
    fields = line.split(' ');

    if len(fields) < 2:
        printerr("Usage: <username> <valid command>");
        return;

    username = fields[0];
    command = fields[1];

    # Handle login command first..
    if command == "pass":
        if len(fields) != 3:
            printerr("Usage: <username> pass <correct password for the username>");
            return;

        password = fields[2];
        try:
            login(username, password);
            return;
        except IncorrectPasswordException:
            printerr("Wrong password for user \'" + username + "\'.");
            return;

    # All other commands require a login.
    elif not logged_in(username):
        printerr("Username \'" + username + "\' not logged in.");
        pass;

    # Okay, logged in, let's try the next commands..


def printerr(string):
    print(string, file = sys.stderr);



##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##  %%  ##

def main():
    try:
        while True:
            handle(input())
    except (EOFError, KeyboardInterrupt) as e:
        pass

if __name__ == "__main__": main()
