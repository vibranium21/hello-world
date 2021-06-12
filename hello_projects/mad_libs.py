#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mad Libs Generator."""
# Loop back to this point once code finishes
LOOP = 1
while LOOP < 10:
    # All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
    # Displays the story based on the users input
    print("------------------------------------------")
    print("Be kind to your", noun, "- footed", p_noun)
    print("For a duck may be somebody's", noun2, ",")
    print("Be kind to your", p_noun, "in", place)
    print("Where the weather is always", adjective, ".")
    print()
    print("You may think that is this the", noun3, ",")
    print("Well it is.")
    print("------------------------------------------")
    # Loop back to "LOOP = 1"
    LOOP += 1
