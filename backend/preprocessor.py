from dicts import *
from constructor import *
import re


def preprocess(text, style):
    # Do nothing
    if style not in styles:
        return "", {}

    # Assign each marker an index in sequence
    counter = 0
    # Use the number of the marker as the key and the corresponding list of options as values in a dictionary
    options = {}
    # regex to match all defined syntactic markers
    markers = re.findall("<[a-z,_]*>", text)

    # Loop over matched markers, lookup and bind appropriate options
    for i in range(len(markers)):
        current_marker = markers[i]
        if current_marker == "<love>":
            options[counter] = love()[style]
            text = text.replace("<love>", "<{}>".format(counter), 1)
        elif current_marker == "<lovenick>":
            options[counter] = lovenick()[style]
            text = text.replace("<lovenick>", "<{}>".format(counter), 1)
        elif current_marker == "<emphasis>":
            options[counter] = emphasis()[style]
            text = text.replace("<emphasis>", "<{}>".format(counter), 1)
        elif current_marker == "<admiration>":
            options[counter] = admiration()[style]
            text = text.replace("<admiration>", "<{}>".format(counter), 1)
        elif current_marker == "<positive>":
            options[counter] = positive()[style]
            text = text.replace("<positive>", "<{}>".format(counter), 1)
        elif current_marker == "<negative>":
            options[counter] = negative()[style]
            text = text.replace("<negative>", "<{}>".format(counter), 1)
        elif current_marker == "<good>":
            options[counter] = good()[style]
            text = text.replace("<good>", "<{}>".format(counter), 1)
        elif current_marker == "<bad>":
            options[counter] = bad()[style]
            text = text.replace("<bad>", "<{}>".format(counter), 1)
        elif current_marker == "<wish_sad>":
            options[counter] = wish_sad()[style]
            text = text.replace("<wish_sad>", "<{}>".format(counter), 1)
        elif current_marker == "<wish_happy>":
            options[counter] = wish_happy()[style]
            text = text.replace("<wish_happy>", "<{}>".format(counter), 1)
        counter += 1
    return text, options



