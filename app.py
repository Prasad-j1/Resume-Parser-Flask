import os
from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
from Resume_Parser_App import ResumeParserApp

# ================= CONFIG =================

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png", "bmp", "tiff"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ================= HELPER =================

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ================= MAIN ROUTE =================

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        # Clear old uploads
        for f in os.listdir(UPLOAD_FOLDER):
            os.remove(os.path.join(UPLOAD_FOLDER, f))

        uploaded_files = request.files.getlist("resumes")

        if not uploaded_files or uploaded_files[0].filename == "":
            return render_template("index.html", results=None)

        # Save uploaded files
        for file in uploaded_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(file_path)

        try:
            # Run parser
            parser = ResumeParserApp(UPLOAD_FOLDER)
            parsed_data = parser.run()   # MUST return list of dictionaries

            return render_template("index.html", results=parsed_data)

        except Exception as e:
            print("Error occurred:", e)
            return render_template("index.html", results=None)

    return render_template("index.html", results=None)


# ================= DOWNLOAD ROUTE =================

@app.route("/download")
def download():

    file_path = "Parsed_Resumes.xlsx"

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return redirect("/")


# ================= RUN APP =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)