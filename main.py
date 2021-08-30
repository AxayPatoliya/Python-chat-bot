from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("ChatterBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-reply", methods = ['GET', 'POST'])
def chatReply():
    if request.method == "POST":
        msg = request.form.get("message")
        reply = str(english_bot.get_response(msg))
    return render_template("index.html", reply = reply)

if __name__ == "__main__":
    app.run(debug=True)