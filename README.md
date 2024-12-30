# 📄 Resume Analyzer

## Overview

The Resume Analyzer is a Python application that processes resumes in `.txt` or `.pdf` format to extract key details like name, skills, experience, and education.

## Features

- Add and view resumes.
- Extract and display key details.
- Search for specific skills or experiences.

## Technologies

- Python 3
- PyPDF2 (for PDF handling)
- spaCy, nltk (for text processing)

## Installation

```bash
# 1. Clone the repository:
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

# 2. Create a virtual environment:
# On Linux/Mac:
python3 -m venv venv

# On Windows:
python -m venv venv

# 3. Activate the virtual environment:
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 4. Install dependencies:
pip install -r requirements.txt

# 5. Run the Resume Analyzer:
python analyze_resume.py --file path_to_resume_file
