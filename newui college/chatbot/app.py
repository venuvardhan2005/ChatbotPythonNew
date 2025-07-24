from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    q = request.json["msg"].lower()

    if "course" in q or "programme" in q:
        return jsonify({
            "reply": """
            KISHKINDA UNIVERSITY offers:<br>
            1. B.Tech (CSE, ECE, EEE, Pharma)<br>
            2. BBA<br>
            3. MBA<br>
            4. MCA<br>
            5. M.Tech<br>
            6. BCA<br>
            7. B.Com<br>
            ...and more.
            """
        })
    elif "hi" in q or "Hi" in q:
        return jsonify({"reply":"Hi , Welcome To The KISHKINDA UNIVERSITY CHATBOT"})
    elif "eligibility" in q:
        return jsonify({"reply": "UG: 45% in 12th with KCET/JEE; PG: 50% in graduation with entrance like PGCET/CAT."})
    elif "about college" in q:
        return jsonify({"reply": "Basavarajeswari Group of Institutions under TEHRD Trust® governs KISHKINDA UNIVERSITY, a private state university in Karnataka recognized by Karnataka State Act No. 20 of 2023."})
    elif "fee" in q:
        return jsonify({"reply": "Fees vary by course. Please check the admissions section or contact admin for details."})
    elif "hostel" in q or "transport" in q:
        return jsonify({"reply": "Yes! KISHKINDA UNIVERSITY provides separate hostels for boys and girls, and local transport facilities."})
    elif "placement" in q:
        return jsonify({"reply": "KISHKINDA UNIVERSITY has 854+ placements in 2023-24. Avg package: ₹4.5 LPA, Highest: ₹19.5 LPA."})
    elif "recruiter" in q or "campus placements" in q:
        return jsonify({"reply": "Top recruiters: TCS, Infosys, Wipro, Tech Mahindra, Accenture, Cognizant, HDFC, and more."})
    elif "location" in q or "campus" in q:
        return jsonify({
        "reply": """
        KISHKINDA UNIVERSITY is located in:<br>
        📍 Hanumanahalli, Ballari District, Karnataka.<br>
        <a href='https://maps.app.goo.gl/8V76ivLAzkYwc2mt8' target='_blank'>📌 View on Google Maps</a>
        """
    })   
    elif "scholarship" in q:
        return jsonify({"reply": "Yes, KISHKINDA UNIVERSITY offers merit-based and need-based scholarships. Check the official site."})
    elif "infastructure" in q or "lab" in q or "facility" in q:
        return jsonify({"reply": "Modern labs, smart classrooms, Wi-Fi campus, digital library, auditorium, gym, sports & more."})
    elif "contact" in q or "phone" in q:
        return jsonify({"reply": "Call the admission cell: +91-94490-86655 or email info@kishkindauniversity.edu.in"})
    elif "ugc" in q or "aicte" in q or "approval" in q:
        return jsonify({"reply": "Yes, Kishkinda University is recognized by UGC and has AICTE-approved programs."})
    elif "international" in q or "collaboration" in q or "global" in q:
        return jsonify({"reply": "KISHKINDA UNIVERSITY collaborates with global universities for student exchange and research programs."})
    elif "how many" in q and "branches" in q:
        return jsonify({"reply": "Kishkinda University has over 6 academic branches including Engineering, Management, Commerce, Pharmacy, Computer Applications, and Science."})
    elif "undergraduate" in q or "ug courses" in q:
        return jsonify({"reply": "UG courses include B.Tech (CSE, EEE, ECE, Pharma), BCA, BBA, and B.Com."})
    elif "postgraduate" in q or "pg courses" in q:
        return jsonify({"reply": "PG courses include MBA, MCA, and M.Tech in various specializations."})
    elif "specialization" in q and "b.tech" in q:
        return jsonify({"reply": "B.Tech specializations include CSE, AI & ML, EEE, ECE, and Pharmaceutical Engineering."})
    elif "department" in q or "b.tech" in q:
        return jsonify({"reply": "CSE, EEE, EC, BCA, MCA, MBA, and M.Tech departments are available."})
    elif "about cse" in q or "cse" in q:
        return jsonify({"reply": "There are totally 240 seats and the fee is ₹1,25,000."})
    elif "diploma" in q or "certification" in q:
        return jsonify({"reply": "Currently, KISHKINDA UNIVERSITY focuses on full-time degree programs. For diploma options, check with the admissions cell."})
    elif "integrated" in q or "dual degree" in q:
        return jsonify({"reply": "Yes! KISHKINDA UNIVERSITY offers integrated BBA + MBA and other programs. Contact admissions for more info."})
    elif "pharmacy" in q or "pharma" in q:
        return jsonify({"reply": "KISHKINDA UNIVERSITY offers B.Tech in Pharmaceutical Engineering and research opportunities in the pharma domain."})
    elif "faculty" in q or "professor" in q or "teacher" in q:
        return jsonify({
        "reply": """
        Our faculty members are:
        <ol>
          <li>Dr. Rajshree V. Bivadar (HOD)</li>
          <li>Dr. Shivu Kumar</li>
          <li>Dr. Mivakeshi</li>
          <li>Mr. Vannur Swamy</li>
          <li>Mr. Mujeeb Ansari</li>
          <li>Mrs. Anitha Jyothi</li>
          <li>Mrs. Deepa T</li>
          <li>Mr. Quadri</li>
          <li>Mr. Ganesh</li>
          <li>Mrs. Ashwini</li>
        </ol>
        """
    })
    elif "extra activities" in q or "Extra Activities" in q:
        return jsonify({"reply": "1. Clubs and Chapters\n2. Tech Workshops\n3. SDP and FDP\n4. Internships and Scholarships\n5. Industrial Visits"})
    elif "admission section" in q:
        return jsonify({"reply": "1. CSE - 240 seats, ₹1,25,000 fees\n2. EC - 120 seats, ₹1,25,000 fees"})
    else:
        return jsonify({"reply": "Sorry, I didn’t understand that. Please ask about courses, placements, hostel, fees, etc."})

if __name__ == "__main__":
    app.run(debug=True)
