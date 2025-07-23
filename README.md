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

✏️ Algorithm (Step-by-Step Process)

1.Start the program by launching the Flask web server.
2.When a user visits the root URL (/), render the chatbot interface using HTML and CSS.
3.The chatbot UI waits for the user to type a message into the input field.
4.Once the user submits a message, JavaScript sends a POST request to the Flask server (/get).
5.The Flask server receives the message and converts it to lowercase for easier comparison.
6.The backend checks the message for known keywords like "faculty", "fees", "course", "location", etc.
7.Based on the keyword matched, the server uses a series of if-elif conditions to determine the appropriate response.
8.The response is formatted using HTML tags like <br> or <ol> to make it clear and readable.
9.On the frontend, a typing animation with dots is shown to simulate a delay.
10.After a few seconds, the animation is replaced with the actual response, which is displayed in the chat box.
11.The chatbot then waits for the next message from the user, continuing the loop.

2.1This step-by-step process makes the chatbot user-friendly, realistic, and responsive to multiple kinds of queries.







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


Powered By Doutly.com
