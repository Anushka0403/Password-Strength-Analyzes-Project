from utils import leet_transform, append_years

def generate_wordlist(user_inputs, years=range(2000, 2026)):
    words = set()
    
    for word in user_inputs:
        word = word.lower()
        words.add(word)
        words.update(leet_transform(word))
        words.update(append_years(word, years))
    
    return sorted(words)

def export_wordlist(words, filename='wordlists/custom_wordlist.txt'):
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + '\n')
    print(f"[+] Wordlist exported to {filename}") 