from flask import Blueprint, request, jsonify, render_template
from utils.base_detection import base_detection

ctf_helpers_bp = Blueprint('ctf_helpers', __name__, url_prefix='/ctf-helpers')

@ctf_helpers_bp.route('/', methods=['GET', 'POST'])
def ctf_helpers():
    if request.method == 'POST':
        data = request.get_json()
        input_data = data.get('input_data', '')
        detected_bases = base_detection(input_data)
        return jsonify({"detected_bases": detected_bases})
    return render_template('ctf_helpers.html')
