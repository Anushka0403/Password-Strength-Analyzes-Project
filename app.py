from flask import Flask, render_template, request
from analyzer import analyze_password
from wordlist_gen import generate_wordlist, export_wordlist
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    wordlist_path = None

    if request.method == 'POST':
        password = request.form.get('password')
        inputs = request.form.get('inputs')
        inputs_list = inputs.split() if inputs else []

        score, feedback, crack_times, suggestion  = analyze_password(password)
        result = {
            'score': score,
            'feedback': feedback,
            'crack_times': crack_times,
            'suggestion': suggestion
        }

        if inputs_list:
            words = generate_wordlist(inputs_list)
            wordlist_path = "static/web_wordlist.txt"
            export_wordlist(words, wordlist_path)
 
    return render_template("index.html", result=result, wordlist_path=wordlist_path)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    if not os.path.exists("wordlists"):
        os.makedirs("wordlists")
    app.run(debug=True)