from textblob import TextBlob
from flask import Flask, request, jsonify, json
from PIL import Image, ExifTags
import requests

app = Flask(__name__)


@app.route("/exif", methods=['POST'])
def exifImage():
    print("exif image")
    print(request.get_json())
    a = request.get_json()
    print(type(a))
    print(a)
    # url="http://127.0.0.1:3333/" + a['body']['file']['tmpPath']

    # req = requests.get(url, stream = True)

    # # img = request.files.get('file', '')

    # with open ("image.png", "wb") as f:
    #     for chunk in req:
    #         f.write(chunk)
    img = Image.open(a['body']['file']['tmpPath'])
    print("111")
    exifData = {
        ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in ExifTags.TAGS
    }

    print(exifData)
    return str(exifData)


if __name__ == '__main__':
    app.run(port=5000)
