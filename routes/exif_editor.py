from flask import Blueprint, render_template, request, jsonify
import piexif
from PIL import Image
import io
import base64

exif_editor_bp = Blueprint('exif_editor', __name__)

# Display the EXIF Editor page
@exif_editor_bp.route('/', methods=['GET'])
def edit_exif_page():
    return render_template('edit_exif.html')

# Modify EXIF Data
@exif_editor_bp.route('/modify', methods=['POST'])
def edit_exif():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    image_file = request.files['image']
    new_exif_data = request.form.get('exif_data')

    try:
        image = Image.open(image_file)
        exif_dict = piexif.load(image.info.get("exif", b""))

        if new_exif_data:
            exif_dict["0th"][piexif.ImageIFD.Artist] = new_exif_data.encode()

        exif_bytes = piexif.dump(exif_dict)
        img_io = io.BytesIO()
        image.save(img_io, format="jpeg", exif=exif_bytes)
        img_io.seek(0)

        img_base64 = base64.b64encode(img_io.getvalue()).decode()

        return jsonify({'message': 'EXIF updated successfully', 'image': img_base64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
