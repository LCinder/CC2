import base64

import cv2
import numpy
import requests


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    # Load the cascade Classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Read the input image
    img = requests.get(req).content
    image = numpy.frombuffer(img, numpy.uint8)
    img = cv2.imdecode(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imwrite("image.png", img)

    with open("image.png", "rb") as f:
        image_final = base64.b64encode(f.read()).decode("utf-8")

    return f'<img src="data:image/jpeg;base64,{image_final}">'
