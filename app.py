from flask import Flask, render_template
from routes.ctf_helpers import ctf_helpers_bp
from routes.cryptography import cryptography_bp
from routes.digital_forensics import digital_forensics_bp
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from CyberNest!'

if __name__ == '__main__':
    app.run(debug=True)



app = Flask(__name__)
app.config.from_object('config.Config')

# Register Blueprints for modular routes
app.register_blueprint(ctf_helpers_bp)
app.register_blueprint(cryptography_bp)
app.register_blueprint(digital_forensics_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/edit-exif', methods=['GET'])
def edit_exif_page():
    return render_template('edit_exif.html')
@app.route('/edit-exif', methods=['GET'])
def edit_exif_page():
    print("Edit EXIF route accessed")
    return render_template('edit_exif.html')

from flask import Flask, render_template, request, jsonify
import piexif
from PIL import Image
import io
import base64

app = Flask(__name__)

# Digital Forensics - EXIF Metadata Editing
@app.route('/edit-exif', methods=['GET'])
def edit_exif_page():
    return render_template('edit_exif.html')
@app.route('/edit-exif', methods=['POST'])
def edit_exif():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    image_file = request.files['image']
    new_exif_data = request.form.get('exif_data')

    try:
        image = Image.open(image_file)
        exif_dict = piexif.load(image.info.get("exif", b""))

        # Update EXIF data (Example: Changing Artist Tag)
        if new_exif_data:
            exif_dict["0th"][piexif.ImageIFD.Artist] = new_exif_data.encode()

        # Convert back to bytes
        exif_bytes = piexif.dump(exif_dict)

        # Save modified image
        img_io = io.BytesIO()
        image.save(img_io, format="jpeg", exif=exif_bytes)
        img_io.seek(0)

        # Convert image to base64 for display
        img_base64 = base64.b64encode(img_io.getvalue()).decode()

        return jsonify({'message': 'EXIF updated successfully', 'image': img_base64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import piexif
from PIL import Image
import io
import base64

app = Flask(__name__)

# Digital Forensics - EXIF Metadata Editing
@app.route('/edit-exif', methods=['POST'])
def edit_exif():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    image_file = request.files['image']
    new_exif_data = request.form.get('exif_data')

    try:
        image = Image.open(image_file)
        exif_dict = piexif.load(image.info.get("exif", b""))

        # Update EXIF data (Example: Changing Artist Tag)
        if new_exif_data:
            exif_dict["0th"][piexif.ImageIFD.Artist] = new_exif_data.encode()

        # Convert back to bytes
        exif_bytes = piexif.dump(exif_dict)

        # Save modified image
        img_io = io.BytesIO()
        image.save(img_io, format="jpeg", exif=exif_bytes)
        img_io.seek(0)

        # Convert image to base64 for display
        img_base64 = base64.b64encode(img_io.getvalue()).decode()

        return jsonify({'message': 'EXIF updated successfully', 'image': img_base64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from routes.ctf_helpers import ctf_helpers_bp
from routes.cryptography import cryptography_bp
from routes.digital_forensics import digital_forensics_bp
from routes.exif_editor import exif_editor_bp  # Import EXIF Editor Module

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(ctf_helpers_bp)
app.register_blueprint(cryptography_bp)
app.register_blueprint(digital_forensics_bp)
app.register_blueprint(exif_editor_bp)  # Register EXIF Editor Module

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from routes.exif_editor import exif_editor_bp  # Import the new module

# Register EXIF Editor Blueprint
app.register_blueprint(exif_editor_bp, url_prefix='/edit-exif')
