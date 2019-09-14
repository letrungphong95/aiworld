from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
import numpy as np
import cv2
import matplotlib.image as mpimg
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model
sess = tf.Session()
graph = tf.get_default_graph()
# Create your views here.
set_session(sess)
model = load_model('backend/model/saved/vgg16_catdog.h5')
label = ['Cat','Dog']
import base64 


def preprocess_image(img, size):
    """
    This function preprocess test image for prediction
    Arguments:
    -path: 
    -size:
    Returns:
    
    """
    # # Read image from image path
    # image_decoded = mpimg.imread(path)
    imdata = np.frombuffer(img, dtype='uint8')
    image_decoded = cv2.imdecode(imdata, cv2.IMREAD_COLOR)
    # convert to float values in [0, 1]
    image = image_decoded/ 255
    # resize image to fit the input size
    resized_image = cv2.resize(image, (size, size))
    # Scale to [0,255]
    resized_image = resized_image*255
    # Transpote from RGB to BGR then subtract for mean(imagenet)
    resized_image = resized_image[...,::-1] - [103.939,116.779,123.68]
    # Reshape tensor
    resized_image = resized_image.reshape((1, size, size, 3))
    return resized_image

"""
Method: POST
Src: {APP_URL}/api/object-label
Header: 
Body:
{
	"image_path": "base_64_image"
} 
Response:
{
    "label": "Cat",
    "scores": 0.9
}
"""
@csrf_exempt
def predict_label(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        img_path = data['image_path']
        # Convert image to base64 string
        img_base64 = bytes(img_path.split(',')[-1], 'utf-8')
        # Convert image to byte
        img_byte = base64.decodestring(img_base64)
        image = preprocess_image(img=img_byte, size=224)
        global sess
        global graph
        with graph.as_default():
            set_session(sess)
            result = model.predict(image)
            return HttpResponse(json.dumps({"label":label[result.argmax()], "scores": str(round(result.max()*100, 2)) + "%"}))
    else:
        return HttpResponseBadRequest("GET is not allowed")


