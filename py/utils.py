import string

def leet_transform(word):
    variations = {word}
    leet_map = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7', '+'],
        'l': ['1'],
        'g': ['9'],
    }
 
    current_variations = {word}
    for char_index, char in enumerate(word.lower()):
        if char in leet_map:
            new_variations_for_char = set()
            for existing_word in current_variations:
                for sub_char in leet_map[char]:
                    new_word_list = list(existing_word)
                    if existing_word[char_index].lower() == char: 
                        new_word_list[char_index] = sub_char
                        new_variations_for_char.add("".join(new_word_list))
            current_variations.update(new_variations_for_char)
    variations.update(current_variations)
    return variations

def append_years(word, years=range(2000, 2026)):
    variations = set()
    for year in years:
        variations.add(f"{word}{year}")
    return variations

def character_substitution(word):
    variations = {word}
    substitutions = {
        'a': ['@', '4'],
        's': ['$', '5'],
        'i': ['1', '!'],
        'o': ['0'],
        'e': ['3'],
        'l': ['1'],
        'b': ['8'],
        'g': ['9'],
        'z': ['2'],
    }

    for i, char in enumerate(word.lower()):
        if char in substitutions:
            for sub_char in substitutions[char]:
                new_word_list = list(word)
                new_word_list[i] = sub_char
                variations.add("".join(new_word_list))

    return variations

def character_duplication(word):
    variations = {word}
    if len(word) > 0:
        last_char = word[-1]
        for i in range(1, 4):
            variations.add(f"{word}{last_char * i}")

    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            variations.add(word[:i+1] + word[i] + word[i+1:])

    for i in range(len(word)):
        variations.add(word[:i+1] + word[i] + word[i+1:])

    return variations