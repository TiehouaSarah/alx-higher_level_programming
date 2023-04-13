#!/usr/bin/python3
""" READING FILE CONTENT """


def read_file(filename=""):
    with open(filename, encoding='utf8') as f:
        contents = f.read()
        print(contents)
