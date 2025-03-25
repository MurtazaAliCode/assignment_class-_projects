import streamlit as st
import time


def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"Metre": 1, "Centimetre": 100, "Kilometre": 0.001, "Millimetre": 1000, "Inch": 39.3701, "Foot": 3.28084},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {
            "Celsius": lambda c: c,
            "Fahrenheit": lambda c: (c * 9/5) + 32,
            "Kelvin": lambda c: c + 273.15
        }
    }
    
    units = conversion_factors[category]
    if from_unit in units and to_unit in units:
        if callable(units[from_unit]):
            return units[to_unit](value)
        return value * (units[to_unit] / units[from_unit])
    return None


st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")
st.title("🔢 Advanced Unit Converter")
st.write("Convert different units easily!")


categories = ["Length", "Weight", "Temperature"]
selected_category = st.selectbox("Select Category", categories)


conversion_factors = {
    "Length": {"Metre": 1, "Centimetre": 100, "Kilometre": 0.001, "Millimetre": 1000, "Inch": 39.3701, "Foot": 3.28084},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {
        "Celsius": lambda c: c,
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15
    }
}

units = list(conversion_factors[selected_category].keys())
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)
value = st.number_input("Enter Value", value=1.0, format="%.2f")


if st.button("Convert"):
    with st.spinner("Converting..."):
        time.sleep(1)  
    
    result = convert_units(value, from_unit, to_unit, selected_category)
    if result is not None:
        st.markdown(
            f"<h2 style='text-align: center; color: green; animation: fadeIn 2s;'>{value} {from_unit} = {result:.2f} {to_unit}</h2>",
            unsafe_allow_html=True
        )
        st.balloons()
        st.success(f"Formula applied for {selected_category}")
    else:
        st.error("Invalid conversion")


st.markdown("---")
st.write("💡 Tip: This tool supports Length, Weight, and Temperature conversions. More units coming soon!")
