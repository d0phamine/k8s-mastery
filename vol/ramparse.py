from textblob import TextBlob
from flask import Flask, request, jsonify, json
import os 

@app.route("/ramExec", methods=['POST'])
def ramExec():
    print("ram execution")
    a = request.get_json()

    # f = open(a['body']['file']['tmpPath'],"r")




if __name__ == '__main__':
    app.run(port=5001)