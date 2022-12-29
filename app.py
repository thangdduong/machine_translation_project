from typing import ContextManager
from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

def translate(text):
    translation = translator.translate(text, dest='vi').text

    return translation

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/translation_api', methods=["GET", "POST"])
def translation_api():
    if request.method == "POST":
        user_query = request.form["user-query"]

        answer = translate(user_query)

        return render_template("index.html", 
                                user_query=user_query, 
                                answer_found=answer)
    else:
        return ("nothing")
    
# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=8080, debug=True)