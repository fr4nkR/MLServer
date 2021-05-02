import os
from flask import Flask, render_template, request, redirect, flash, url_for
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()  # take environment variables from .env.
BASE_PATH = os.getenv('BASE_PATH')
app = Flask(__name__)
app.secret_key = b'secret'

# here change it for the actual file extension for ML models for torch
# BASE_PATH = os.path.abspath()
ALLOWED_EXTENSION = {'txt', 'zip', 'gz', 'pth'}

def allowed_files(filename: str) -> bool :
    # print(filename)
    # print('.' in filename and filename.rsplit('.',1)[1].lower{} in ALLOWED_EXTENSION)
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files.get('file')

        if file.filename == '':
            flash('No file was selected')
            return redirect(request.url)

        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(BASE_PATH, filename))
            print(os.path.join(BASE_PATH, filename))
            flash('File uploaded successfully')
            return redirect(url_for('download'))
    return render_template('index.html')

# @app.route('/', methods=['GET'])
# def train_my_model():
#     if 

# @app.route('/', methods=['GET'])
# def upload_data():

@app.route('/download', methods=['GET'])
def download():
    return 'Download Page'

# if __name__ == '__main__':
#     app.run(debug=True)

