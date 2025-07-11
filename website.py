from flask import Flask, render_template, request, url_for
import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename  # For secure filenames

app = Flask(__name__)
UPLOAD_FOLDER = 'static/Image/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def Hello():
    result = None
    image_url = None
    if request.method == "POST":
        file = request.files["file"]
        if file:
            # Secure the filename to prevent path issues
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Generate URL for the uploaded image
            image_url = url_for('static', filename=f'Image/{filename}')
            
            model_path = "C:/tensorflow/classification/Project/malware_detection_model2.h5"
            model = tf.keras.models.load_model(model_path)
            
            img = image.load_img(filepath, target_size=(256, 256))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            predictions = model.predict(img_array)
            confidence = predictions[0][0]
            
            if confidence >= 0.5:
                result = ["Result: Normal", f"Score: {int(confidence * 100)}%"]
            else:
                result = ["Result: Malicious", f"Score: {int((1 - confidence) * 100)}%"]
    
    # Render index.html instead of home.html
    return render_template('home.html', result=result, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)