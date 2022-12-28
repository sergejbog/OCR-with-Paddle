import os
import base64
from werkzeug.utils import secure_filename
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin

def doOcr(img_path, lang='en'):
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=False)
    result = ocr.ocr(img_path, cls=True)
    resultString = ''
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            resultString += line[1][0] + '\n'

    # draw result
    result = result[0]
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')
    return resultString




app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def hello_world():
    data = request.files['file']
    language = request.form['language']

    filename = secure_filename(data.filename) # save file 
    filepath = os.path.join("./", filename)
    data.save(filepath)

    resultString = doOcr(filepath, language)

    with open('result.jpg', 'rb') as f:
        image_data = f.read()
    image_str = base64.b64encode(image_data).decode('utf-8')

    response_data = {
        'resultString': resultString,
        'image': image_str
    }

    os.remove(filepath)
    os.remove('result.jpg')
    
    return jsonify(response_data)

if __name__ == "__main__":
    app.run()