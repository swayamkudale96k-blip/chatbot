 import json
import random
import pickle
import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ============================================
# COLLEGE HELPDESK AI CHATBOT
# ============================================

# Dataset (Intents + Responses)

data = {
    "intents": [

        {
            "tag": "admission",
            "patterns": [
                "How can I apply for admission?",
                "Admission process",
                "Eligibility criteria",
                "Admission last date",
                "How to take admission",
                "Admission details"
            ],
            "responses": [
                "You can apply online through the college admission portal.",
                "Admissions are open from June to August.",
                "Please visit the admission office for detailed guidance."
            ]
        },

        {
            "tag": "exam",
            "patterns": [
                "When are exams?",
                "Exam timetable",
                "Hall ticket download",
                "Semester exam dates",
                "Exam schedule",
                "Where can I get hall ticket?"
            ],
            "responses": [
                "Exam schedules are available on the examination portal.",
                "Hall tickets can be downloaded 10 days before exams.",
                "Please check the exam notice board regularly."
            ]
        },

        {
            "tag": "library",
            "patterns": [
                "Library timing",
                "Is library open?",
                "Where is library?",
                "Library hours",
                "Library information"
            ],
            "responses": [
                "The library is open from 8 AM to 8 PM.",
                "The library is located near Block A.",
                "Students can borrow up to 3 books at a time."
            ]
        },

        {
            "tag": "hostel",
            "patterns": [
                "Hostel fees",
                "Hostel availability",
                "Boys hostel",
                "Girls hostel",
                "Hostel details"
            ],
            "responses": [
                "Hostel fees are ₹45,000 per year.",
                "Separate hostel facilities are available for boys and girls.",
                "Hostel rooms are allotted based on availability."
            ]
        },

        {
            "tag": "fees",
            "patterns": [
                "Course fees",
                "Tuition fees",
                "Fee structure",
                "College fees",
                "Semester fees"
            ],
            "responses": [
                "Fee details are available in the accounts section.",
                "Tuition fees depend on the selected course.",
                "You can also download the fee structure from the college website."
            ]
        },

        {
            "tag": "canteen",
            "patterns": [
                "Canteen timing",
                "Food facility",
                "College canteen",
                "Is canteen available?"
            ],
            "responses": [
                "The college canteen is open from 9 AM to 5 PM.",
                "Healthy and affordable meals are available in the canteen."
            ]
        }

    ]
}

# ============================================
# TRAINING THE MODEL
# ============================================

sentences = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(intent["tag"])

# Convert text into numerical vectors
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# ============================================
# LOAD MODEL
# ============================================

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ============================================
# CHATBOT INTERFACE
# ============================================

print("======================================")
print("     COLLEGE HELPDESK AI CHATBOT")
print("======================================")
print("Ask questions regarding:")
print("- Admissions")
print("- Exams")
print("- Hostel")
print("- Library")
print("- Fees")
print("- Campus Facilities")
print("--------------------------------------")
print("Type 'quit' to exit")
print("======================================")

while True:

    user_input = input("\nYou: ")

    # Exit condition
    if user_input.lower() == "quit":
        print("Bot: Thank you! Have a nice day.")
        break

    # Convert user input to vector
    X_input = vectorizer.transform([user_input])

    # Predict intent
    prediction = model.predict(X_input)[0]

    # Find matching response
    response_found = False

    for intent in data["intents"]:

        if intent["tag"] == prediction:

            response = random.choice(intent["responses"])

            print("Bot:", response)

            response_found = True
            break

    # Fallback response
    if not response_found:
        print("Bot: Sorry, I couldn't understand your question.")

# ============================================
# END OF PROGRAM
# ============================================
