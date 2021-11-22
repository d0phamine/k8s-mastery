from textblob import TextBlob
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/textan", methods=['POST'])
def analyse_sentiment():
    sentence = request.get_json('body')['body']['body']
    print(sentence)
    polarity = TextBlob(sentence).sentences[0].polarity
    print(polarity)
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)