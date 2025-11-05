# chatbot_app.py
# -*- coding: utf-8 -*-
import streamlit as st
import random

# --- List of jokes ---
jokes = [
    "Why don't skeletons fight each other? They don't have the guts!",
    "What did the zero say to the eight? Nice belt!",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out."
]

# --- Study resources ---
study_resources = {
    "math": [
        "Khan Academy: https://www.khanacademy.org",
        "Coursera - Mathematics: https://www.coursera.org/courses?query=mathematics",
        "YouTube - 3Blue1Brown: https://www.youtube.com/c/3blue1brown"
    ],
    "python": [
        "Python Official Documentation: https://docs.python.org/3/",
        "Real Python: https://realpython.com",
        "FreeCodeCamp Python Tutorials: https://www.freecodecamp.org/news/python-tutorial-for-beginners/"
    ],
    "history": [
        "History Channel: https://www.history.com",
        "Khan Academy - History: https://www.khanacademy.org/humanities",
        "BBC History: https://www.bbc.co.uk/history"
    ],
    "science": [
        "NASA's Education Portal: https://www.nasa.gov/education",
        "National Geographic: https://www.nationalgeographic.com",
        "Coursera - Science Courses: https://www.coursera.org/courses?query=science"
    ]
}

# --- Math solver ---
def solve_math(problem):
    try:
        return str(eval(problem))
    except:
        return "Sorry, I couldn't solve that. Please make sure your problem is written correctly."

# --- Disease prediction ---
def predict_disease(symptoms):
    diseases = {
        "fever": "You may have a cold or flu. Please consult a doctor.",
        "cough": "This could be a sign of a respiratory infection, such as the flu or common cold.",
        "headache": "A headache could be a sign of stress, dehydration, or a common cold.",
        "fatigue": "Fatigue can be a symptom of stress, sleep deprivation, or several other conditions.",
        "sore throat": "A sore throat could indicate a cold or strep throat. It might be wise to see a doctor.",
        "nausea": "Nausea can be associated with many issues, including food poisoning, stomach flu, or more severe conditions.",
        "shortness of breath": "This could be a sign of respiratory issues such as asthma, pneumonia, or a heart condition. Please consult a doctor.",
        "diarrhea": "Diarrhea can be a symptom of food poisoning, a viral infection, or digestive issues.",
        "vomiting": "Vomiting could indicate a stomach infection, food poisoning, or even stress-related conditions.",
        "chills": "Chills are often associated with infections such as the flu, cold, or a fever.",
        "muscle pain": "Muscle pain could be a sign of overuse, an injury, or could be related to conditions like the flu.",
        "dizziness": "Dizziness can be caused by dehydration, low blood pressure, or even an ear infection.",
        "rash": "A rash could be a sign of an allergic reaction, infection, or skin condition. It’s best to consult a healthcare provider.",
        "runny nose": "A runny nose is often linked to the common cold, flu, or allergies."
    }

    prediction = []
    for symptom in symptoms:
        symptom = symptom.strip().lower()
        if symptom in diseases:
            prediction.append(diseases[symptom])
        else:
            prediction.append(f"Sorry, I don't recognize the symptom: {symptom}")

    return "\n".join(prediction)

# --- Chit-chat ---
def chit_chat(user_input):
    chit_chat_responses = [
        "I’m doing great, thanks for asking!",
        "Not much, just chatting with you!",
        "I’m just a chatbot, but I love talking to you!",
        "How about you? What's up?",
        "I could talk all day, but I’m still learning!"
    ]
    return random.choice(chit_chat_responses)

# --- Study resources ---
def provide_study_resources(subject):
    subject = subject.lower()
    if subject in study_resources:
        return "\n".join(study_resources[subject])
    else:
        return f"Sorry, I don't have study resources for {subject}. But I can help you with some general topics!"

# --- Main respond function ---
def respond(user_input):
    user_input_lower = user_input.lower().strip()

    # Polite replies
    if user_input_lower in ["okay", "ok", "alright"]:
        return "I’m glad I could help! If there’s anything more I can do, just let me know."
    elif user_input_lower in ["thank you", "thanks", "thx"]:
        return "You’re welcome! 😊"

    # Feature info
    elif "what can you do" in user_input_lower or "features" in user_input_lower or "what else" in user_input_lower:
        return (
            "I can help you with:\n"
            "- Answering general questions and chit-chat\n"
            "- Telling jokes 😄\n"
            "- Solving basic math problems\n"
            "- Providing study resources (Math, Python, History, Science)\n"
            "- Giving basic disease prediction based on symptoms\n"
        )

    # Jokes
    elif "joke" in user_input_lower:
        return random.choice(jokes)

    # Math
    elif any(char.isdigit() for char in user_input_lower):
        return solve_math(user_input_lower)

    # Study resources
    elif "study" in user_input_lower or "resources" in user_input_lower:
        for sub in ["math", "python", "history", "science"]:
            if sub in user_input_lower:
                return provide_study_resources(sub)
        return "Please specify the subject (math, python, history, science)."

    # Disease prediction
    elif "symptoms" in user_input_lower or "predict" in user_input_lower:
        symptoms = user_input_lower.split("symptoms")[-1].strip()
        symptoms = symptoms.split(",")
        return predict_disease(symptoms)

    # Greetings & chit-chat
    elif user_input_lower in ["hello", "hi", "hey", "greetings"]:
        return random.choice(["Hello!", "Hi there!", "Hey!", "Greetings!"])
    elif "how are you" in user_input_lower:
        return "I’m just a bot, but I’m doing well! How about you?"
    elif "what's up" in user_input_lower or "whats up" in user_input_lower:
        return chit_chat(user_input_lower)

    # Farewell
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Goodbye! It was nice talking to you!"

    # Default fallback
    else:
        return chit_chat(user_input_lower)

# --- Streamlit Web Interface ---
st.title("ChatBuddy 🤖")

# Keep chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Text input
user_input = st.text_input("You:")

if user_input:
    response = respond(user_input)
    st.session_state.messages.append({"user": user_input, "bot": response})

# Display chat
for msg in st.session_state.messages:
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**Bot:** {msg['bot']}")
