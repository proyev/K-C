import numpy as np
from dicts import *
from templates import *

# acceptable styles
styles = ["fun", "poetic", "neutral", "formal"]

# NOTE: These functions share a lot of very similar, but not identical steps

def wedding_constructor(plural, style, name1, name2):
    # Do nothing
    if style not in styles:
        return ""

    # Select appropriate replacements for narrator (sender)
    sender = ""
    sender_poss = ""
    sender_verb = ""
    sender_rel = ""
    if plural:
        sender = get_sender()[1]
        sender_poss = get_sender_poss()[1]
        sender_verb = get_sender_verb()[1]
        sender_rel = get_sender_rel()[1]
    else:
        sender = get_sender()[0]
        sender_poss = get_sender_poss()[0]
        sender_verb = get_sender_verb()[0]
        sender_rel = get_sender_rel()[0]

    # Fuse names
    name = ""
    if name1 is not None:
        if name2 is not None:
            name = "{} and {}".format(name1, name2)
        else:
            name = name1
    else:
        if name2 is not None:
            name = name2
        # else don't overwrite name

    # possible greeting formulas
    known = name != ""
    address_options = []
    if known:
        address_options = np.concatenate((address_generic_known()[style], address_wedding_known()[style]))
    else:
        address_options = np.concatenate((address_generic_anon()[style], address_wedding_anon()[style]))

    # decide on template components
    address = choose_random(address_options)
    start = choose_random(wedding_start())
    # wedding can also use generic end
    end = choose_random(np.concatenate((generic_end(), wedding_end())))

    # Build full text
    separator = "\n"
    text = separator.join([address, start, end])

    # always mentioning name would be too repetitive
    # but has to occur at least once, i.e. in the greeting
    text = text.replace("<name>", name, 1)
    if name != "":
        while "<name>" in text:
            if np.random.random() < 0.5:
                text = text.replace("<name>", name, 1)
            else:
                text = text.replace("<name>", "", 1)
    else:
        text = text.replace("<name>", name)

    # replace hard-set markers
    text = text.replace("<sender>", sender).replace("<sender_verb>", sender_verb) \
        .replace("<sender_rel>", sender_rel).replace("<sender_poss>", sender_poss)

    return text


def birthday_constructor(plural, style, name1, age):
    # Do nothing
    if style not in styles:
        return ""

    # Select appropriate replacements for narrator (sender)
    sender = ""
    sender_poss = ""
    sender_verb = ""
    sender_rel = ""
    if plural:
        sender = get_sender()[1]
        sender_poss = get_sender_poss()[1]
        sender_verb = get_sender_verb()[1]
        sender_rel = get_sender_rel()[1]
    else:
        sender = get_sender()[0]
        sender_poss = get_sender_poss()[0]
        sender_verb = get_sender_verb()[0]
        sender_rel = get_sender_rel()[0]

    # birthday specific information
    name = ""
    if name1 is not None:
        name = name1
    age_string = ""
    age_nr = ""
    if age != 0:
        age_string = str(age)
        if age_string[-1:] == "1":
            age_nr = age_string + "st"
        elif age_string[-1:] == "2":
            age_nr = age_string + "nd"
        elif age_string[-1:] == "3":
            age_nr = age_string + "rd"
        else:
            age_nr = age_string + "th"

    # possible greeting formulas
    known = name1 is not None
    address_options = []
    if known:
        address_options = address_generic_known()[style]
    else:
        address_options = address_generic_anon()[style]

    # decide on template components
    address = choose_random(address_options)
    start = choose_random(birthday_start())
    middle = None
    if age:
        middle = choose_random(birthday_age())
    # birthday can also use generic end
    end = choose_random(np.concatenate((generic_end(), birthday_end())))

    # Build full text
    separator = "\n"
    text = ""
    text += (address + separator)
    text += (start + separator)
    if middle:
        text += (middle + separator)
    text += end

    # always mentioning name would be too repetitive
    # but has to occur at least once, i.e. in the greeting
    text = text.replace("<name>", name, 1)
    if name != "":
        while "<name>" in text:
            if np.random.random() < 0.5:
                text = text.replace("<name>", name, 1)
            else:
                text = text.replace("<name>", "", 1)
    else:
        text = text.replace("<name>", name)

    # replace hard-set markers
    text = text.replace("<sender>", sender).replace("<sender_verb>", sender_verb) \
        .replace("<sender_rel>", sender_rel).replace("<sender_poss>", sender_poss)
    text = text.replace("<age>", age_string).replace("<age_nr>", age_nr)

    return text


def funeral_constructor(plural, style, name1, name2, gender):
    # Do nothing
    if style not in styles:
        return ""

    # Select appropriate replacements for narrator (sender)
    sender = ""
    sender_poss = ""
    sender_verb = ""
    sender_rel = ""
    if plural:
        sender = get_sender()[1]
        sender_poss = get_sender_poss()[1]
        sender_verb = get_sender_verb()[1]
        sender_rel = get_sender_rel()[1]
    else:
        sender = get_sender()[0]
        sender_poss = get_sender_poss()[0]
        sender_verb = get_sender_verb()[0]
        sender_rel = get_sender_rel()[0]

    # death specific information
    name = name1
    if gender == "male":
        dead_gender = get_gender()[0]
    if gender == "female":
        dead_gender = get_gender()[1]
    # if no name present replace with pronoun
    dead = ""
    if name2 is not None:
        dead = name2
    else:
        dead = dead_gender

    # possible greeting formulas
    known = name1 is not None
    name = ""
    address_options = []
    if known:
        address_options = np.concatenate((address_generic_known()[style], address_death_known()[style]))
        name = name1
    else:
        address_options = np.concatenate((address_generic_anon()[style], address_death_anon()[style]))

    # decide on template components
    address = choose_random(address_options)
    start = choose_random(death_start())
    middle = choose_random(death_deceased())
    end = choose_random(death_end())

    # Build full text
    separator = "\n"
    text = separator.join([address, start, middle, end])

    # always mentioning name would be too repetitive
    # but has to occur at least once, i.e. in the greeting
    text = text.replace("<name>", name, 1)
    if name != "":
        while "<name>" in text:
            if np.random.random() < 0.5:
                text = text.replace("<name>", name, 1)
            else:
                text = text.replace("<name>", "", 1)
    else:
        text = text.replace("<name>", name)

    # replace hard-set markers
    text = text.replace("<dead>", dead).replace("<gender>", dead_gender)
    text = text.replace("<sender>", sender).replace("<sender_verb>", sender_verb) \
        .replace("<sender_rel>", sender_rel).replace("<sender_poss>", sender_poss)

    return text


def valentines_constructor(plural, style, name1):
    # Do nothing
    if style not in styles:
        return ""

    # Select appropriate replacements for narrator (sender)
    sender = ""
    sender_poss = ""
    sender_verb = ""
    sender_rel = ""
    if plural:
        sender = get_sender()[1]
        sender_poss = get_sender_poss()[1]
        sender_verb = get_sender_verb()[1]
        sender_rel = get_sender_rel()[1]
    else:
        sender = get_sender()[0]
        sender_poss = get_sender_poss()[0]
        sender_verb = get_sender_verb()[0]
        sender_rel = get_sender_rel()[0]

    # name is optional
    name = ""
    if name1 is not None:
        name = name1

    # possible greeting formulas
    known = name1 is not None
    address_options = []
    if known:
        address_options = np.concatenate((address_generic_known()[style], address_valentines_known()[style]))
    else:
        address_options = np.concatenate((address_generic_anon()[style], address_valentines_anon()[style]))

    # decide on template components
    address = choose_random(address_options)
    start = choose_random(valentines_start())
    middle = choose_random(valentines_mid())
    end = choose_random(valentines_end())

    # Build full text
    separator = "\n"
    text = separator.join([address, start, middle, end])

    # always mentioning name would be too repetitive
    # but has to occur at least once, i.e. in the greeting
    text = text.replace("<name>", name, 1)
    if name != "":
        while "<name>" in text:
            if np.random.random() < 0.5:
                text = text.replace("<name>", name, 1)
            else:
                text = text.replace("<name>", "", 1)
    else:
        text = text.replace("<name>", name)

    # replace hard-set markers
    text = text.replace("<sender>", sender).replace("<sender_verb>", sender_verb) \
        .replace("<sender_rel>", sender_rel).replace("<sender_poss>", sender_poss)

    return text

# helper function for selection
def choose_random(arr):
    index = np.random.randint(0, len(arr))
    result = arr[index]
    return result
