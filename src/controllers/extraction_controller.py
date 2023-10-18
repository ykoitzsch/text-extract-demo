from flask import Blueprint, request, jsonify
from src.services.extraction_service import ExtractionService
import os

extraction_blueprint = Blueprint('extraction', __name__)
service = ExtractionService()


@extraction_blueprint.route('/extract_from_pdf', methods=['POST'])
def extract_text():
    file = request.files.get('pdf_file')

    if file and file.filename.endswith('.pdf'):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        temp_dir = os.path.join(base_dir, '..', 'resources', 'temp')
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)
        doc_pdf = service.extract_from_pdf(file_path=file_path)

        os.remove(file_path)

        return jsonify({"content": doc_pdf.content})

    return jsonify({"error": "No PDF file provided or invalid file type"}), 400
