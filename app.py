from flask import Flask, request, jsonify
from resume_parser import extract_resume_data
from job_matcher import match_resume_with_job
from logger import log_info, log_error

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_resume():
    """API endpoint to upload a resume and compare it with job description."""
    try:
        file = request.files["resume"]
        resume_text = file.read().decode("utf-8")
        job_desc = request.form.get("job_description", "")

        parsed_data = extract_resume_data(resume_text)
        match_score = match_resume_with_job(parsed_data, job_desc)

        response = {
            "resume_data": parsed_data,
            "match_score": f"{match_score:.2f}%"
        }

        log_info(f"API Response: {response}")
        return jsonify(response)

    except Exception as e:
        log_error(f"Error in API: {str(e)}")
        return jsonify({"error": "Failed to process request"}), 500

if __name__ == "__main__":
    app.run(debug=True)
