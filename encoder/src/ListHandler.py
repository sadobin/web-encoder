#! /bin/python3

# Appending parent directory to the path
import sys, os
sys.path.append( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) )


class ListHandler:

    def __init__(self, string, desired_chars, all_chars):

        self.list = []

        if all_chars:
            temp = ''.join( l for l in string)
            self.list += [ i for i in temp+desired_chars ]

        elif desired_chars:
            self.list = [ i for i in desired_chars ]


    def get_list(self):
        return self.list
