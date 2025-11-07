# streamlit_app.py
# -*- coding: utf-8 -*-
import streamlit as st
import random
import re  # For regex symptom detection

# --- List of jokes ---
jokes = [
    "Why did the computer go to the doctor? It caught a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the math book look sad? It had too many problems.",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the coffee file a police report? It got mugged!",
    "Why was the equal sign so humble? Because it knew it wasn’t less than or greater than anyone else.",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
    "Why did the cookie go to the hospital? Because it felt crummy!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the physics teacher break up with the biology teacher? There was no chemistry.",
    "Why did the computer keep sneezing? It had too many tabs open.",
    "Why was the cell phone wearing glasses? It lost its contacts.",
    "Why did the programmer quit his job? He didn’t get arrays.",
    "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself.",
    "Why did the PowerPoint cross the road? To get to the other slide.",
    "Why did the picture go to jail? Because it was framed!",
    "Why was the belt arrested? For holding up a pair of pants.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "Why was the broom late? It overswept.",
    "Why did the golfer bring extra pants? In case he got a hole in one.",
    "Why did the mushroom go to the party? Because he was a fungi.",
    "Why don’t eggs tell jokes? They might crack up.",
    "Why did the kid bring a ladder to school? Because he wanted to go to high school.",
    "Why was the computer cold? It left its Windows open.",
    "Why did the man put his money in the freezer? He wanted cold hard cash.",
    "Why did the calendar go to therapy? Its days were numbered.",
    "Why don’t oysters share their pearls? Because they’re shellfish.",
    "Why did the man run around his bed? Because he was trying to catch up on sleep.",
    "Why did the smartphone go to school? It wanted to be smarter.",
    "Why did the student bring a pencil to the party? In case he wanted to draw some attention.",
    "Why did the web developer go broke? Because he used up all his cache.",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why did the teacher go to the beach? To test the waters.",
    "Why don’t vampires attack programmers? They don’t like bugs.",
    "Why was the math lecture so long? The professor kept going off on a tangent.",
    "Why did the student eat a light bulb? He wanted to be bright.",
    "Why did the AI break up with its user? It felt used.",
    "Why did the chicken join a band? Because it had the drumsticks.",
    "Why was the robot so bad at soccer? It kept kicking up sparks.",
    "Why did the grape stop in the middle of the road? It ran out of juice.",
    "Why did the skeleton go to the party alone? He had no body to go with.",
    "Why don’t cats play poker in the jungle? Too many cheetahs.",
    "Why was the broom so happy? It swept the competition away.",
    "Why did the teacher wear sunglasses? Because her students were so bright.",
    "Why did the physics book look sad? Because it had so much potential.",
    "Why did the computer sit on a clock? To catch up on its time.",
    "Why did the banana go to the doctor? It wasn’t peeling well.",
    "Why did the music teacher go to jail? Because she got caught with the treble.",
    "Why was the math teacher suspicious of prime numbers? They were always odd."
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

# --- Main respond function with auto symptom detection ---
def respond(user_input):
    user_input_lower = user_input.lower().strip()

    # Polite replies
    if user_input_lower in ["okay", "ok", "alright","okie","Ok","acha ok"]:
        return "I’m glad I could help! If there’s anything more I can do, just let me know:)"
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

    # Disease prediction — auto detect symptoms in sentence
    symptoms_list = ["fever", "cough", "headache", "fatigue", "sore throat",
                     "nausea", "shortness of breath", "diarrhea", "vomiting",
                     "chills", "muscle pain", "dizziness", "rash", "runny nose"]
    
    # Detect any symptom mentioned anywhere in the sentence
    detected_symptoms = [sym for sym in symptoms_list if re.search(r'\b' + re.escape(sym) + r'\b', user_input_lower)]
    
    if detected_symptoms:
        return predict_disease(detected_symptoms)

    # Greetings & chit-chat
    elif user_input_lower in ["hello", "hi", "hey", "greetings","assalamualaikum","aslkm","asak","assalamu alaikum","namaste"]:
        return random.choice(["Hello!", "Hi there!", "Hey!", "Greetings!","waleikumassalam","walkm","wslkm","walikum salam","walaikumassalam","namaste"])
    elif "how are you" in user_input_lower:
        return "I’m just a bot, but I’m doing well! How about you?"
    elif "what's up" in user_input_lower or "whats up" in user_input_lower:
        return chit_chat(user_input_lower)
    elif "what's your name" in user_input_lower or "whats your name" in user_input_lower:
        return "I am ChatBuddy 🤖, your friendly chatbot!"
    

    # Farewell
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Goodbye! It was nice talking to you!"

    # Default fallback
    else:
        return chit_chat(user_input_lower)

# --- Streamlit Web Interface ---
st.title("ChatBuddy 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages as chat bubbles
for message in st.session_state.messages:
    with st.chat_message("user"):
        st.markdown(message["user"])
    with st.chat_message("bot"):
        st.markdown(message["bot"])

# Input for new message
if user_input := st.chat_input("Type your message here..."):
    # Generate bot response
    response = respond(user_input)
    # Store in session
    st.session_state.messages.append({"user": user_input, "bot": response})
    # Display latest messages
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("bot"):
        st.markdown(response)
# 👇 Display chatbot capabilities at the bottom of the app
st.markdown("---")
st.subheader("💡 What I Can Do")
st.markdown("""
Here are a few things you can try asking me:
- 😂 **Tell me a joke**
- ➕ **Solve simple math problems** (like `12 + 8` or `9 * 7`)
- 📚 **Give study resources** (for Math, Python, or Science)
- 🩺 **Predict possible diseases** (e.g., “I have fever and sore throat”)
- 💬 **Casual chat** (“Hi”, “Thanks”, etc.)
""")
