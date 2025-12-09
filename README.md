# 🛒 Smart Grocery Shopping Assistant  
A rule-based Python assistant that helps users manage grocery lists, suggests healthier alternatives, predicts missing items based on shopping habits, and provides expiry reminders using purchase history.

---

## 📌 Project Overview

The **Smart Grocery Shopping Assistant** is a simple AI-driven console application built using Python.  
It demonstrates practical use of:

- ✔ Rule-based reasoning  
- ✔ Data-driven predictions  
- ✔ Interactive decision making  
- ✔ Expiry tracking logic  

This project was developed as part of an academic mini-project to demonstrate how basic AI concepts can solve real-life problems.

---

## 🎯 Key Features

### 📝 1. Grocery List Management
- Add items  
- View current list  
- Remove purchased items  
- Simple CLI interface  

---

### 🥗 2. Healthier Alternative Suggestions

Automatically suggests healthier item substitutions:

| Unhealthy Item      | Recommended Alternative |
|---------------------|--------------------------|
| White Bread         | Brown Bread             |
| Sugar               | Brown Sugar             |
| Full Cream Milk     | Low Fat Milk            |
| Instant Noodles     | Whole Wheat Pasta       |

---

### 🔮 3. Smart Rule-Based Predictions

Predicts what items you may need again based on:

- Weekly purchase cycle (items bought 5–9 days ago)  
- Staple items not bought in 14+ days  
- First-time essential item recommendations  

---

### ⏰ 4. Expiry Reminder System

Warns users when items are:

- ⚠️ About to expire  
- ❌ Already expired  

Example reminder:

```
⚠️ 'Milk' will expire in 1 day(s). (Expiry: 2025-12-05)
```

---

### 📜 5. Purchase History Tracking

Records:

- Item name  
- Date of purchase  
- Expiry date  

Used by the suggestion and reminder systems.

---

## 🧠 System Architecture

The system includes:

- **User Interaction Layer** (menu-driven CLI)
- **AI Logic Layer**  
  - Suggestion engine  
  - Healthier alternative engine  
  - Expiry tracking system  
  - Purchase history manager  
  - Grocery list manager  
- **In-memory Data Storage**  
  - Lists & dictionaries  

Interactive architecture and flowchart diagrams (dark theme) are included in:

```
architecture_dark.html  
flowchart_dark.html  
```

---

## 🛠️ Technologies Used

- Python 3.x  
- Rule-based reasoning  
- datetime module  
- Console-based UI  

---

## ▶️ How to Run the Program

### 1. Clone the repository:
```
git clone https://github.com/ShasmaAfs/Smart-Grocery-Shopping-Assistant.git
```

### 2. Navigate into the folder:
```
cd Smart-Grocery-Shopping-Assistant
```

### 3. Run the script:
```
python smart_grocery_assistant.py
```

---

## 📁 Folder Structure

```
Smart-Grocery-Shopping-Assistant/
│
├── smart_grocery_assistant.py     # Main Python script
├── README.md                      # Documentation
├── architecture_dark.html         # Interactive architecture diagram
└── flowchart_dark.html            # Interactive flowchart diagram
```

---

## 📚 Academic Requirements Covered

This project satisfies Scenario 01 requirements:

- ✔ Predict missing items using rule-based reasoning  
- ✔ Suggest healthier alternatives  
- ✔ Provide expiry reminders  
- ✔ Use a simple interaction interface  

---

## 🌟 Future Improvements

- Machine learning–based consumption prediction  
- Voice assistant integration  
- Persistent database storage  
- Mobile app or GUI interface  
- Real product barcode scanning  

---

## ✨ Author

**A.L.F. Siyasath Shasma**  


