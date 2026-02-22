from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file.save(f'uploads/{file.filename}')
    
    return jsonify({"message": f"File '{file.filename}' uploaded successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=1583)

