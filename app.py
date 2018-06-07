from flask import Flask, request, render_template, make_response,jsonify
from flask_bootstrap import Bootstrap

import os
import uuid
import base64
import image_management
import db_access

from PIL import Image
import warnings
warnings.simplefilter('error', Image.DecompressionBombWarning)

app = Flask(__name__, static_folder='imgs')
bootstrap = Bootstrap(app)


@app.route('/')
def do_get():
    return render_template('index.html')

@app.route('/list')
def page_image_list():
    return render_template('imagelist.html')

@app.route('/api/image/list', methods=['GET'])
def imagelist():
    results = db_access.findImagesWithUserId(request.args.get('userId'))
    images = []
    if results and results.count() > 0:
        for r in results:
            image = {}
            image['url'] = r['url']
            image['thumbnail'] = r['thumbnail']
            images.append(image)
    return make_response(jsonify(images), 200)
    return images

@app.route('/api/image', methods=['POST'])
def saveimage():
    event = request.form.to_dict()

    dir_name = 'imgs'
    img_name = uuid.uuid4().hex
    userId = event['user_id']

    # Saving image in the 'imgs' folder temporarily. Should be deleted after a certain period of time
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(os.path.join(dir_name, '{}.png'.format(img_name)), 'wb') as img:
        img.write(base64.b64decode(event['image'].split(",")[1]))

    original_filepath = os.path.join(dir_name, '{}.png'.format(img_name))

    url, imageId = image_management.upload(original_filepath, userId)
    thumbnail = image_management.getPreviewImage(imageId)
    db_access.addImage(userId, imageId, url, thumbnail)

    return make_response(jsonify({'url':url,'thumbnail':thumbnail}), 200)


if __name__ == '__main__':
    app.debug = True
    app.run()
