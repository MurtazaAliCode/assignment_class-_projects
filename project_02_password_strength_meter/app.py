import streamlit as st
import re
import time

def evaluate_password(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long (12+ recommended).")
    
    # Upper and lowercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Repeated characters check
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid using repeated characters in a row.")
    
    # Common password check
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        feedback.append("Avoid using common passwords.")
        score = 1  # Override weak score
    
    # Strength Evaluation
    if score >= 5:
        strength = "Very Strong"
        message = "🔥 Your password is very strong! Well done."
    elif score == 4:
        strength = "Strong"
        message = "✅ Your password is strong!"
    elif score == 3:
        strength = "Moderate"
        message = "⚠️ Your password is moderate. Consider adding more security features."
    else:
        strength = "Weak"
        message = "❌ Your password is weak. Improve it with the suggestions below."
    
    return strength, score, message, feedback

def main():
    st.set_page_config(page_title="Password Strength Meter", layout="centered")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 10px;
        }
        .animated-text {
            animation: fadeIn 1s ease-in-out;
            font-weight: bold;
            font-size: 24px;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .progress-bar {
            height: 10px;
            border-radius: 5px;
            transition: width 0.5s ease-in-out;
        }
        .weak { background-color: red; width: 20%; }
        .moderate { background-color: orange; width: 50%; }
        .strong { background-color: green; width: 80%; }
        .very-strong { background-color: blue; width: 100%; }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🔐 Password Strength Meter")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        with st.spinner('Analyzing password...'):
            time.sleep(1)  # Simulating processing time
        
        strength, score, message, feedback = evaluate_password(password)
        
        # Determine progress bar class
        progress_class = "weak" if score <= 2 else "moderate" if score == 3 else "strong" if score == 4 else "very-strong"
        
        st.markdown(f"<h3 class='animated-text'>{strength} ({score}/5)</h3>", unsafe_allow_html=True)
        st.markdown(f"<div class='progress-bar {progress_class}'></div>", unsafe_allow_html=True)
        st.info(message)
        
        if feedback:
            st.warning("**Suggestions to improve your password:**")
            for tip in feedback:
                st.write(f"- {tip}")
    
if __name__ == "__main__":
    main()
