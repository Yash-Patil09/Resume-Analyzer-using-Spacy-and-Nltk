from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    resume_file = request.files['resume']

    if resume_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if resume_file:
        # Save the uploaded file
        filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(filename)

        # Dummy analysis data for testing
        analysis_data = analyze_resume(filename)

        return jsonify({'success': True, 'redirect': '/result'})

@app.route('/result')
def result():
    # Dummy data for result rendering
    analysis_data = {
        'field': 'Data Science',
        'matched_skills': ['Python', 'Machine Learning', 'SQL'],
        'internships': [{'type': 'Software Engineer', 'description': 'Developed ML models'}],
        'suggestions': 'Focus on deep learning and NLP.'
    }

    return render_template('result.html', analysis=analysis_data)

def analyze_resume(resume_path):
    # Placeholder for actual analysis logic
    return {
        'field': 'Data Science',
        'matched_skills': ['Python', 'Machine Learning', 'SQL'],
        'internships': [{'type': 'Software Engineer', 'description': 'Developed ML models'}],
        'suggestions': 'Focus on deep learning and NLP.'
    }

if __name__ == '__main__':
    app.run(debug=True)
