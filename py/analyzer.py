from zxcvbn import zxcvbn 
import random
import string

def analyze_password(password):
     result = zxcvbn(password)
     score = result['score']
     feedback = result['feedback']
     crack_times = result['crack_times_display']
         
     print("\n--- Password Strength Analysis ---")
     print(f"\n Password: {password}")
     print(f"Score (0-4, 4 is strongest): {result['score']}/4")
     print(f"Estimated time to crack (offline, slow hash): {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
     print("\n  Feedback:")

     if result['feedback']['suggestions']:
        for suggestion in result['feedback']['suggestions']:
            print(f"- {suggestion}")
     else:
        print("- No specific suggestions from zxcvbn.")

     if result['feedback']['warning']:
        print(f"\n Warning: {result['feedback']['warning']}") 

     strong_password_suggestion = None 
     if score < 3:
        strong_password_suggestion = suggest_strong_password()
        print(f"\n For a stronger password, consider: {strong_password_suggestion}\n")
     return score, feedback, crack_times, strong_password_suggestion

def suggest_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))  