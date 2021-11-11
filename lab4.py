# course: Object-oriented programming, year 2, semester 1
# academic year: 202122
# author: B. Schoen-Phelan
# date: 14-10-2021
# purpose: Lab 4

import sys


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)
        list1 = list(self.user_input)
        list2 = list1
        i = 0
        j = 0
        print(list1)
        while i < ((len(list1)/2)):
            list1[i + 1], list1[i + 2] = list1[i +2], list1[i + 1]
            list1[j - 2], list1[j - 3] = list1[j -3], list1[j - 2]
            i = i + 1
            j = j + 1

        list1[0] == list2[0]
        list1[-1] == list2[-1]
        print(list1)


        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

