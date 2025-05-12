from flask import Flask, render_template, request
from utils.process_image import predict_image
from utils.process_video import predict_video
from utils.process_text import predict_text
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "<h3>No file uploaded</h3><a href='/'>Back</a>"

    file = request.files['file']
    if file.filename == '':
        return "<h3>No selected file</h3><a href='/'>Back</a>"

    file_type = request.form.get('file_type')
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        if file_type == 'image':
            result = predict_image(filepath)
        elif file_type == 'video':
            result = predict_video(filepath)
        elif file_type == 'text':
            result = predict_text(filepath)
        else:
            result = "Invalid type selected."
    except Exception as e:
        result = f"Error while processing: {e}"

    return f"""
        <h2>Detection Result</h2>
        <p><strong>File Type:</strong> {file_type.capitalize()}</p>
        <p><strong>Result:</strong> {result}</p>
        <a href='/'>🔙 Back to Home</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
