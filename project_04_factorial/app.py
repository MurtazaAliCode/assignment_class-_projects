import streamlit as st
import math
import time

def calculate_factorial(n):
    try:
        n = int(n)
        if n < 0:
            return "Factorial is not defined for negative numbers."
        return math.factorial(n)
    except ValueError:
        return "Please enter a valid integer."

# Streamlit UI
st.title("✨ Factorial Calculator ✨")
st.write("Enter a number to find its factorial.")

# User input
number = st.text_input("Enter a number:", "0")

if st.button("Calculate Factorial"):
    with st.spinner("Calculating... 🔄"):
        time.sleep(1.5)  # Simulating processing time
        result = calculate_factorial(number)
    
    st.success(f"Factorial: {result}")
    
    # Display factorial formula
    if number.isdigit() and int(number) >= 0:
        num = int(number)
        formula = f"{num}! = " + " × ".join(map(str, range(num, 0, -1))) + f" = {result}"
        st.markdown(f"### 📌 Factorial Formula:")
        st.latex(formula)
    
    st.balloons()  # Fun animation

# Documentation Section
st.sidebar.title("📖 Documentation")
st.sidebar.write("""
### What is Factorial?
Factorial of a non-negative integer *n* is the product of all positive integers less than or equal to *n*.

- **Formula:**  
  \( n! = n \times (n-1) \times ... \times 2 \times 1 \)
- **Example:**  
  \( 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 \)

This app calculates the factorial of any given number and displays the full factorial formula.
""")
