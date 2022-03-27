from textblob import TextBlob
from flask import Flask, request, render_template
from PIL import Image, ExifTags
import requests

app = Flask(__name__)

# @app.route("/start", methods=["GET"])
# def hello_world():
#     return 'Moe Flask приложение в контейнере Docker.'


@app.route("/exif", methods=['POST'])
def exifImage():
    print("exif image")
    # print(request.get_json())
    a = request.get_json()
    # print(type(a))
    # print(a)
    # url="http://127.0.0.1:3333/" + a['body']['file']['tmpPath']

    # req = requests.get(url, stream = True)

    # # img = request.files.get('file', '')

    # with open ("image.png", "wb") as f:
    #     for chunk in req:
    #         f.write(chunk)
    req = requests.get("http://host.minikube.internal:3333/uploads/"+a["fileName"], stream = True)
    if req.status_code == 200:
        with open("image.png", "wb") as f:
            for chunk in req:
                f.write(chunk)
    # f = open("qwer.png", "w")
    # f.write(req.content)
    img = Image.open("image.png")
    print(img)
    try:
        exifData = {
            ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in ExifTags.TAGS
        }
    except: exifData = {'data' : 'нет данных'}

    print(exifData)
    return str(exifData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
