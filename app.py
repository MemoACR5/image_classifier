from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import load_img


app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    img = tf.keras.utils.load_img(image_path)
    resize = tf.image.resize(img, (256,256))

    model = load_model('./imageclassifier.h5')
    yhat = model.predict(np.expand_dims(resize/255, 0))

    if yhat > 0.5: 
        yhat = "Sad"
        print(f'Predicted class is Sad')
    else:
        yhat = "Happy"
        print(f'Predicted class is Happy')


    return render_template('index.html', prediction=yhat)


if __name__ == '__main__':
    app.run(port=3000, debug=True)