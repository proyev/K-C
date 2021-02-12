def valentines_start():
    return [
        "Happy Valentine’s Day to the most <admiration> person in <sender_poss> life",
        "Especially today <sender> hope you know how much <sender> <love> you",
        "<sender_verb> <emphasis> in love with you, <sender_poss> <lovenick>",
        "When <sender_verb> with you everything is <positive>",
    ]


def valentines_mid():
    return [
        "Every moment with you is <positive>",
        "With you everything is full of <good>",
        "When <sender> think of you <sender> think of <good>",
        "You are <sender_poss> everything <name>",
        "You mean the world to <sender_rel> <name>",
    ]


def valentines_end():
    return [
        "<sender> <love> you more than anything <name>",
        "Happy Valentine's Day, <lovenick>",
        "You are <admiration> <name>, <sender> <love> you with all <sender_poss> heart",
        "<sender> <love> you forever",
    ]


# -----------------------------

def death_start():
    return [
        "<sender> hope you are coping well in these <negative> times",
        "<sender> feel for you in this <negative> <bad>",
        "<sender> can't begin to imagine how <negative> this <bad> must be for you",
        "All <sender> can do in this <negative> moment is to wish you <wish_sad>",
    ]


def death_deceased():
    # replace dead with gender if not otherwise specified
    return [
        "<dead> was truly <admiration>, <gender> will be sorely missed",
        "Wherever <dead> may be now, <sender> hope she experiences <good>",
        "<dead> will be <emphasis> missed",
        "<dead> lived a <positive> life",
        "<sender> know how much <dead> meant to you <name>",
    ]


def death_end():
    return [
        "<sender_verb> <emphasis> sorry for your loss <name>",
        "<sender_verb> with you and wish you <wish_sad> as you grieve",
        "know that <sender_verb> with you and wish you <wish_sad> as you grieve",
        "<sender_poss> thoughts and prayers are with you <name>",
    ]


# -----------------------------

def birthday_start():
    return [
        "Congratulations on your <age_nr> birthday",
        "Happy <age_nr> Birthday",
        "<sender> wish you a very <positive> <age_nr> birthday",
        "celebrate this <positive> day",
    ]


def birthday_age():
    return [
        "<age> years of age, time does fly by",
        "You may be <age> now, but you haven't changed a bit <name>",
        "<age> years old, but still the same <admiration> person",
        "You are <age> now, what a <positive> number",
    ]


def birthday_end():
    return [
        "Wishing you a <emphasis> <positive> day <name>",
        "<sender> hope you have a <positive> day today and the year ahead is full of <good>",
        "<wish_happy> for your birthday and every day",
    ]


# -----------------------------

def generic_end():
    # join this with wedding_end or birthday_end
    return [
        "you are <emphasis> <admiration>, <sender> wish you <wish_happy>",
        "you are <admiration>, <sender> wish you lots of <good>",
        "May all your dreams come true and <good> follow you",
        "May your life from this day onwards be full of <good>",
        "On this special day <sender> wish you <wish_happy> dear <name>",
    ]


# -----------------------------

def wedding_start():
    return [
        "<name> <sender> wish you <wish_happy> for your wedding and a <positive> time together",
        "<sender> wish you <wish_happy> for your wedding and <wish_happy> in the <positive> years ahead",
        "congratulations on your wedding <name>, <sender> wish you <wish_happy>",
        "thank you for this <positive> day <name>, here's to a future of <good>",
    ]


def wedding_end():
    return [
        "<wish_happy> to you <admiration> couple",
        "may your marriage be <positive> and your bond grow ever stronger",
        "may your new lives together be <positive> and filled with <good>",
    ]


# -----------------------------

def address_generic_anon():
    # join this with any specific anon
    return {
        "fun": ["Hey you", "How's it going", "What's up"],
        "poetic": ["Many greetings", "<sender> hope this finds you in good health", "Greetings", "Salutations"],
        "neutral": ["Hello dear", "Hello, how are you?"],
        "formal": ["Dear colleague", "Hello", "To whom it may concern"],
    }


def address_generic_known():
    # join this with any specific known
    return {
        "fun": ["Hey <name>", "What's good <name>", "To the one and only <name>"],
        "poetic": ["To the <admiration> <name>", "Oh <admiration> <name>", "Warm Greetings <name>"],
        "neutral": ["Dear <name>"],
        "formal": ["Esteemed <name>", "To <name>"],
    }


def address_wedding_anon():
    return {
        "fun": ["To <sender_poss> favourite couple", "Hey you two lovebirds", "To the lucky groom and foolish bride"],
        "poetic": ["A toast to the <admiration> newlyweds", "Dear <admiration> groom, most <admiration> bride"],
        "neutral": ["To the <admiration> couple", "Dear newlyweds"],
        "formal": ["To the newlyweds", "To the groom and bride"],
    }

def address_wedding_known():
    # only used when two names are given
    return {
        "fun": ["Hey <name>, you two lovebirds", "To <name>, the stars of the day"],
        "poetic": ["To the <admiration> conjoined souls <name>", "To the most <admiration> <name>"],
        "neutral": ["To <name>, the <admiration> couple", "Dear newlyweds <name>"],
        "formal": ["To the newlyweds <name>"],
    }



def address_death_anon():
    return {
        "fun": ["Tough times huh", "Sending warm hugs your way", "<sender_verb> <emphasis> sorry for you"],
        "poetic": ["<sender> write you in this time of <bad>",
                   "with heavy heart <sender> write you in this <negative> moment"],
        "neutral": ["Dear mourning family"],
        "formal": ["To the mourning", "To the family & friends of the deceased"],
    }


def address_death_known():
    # needs many options for fun to balance fun generics, others are fine
    return {
        "fun": ["Hey <name>, this must suck so bad", "Hey <name>, you good?", "Hi <name>, hope you are managing"],
        "poetic": ["In deep sorrow <sender> write to you <name>"],
        "neutral": ["Dear mourning <name>"],
        "formal": ["Esteemed and valued <name>"],
    }


def address_valentines_anon():
    return {
        "fun": ["Hey <lovenick>", "What's up <lovenick>"],
        "poetic": ["To the love of <sender_poss> life", "To <sender_poss> <lovenick>"],
        "neutral": ["Hey <lovenick>"],
        "formal": ["Hello <lovenick>"],
    }


def address_valentines_known():
    return {
        "fun": ["To <sender_poss> <admiration> <name>", "<name>, you <admiration> creature"],
        "poetic": ["Oh <name>, <sender_poss> one and only"],
        "neutral": ["<sender_poss> <admiration> <name>"],
        "formal": ["<admiration> <name>"],
    }


