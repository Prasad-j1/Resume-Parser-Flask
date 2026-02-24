📄 AI Resume Parser (Flask Web App)


🚀 Project Overview
This project is a Flask-based web application that extracts structured information from unstructured resume documents (PDF & image formats) using:

OCR (Tesseract)

NLP (spaCy Named Entity Recognition)

Regex-based data extraction

Pandas for Excel export

The system processes single or multiple resumes and generates structured output including:

Name

Email

Phone

Gender

Skills

Experience

🛠 Tech Stack
Python

Flask

spaCy (NLP)

Tesseract OCR

pdf2image

Pandas

Bootstrap 5 (Frontend)

🧠 Architecture
Upload resumes via web UI

Convert PDF to images (if required)

Extract text using OCR

Apply NLP & Regex for structured extraction

Display results dynamically

Export results to Excel

📂 Project Structure
app.py
Resume_Parser_App.py
Data_Extractor.py
OCR_Engine.py
PDF_Handler.py
Data_Storage.py
templates/
static/
requirements.txt
⚙️ Installation
git clone https://github.com/YOUR_USERNAME/AI-Resume-Parser-Flask.git
cd AI-Resume-Parser-Flask
pip install -r requirements.txt
python app.py
Open:

http://127.0.0.1:5000
🌐 Deployment
(Will be updated after deployment)

📌 Future Improvements
Skill frequency dashboard

Resume ranking system

Experience scoring

Admin authentication

Cloud storage integration

👨‍💻 Author
Prasad Joshi.
