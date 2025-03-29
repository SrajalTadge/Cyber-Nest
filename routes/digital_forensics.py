from flask import Blueprint, request, jsonify, render_template
from utils.exif_extraction import extract_exif

digital_forensics_bp = Blueprint('digital_forensics', __name__, url_prefix='/digital-forensics')

@digital_forensics_bp.route('/', methods=['GET', 'POST'])
def digital_forensics():
    if request.method == 'POST':
        if 'image_path' not in request.files:
            return jsonify({"error": "No file part"}), 400
        image_file = request.files['image_path']
        try:
            exif_data = extract_exif(image_file)
            return jsonify({"exif_data": exif_data})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return render_template('digital_forensics.html')
