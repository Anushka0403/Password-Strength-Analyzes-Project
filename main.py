import argparse
from analyzer import analyze_password
from wordlist_gen import generate_wordlist, export_wordlist

def main():
     parser = argparse.ArgumentParser(description="Analyze password strength and generate custom wordlists.")
     parser.add_argument("-p", "--password", help="Password to analyze.")
     parser.add_argument("-i", "--inputs", nargs='+', help="Custom inputs (e.g., name, pet, etc.)")
     parser.add_argument("-o", "--output", default="wordlists/custom_wordlist.txt", help="Output file")
     args = parser.parse_args()

     if args.password:
        analyze_password(args.password)
     else:
      print(" Please provide a password to analyze using -p or --password.")

      if args.inputs:
         words = generate_wordlist(args.inputs)
         export_wordlist(words, args.output)

if __name__ == "__main__":
    main()