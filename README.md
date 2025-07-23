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

✏️ Algorithm

1.Begin the program by launching the Flask web server.

2.When the root URL (/) is visited, load the HTML + CSS interface.

3.Wait for the user to type a message in the chat input field.

4.Capture that message and send it to the Flask backend using a POST request (/get).

5.In the Flask app, convert the message to lowercase.

6.Check if the message contains known keywords like "faculty", "course", "fees", etc.

7.Match the message using if-elif conditions to return a suitable predefined response.

8.Use HTML tags (like <br> or <ol>) to format the response if needed.

9.In the frontend, show a typing animation with three dots to simulate delay.

10.After a short delay, display the bot's final message in the chat window.

11.Return to step 3 to handle the next message from the user.





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
