🛒 Smart Grocery Shopping Assistant

A rule-based Python assistant that helps users manage grocery lists, suggests healthier alternatives, predicts missing items based on shopping habits, and provides expiry reminders using purchase history.

📌 Project Overview
The Smart Grocery Shopping Assistant is a simple AI-driven console application built using Python.
It demonstrates practical use of:
✔ Rule-based reasoning
✔ Data-driven predictions
✔ Interactive decision making
✔ Expiry tracking logic

The project is designed as part of an academic mini-project to show how basic AI concepts can be applied in everyday contexts.

🎯 Key Features
📝 1. Grocery List Management
Add items
View current list
Remove purchased items
Maintain clean interaction UI

🥗 2. Healthier Alternative Suggestions

The system automatically suggests healthier substitutions, e.g.:
Unhealthy Item	Recommended Alternative
White Bread	Brown Bread
Sugar	Brown Sugar
Full Cream Milk	Low Fat Milk
Instant Noodles	Whole Wheat Pasta
User can choose whether to replace the original item.

🔮 3. Smart Rule-Based Predictions
The assistant predicts what items the user may need again using rules like:
✔ Weekly purchase cycle (items bought 5–9 days ago)
✔ Staple items not bought in 14+ days
✔ Suggesting essentials for first-time users

⏰ 4. Expiry Reminder System
Uses shelf-life values to warn users when items are:
⚠️ About to expire
❌ Already expired
Example warning:
⚠️ 'Milk' will expire in 1 day(s). (Expiry: 2025-12-05)

📜 5. Purchase History Tracking

The system logs:
Item name
Date of purchase
Calculated expiry date
This helps generate predictions and reminders.

🧠 System Architecture

The project consists of:
User interaction layer (menu-driven CLI)

AI logic modules:
Suggestion engine
Alternative recommendation engine
Expiry tracking system
Purchase history manager
Grocery list manager
Simple in-memory data storage (lists + dictionaries)
Diagrams are included in the repository.

🛠️ Technologies Used
Python 3.x
Rule-based reasoning
Date/time calculations (via datetime)
Console-based interaction

▶️ How to Run the Program

Clone the repository:
git clone https://github.com/ShasmaAfs/Smart-Grocery-Shopping-Assistant.git

Navigate to the project folder:
cd Smart-Grocery-Shopping-Assistant

Run the script:
python smart_grocery_assistant.py

📁 Folder Structure
Smart-Grocery-Shopping-Assistant/
│
├── smart_grocery_assistant.py     # Main Python script
├── README.md                      # Project documentation
├── architecture_dark.html         # Architecture diagram (interactive)
└── flowchart_dark.html            # Flowchart diagram (interactive)

📚 Academic Requirements Covered

This project fully satisfies Scenario 01:

✔ Predict missing items using rule-based reasoning
✔ Suggest healthier alternatives
✔ Provide expiry reminders
✔ Use a simple interaction interface

Ideal for mini-projects, practical exams, and viva demonstrations.

🌟 Future Improvements

Suggested enhancements:

Machine learning for improved predictions

Voice assistant integration

Real-time notifications

Persistent database (SQLite/MongoDB)

GUI or mobile app interface

✨ Author
A.L.F. Siyasath Shasma
