import tensorflow as tf 
import numpy as np
#import time 
#import os
from tensorflow import keras

# 1: Regular Shakespear
# 2: Regular Michael Jackson
# 3: Maid of Honor

def process(one_step_reloaded, length, user_input):
    states = None
    next_char = tf.constant([user_input])
    result = [next_char]

    # Vorhersage von <length> Buchstaben zu dem gegebenen Anfang (abgebildet in Zahlenwerten)
    for n in range(length):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)

    # Rückgabe der zusammengefügten, decodierten Vorhersagen
    return tf.strings.join(result)[0].numpy().decode("utf-8")

def text_generation(model, index):
    # Shakepeare 
    if index == 1:
        value = ["Therefore", "How", "But", "Here", "We",
                 "O,", "As", "And", "Come", "The",
                 "Let", "Not", "That", "Until", "Into",
                 "My soul", "Mistake", "To", "Or", "You",
                 "Your"]
        n_to_value = np.random.randint(0, 21)

        # Text erzeugen
        text_part = process(model, 1100, value[n_to_value])

        # Text anpassen: Der Text soll entweder nach einem ".", einem "?" oder einer freien Zeile zurückgegeben werden
        text = ""

        go = 1

        while go == 1:
            try:
                index_qm = text_part.index("?")
            except:
                index_qm = 1110
            try:
                index_point = text_part.index(".")
            except:
                index_point = 1110
            try:
                index_em = text_part.index("!")
            except:
                index_em = 1110

            index_break = text_part.index("\n")
            following = text_part[index_break + 1]                 

            if index_point < index_break and index_point < index_qm and index_point < index_em:
                text += text_part[:index_point + 1]

                go = 0
            elif index_qm < index_break and index_qm < index_point and index_qm < index_em:
                text += text_part[:index_qm + 1]

                go = 0
            elif index_em < index_break and index_em < index_qm and index_em < index_point:
                text += text_part[:index_em + 1]

                go = 0
            else:
                text_part_2 = text_part[:index_break + 1]
                text += text_part_2
                text_part = text_part[index_break + 1:]

                go = 1

                if following == "\n":
                    go = 0

    # Michael Jackson Bearbeitung
    elif index == 2:
        # Zufälligen Textanfang auswählen
        value = ["You", "We", "I wish", "Somebody", "She", "Look", 
                 "Like", "It", "They", "For", "The fire", "Just", 
                 "She called", "What about", "Promise", "Better", 
                 "No", "Good", "Good with", "The girl", "'Cause I", 
                 "You", "You", "Me", "We", "Love", "Angels"] 
        n_to_value = np.random.randint(0, 26)

        # Text erzeugen
        text_part = process(model, 300, value[n_to_value])
        text = ""

        for i in range(0,2):
            #print("i: ", i)
            index = text_part.index('\n')
            text += text_part[:index]
            if i == 0:
                text += "- "
            text_part = text_part[index + 1:]

        text = text.replace("\"", "")

    # Maid of Honor Bearbeitung
    elif index == 3:
        value = ["I wish", "Today", "You are", "Together", "This moment", 
                 "May", "You", "When", "Anna", "Words", "You seem", 
                 "Happily", "Happy", "Last", "I wish it", "I", "Also", 
                 "My soul", "Come", "If", "She", "On", "On behalf", 
                 "Additionally", "Youd should know", "Kindly", "Consistently", 
                 "Everyday", "Every", "Ever", "The spirit", "Taking care"] 
        n_to_value = np.random.randint(0, 32)

        # Text erzeugen
        text = process(model, 600, value[n_to_value])

        # Text verarbeiten
        try:
            index_point = text.index(".")
            text = text[:index_point + 1]
        except:
            text = text[:-1] + "."
            index_point = text.index(".")
        try:
            index_em = text.index("!")
        except:
            index_em = index_point + 1
        try:
            index_qm = text.index("?")
        except:
            index_qm = index_point + 1

        if index_point < index_em and index_point < index_qm:
            text = text[:index_point + 1]
        elif index_em < index_qm:
            text = text[:index_em + 1]
        else:
            text = text[:index_qm + 1]

    else:
        return 0

    text = text.replace("my name is", "") 

    return text