import streamlit as st
import random

# Website Title
st.title(" Welcome to My Website ")
st.header("Learn, Enjoy, and Get Inspired")

# Simple Calculator
st.subheader(" Calculator")
num1 = st.number_input("First number:", value=0)
num2 = st.number_input("Second number:", value=0)
operation = st.selectbox("Operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
    st.write(f"Result: **{result}**")


st.subheader("Fun Fact")
facts = [
    "Honey never spoils, even after 3000 years!",
    "A single spaghetti strand is called a 'spaghetto'.",
    "Octopuses have three hearts!",
    "Bananas are berries, but strawberries aren't.",
    "The universe has more stars than grains of sand on Earth."
]

if st.button("Show Fun Fact"):
    st.write(random.choice(facts))

# Motivational Quotes 
st.subheader("Motivation")
quotes = [
    "Believe you can, and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Keep going; success is near. - Sam Levenson",
    "Happiness is the key to success. - Albert Schweitzer"]

if st.button("Show Motivation"):
    st.write(random.choice(quotes))


st.write(" Thank you for visiting! Have a great day! ")
