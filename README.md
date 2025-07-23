# ChatbotPythonNew

# 🤖 Kishkinda University Chatbot (Web Version)

A responsive, animated chatbot interface for **Kishkinda University** that provides instant answers to common student queries — such as faculty, courses, location, fees, and more. Built using **HTML, CSS, and Python (Flask)**, it simulates a helpful university assistant with a visually appealing interface and splash loading animation.

---

## 🌟 Features

* Splash screen with animated logo.
* Chatbot with smooth UI and golden bordered replies.
* Loading dots before showing response (for realism).
* Mobile responsive layout.
* Pre-defined intelligent answers for university-related queries.
* Auto-scroll chat with avatars and styled messages.

---

## 🔁 Flowchart (with Symbols)

text
┌────────────────────┐
│  User Sends Query  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────────────┐
│  Frontend sends POST /get  │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│ Flask backend receives msg │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│ Check keywords in message  │
└─────────┬──────────────────┘
          │        ┌───────────────┐
          │  Yes → │ Return reply  │
          │        └────┬──────────┘
          │             │
          ▼             ▼
  No Match → ┌────────────────────────┐
             │ Return default message│
             └──────────┬─────────────┘
                        │
                        ▼
           ┌────────────────────────────┐
           │ Frontend shows loading (...)│
           └────────────┬───────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │ Display bot response on screen │
        └────────────────────────────────┘




## ❓ Questions Answered by Chatbot

* Courses / Programmes offered
* Faculty / Professors
* College Overview
* Eligibility for UG & PG
* Hostel & Transport Facilities
* Fee Details
* Placement Stats
* Recruiters & Companies
* Location with Google Map
* Scholarships
* Infrastructure / Labs
* Contact Information
* UGC / AICTE Approval
* International Collaborations
* No. of Branches
* UG Courses
* PG Courses
* B.Tech Specializations
* Departments Offered
* About CSE
* Diploma / Certifications
* Integrated / Dual Degree Programs
* Pharmacy Department
* Extra Activities
* Admission Section

---

## 🚀 How to Run This Project

1. **Install Python & Flask**:

bash
pip install flask


2. **Project Structure**:


project-folder/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
└── README.md


3. Run the Flask App:

bash
python app.py

4. Open in Browser**:
http://localhost:5000
Now chat with Kishkinda University bot!
Feel free to customize the UI, responses, or extend the logic to use a proper NLP backend or database.
