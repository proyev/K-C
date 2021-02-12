# Direct insertion

# <name>
# <dead>
# <age>
# <age_nr>

# -----------------------------

# Fixed ones

def get_sender():
    return ["I", "we"]

def get_sender_poss():
    return ["my", "our"]

def get_sender_verb():
    return ["I am", "we are"]

def get_sender_rel():
    return ["me", "us"]

def get_gender():
    return["he", "she"]


# -----------------------------

# Insertions by BERT

def love():
    # verb synonyms
    return {
        "fun": ["idolize", "worship", "caress", "chase"],
        "poetic": ["worship", "exalt", "treasure", "cherish"],
        "neutral": ["love", "care", "adore", "need"],
        "formal": ["require", "respect", "applaud", "commend"],
    }

def lovenick():
    # cute nicknames
    return {
        "fun": ["Snuggles", "Teddybear", "Pumpkin", "Baby", "Cutie-pie", "Precious", "Honey", "Buttercup"],
        "poetic": ["rosepetal", "blossom", "angeleyes", "sunshine", "enchanting", "sunlight", "wildfire"],
        "neutral": ["Love", "Beautiful", "Gorgeous", "Handsome", "Sweetheart", "Precious", "Darling", "Honey"],
        "formal": ["companion", "rolemodel", "Wonderful", "Dear", "Stunning", "Mate", "Partner", "acquaintance"],
    }

def emphasis():
    # adverbs that exaggerate
    return {
        "fun": ["unimaginably", "absolutely", "sanely", "undoubtedly", "extremely", "super", "incredibly", "acutely",
                "excessively", "severely"],
        "poetic": ["unequivocally", "veraciously", "truthfully", "wholeheartedly", "profoundly", "candidly"],
        "neutral": ["truly", "sorely", "deeply", "genuinely", "sincerely", "utterly", "terrifically"],
        "formal": ["genuinely", "positively", "undoubtedly", "firmly", "earnestly", "profoundly", "inordinately",
                   "immensely"],
    }

def admiration():
    # adjectives to describe person
    return {
        "fun": ["stunning", "flashy", "sweet", "awesome", "ingenious", "preposterous", "stimulating", "cool"],
        "poetic": ["sparkling", "dazzling", "brilliant", "exhilarating", "ravishing", "splendid", "prodigious"],
        "neutral": ["astonishing", "beloved", "extraordinary", "caring", "special", "terrific", "brilliant",
                    "wonderful", "heartwarming"],
        "formal": ["remarkable", "inspiring", "commendable", "extraordinary", "admirable", "motivating", "innovative"],
    }

def positive():
    # adjectives to describe thing
    return {
        "fun": ["wonderful", "beautiful", "fantastic", "amazing", "stunning", "bedazzling", "fabulous", "outrageous",
                "breathtaking", "thrilling"],
        "poetic": ["magnificent", "marvelous", "astounding", "wondrous", "striking", "spectacular", "fabulous",
                   "superb", "merry"],
        "neutral": ["happy", "nice", "joyful", "wonderful", "pleasant", "fascinating", "sweet", "pleasing", "charming",
                    "delightful"],
        "formal": ["fruitful", "pleasant", "harmonious", "enjoyable", "rewarding", "impressive", "remarkable",
                   "amiable", "satisfying", "cordial"],
    }

def negative():
    # adjectives to describe thing
    return {
        "fun": ["dreadful", "depressing", "excruciating", "awful", "depressing", "brutal", "terrifying", "bad",
                "cruel"],
        "poetic": ["sinister", "mournful", "somber", "dismal", "dire", "sorrowful", "cheerless", "dreadful",
                   "arduous"],
        "neutral": ["dark", "sad", "sinister", "bitter", "rough", "harsh", "terrible", "grave", "painful", "hurtful"],
        "formal": ["regrettable", "distressing", "grave", "saddening", "dire", "grave", "severe", "displeasing"],
    }

def good():
    # nouns, good concepts
    return {
        "fun": ["lovemaking", "pleasure", "happiness", "surprises", "thrill", "adventure"],
        "poetic": ["joy", "delight", "elation", "euphoria", "jubilation", "prosperity", "ecstasy",
                   "delectation"],
        "neutral": ["happiness", "wonder", "bliss", "joy", "laughter", "fun", "enjoyment", "comfort"],
        "formal": ["enjoyment", "amusement", "pleasantries", "harmony", "fulfillment", "optimism",
                   "contentment"],
    }

def bad():
    # nouns, bad concepts
    return {
        "fun": ["pain", "misery", "darkness", "torture", "torment", "limbo", "nothingness", "void", "suffering"],
        "poetic": ["tragedy", "agony", "woe", "gloom", "anguish", "despair", "bereavement", "wailing", "heartache",
                   "peril"],
        "neutral": ["sorrow", "sadness", "pain", "grief", "hurting", "mourning", "difficulty", "hardship", "disbelief"],
        "formal": ["tragedy", "mourning", "discomfort", "affliction", "distress", "difficulty", "misfortune"],
    }

def wish_sad():
    # wish in bad times
    return {
        "fun": ["acceptance", "happiness", "hope", "strength", "fortune", "purpose"],
        "poetic": ["fortitude", "perseverance", "steadfastness", "solace"],
        "neutral": ["strength", "stability", "perseverance", "comfort", "consolation", "well"],
        "formal": ["fortitude", "soundness", "well", "stability", "harmony"],
    }

def wish_happy():
    # wish in happy times
    return {
        "fun": ["happiness", "love", "best", "fun", "adventure", "groove"],
        "poetic": ["delight", "pleasure", "abundance", "exuberance", "vigor"],
        "neutral": ["happiness", "best", "joy", "love", "fun", "enjoyment"],
        "formal": ["wellness", "health", "satisfaction", "wellbeing", "pleasantries", "success"],
    }
