def fit_bert(text, options, mask_flag, fb):
    """"This is the FitBERT function itself
    
    Takes string with a single ***mask***, dictonary of options of words to be placed in the blank-spot,
    a mask_flag - which corresponds with position of the mask in the text, and list of previously used options
    
    After the mask was replaced with a suitable option, this option is removed from the list of options corresponding to this mask.
    Furthermore, if there are several masks in the whole text, in order to avoid tautologies, the chosen option will be removed from the following dictionaries
    
    In the end, the text with blanks filled, the dict of still available options returned"""

    replaced_elem_id = text.split().index('***mask***')

    filled_in_part = fb.fitb(text, options=options[mask_flag])
    
    used_options = []
    for elem in options[mask_flag]:  # without this loop elements from the list will be dynamicaly corresponded to dict
    	used_options.append(elem)
    
    replaced_elem = filled_in_part.split()[replaced_elem_id]

    for key in options:
        if options[key] == used_options:
            options[key].remove(replaced_elem)
            continue

    return filled_in_part, options



def before(text):
    """The wished step before using BERT
    
    This function will simply process the string and replace the punctuation, so it can be processed by FitBERT correctly"""

    text = text.replace('?\n', ' ? ')
    text = text.replace('\n', ' . ')
    text = text.replace('  ', ' ')
    text = text.replace(', ', ' , ')
    return text

def after(text):
    """This function takes already processed through BERT text and places the punctuation back, so it is correctly formated from now on"""
    return text.replace(' ? ', '?\n').replace(' . ', '.\n').replace('  , ', ', ').replace(' , ', ', ')


def fill_in(text, options, fb): 
    """This function takes the whole text as an input and corresponding dictionary of options to be placed in place of each blank-spot
    
    The function will count the number of the blank-spots and will replace every single one of them iteratively.
    During each iteration, the text up to the next following marker will be used to perform further BERT functions,
    which provides a chance to maximize the quality of the output
    
    The function will return the text with filled blank spots and the dictionary of options that are left after the process
    which makes it possible to generate new different results if the user is not satisfied with the outcome"""

    text = before(text)

    mask_flag = 0

    sentence = text
    mask_count = sentence.count('<')
    while mask_count > 1:
        mask = sentence[sentence.index('<'):sentence.index('>')+1]
        sentence = sentence.replace(mask, '***mask***', 1)
        bert_sentence = sentence[:sentence.index('<')]

        bert_sentence, options = fit_bert(bert_sentence, options, mask_flag, fb)
        sentence = sentence.replace(sentence[:sentence.index('<')], bert_sentence)

        mask_count = sentence.count('<')
        mask_flag += 1

    else:
        mask = sentence[sentence.index('<'):sentence.index('>')+1]
        sentence = sentence.replace(mask, '***mask***', 1)

        filled_in_sentence, afterwards_options = fit_bert(sentence, options, mask_flag, fb)
        filled_in_sentence += '.'  # puts the dot after the last sentence
    filled_in_sentence = after(filled_in_sentence)
    return filled_in_sentence, afterwards_options
