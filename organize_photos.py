#!/usr/bin/env python3
# os.listdir
# os.mkdir
# os.rename to move files

import os

# os.chdir("photos")
# originals = os.listdir(".")


def extract_place(filename):
    # first = filename.find("_")
    # partial = filename[first+1:]
    # second = partial.find("_")
    # place = partial[:second]
    # return place
    print(filename)
    return filename.split("_")[1]


def make_place_dictionaries(places):
    for place in places:
        os.mkdir(place)


# create_directory("originals")
def organise_photots(directory):
    places = []
    os.chdir(directory)
    originals = os.listdir()
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)
    make_place_dictionaries(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


directory = "photos"
organise_photots(directory)
