import streamlit as st

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles * 1.60934

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds * 0.453592

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_cm_to_inch(cm):
    return cm * 0.393701

def convert_inch_to_cm(inch):
    return inch * 2.54

def convert_kilogram_to_gram(kilogram):
    return kilogram * 1000

def convert_gram_to_kilogram(gram):
    return gram * 0.001

def convert_m_to_yards(m):
    return m * 1.09361

def convert_yards_to_m(yards):
    return yards * 0.9144

st.set_page_config(
    page_title="Unit Conversion"
)
st.title("Unit Converter")
st.write("Welcome to the Unit Converter!")

conversion_type = st.selectbox("Select a conversion type:", ["Length", "Weight", "Temperature", "Distance"], key="conversion_type")
val_num = st.number_input("Enter a value to convert:")

if conversion_type == "Length":
    length_conversion = st.selectbox("Select conversion:", ["Kilometers to Miles", "Miles to Kilometers", "Centimeters to Inches", "Inches to Centimeters"])
    if length_conversion == "Kilometers to Miles":
        st.write(f"{val_num} Kilometers is equal to {convert_km_to_miles(val_num)} Miles")
    elif length_conversion == "Miles to Kilometers":
        st.write(f"{val_num} Miles is equal to {convert_miles_to_km(val_num)} Kilometers")
    elif length_conversion == "Centimeters to Inches":
        st.write(f"{val_num} Centimeters is equal to {convert_cm_to_inch(val_num)} Inches")
    elif length_conversion == "Inches to Centimeters":
        st.write(f"{val_num} Inches is equal to {convert_inch_to_cm(val_num)} Centimeters")

elif conversion_type == "Weight":
    weight_conversion = st.selectbox("Select conversion:", ["Kilograms to Pounds", "Pounds to Kilograms","Kilogram to Gram", "Gram to Kilogram"])
    if weight_conversion == "Kilograms to Pounds":
        st.write(f"{val_num} Kilograms is equal to {convert_kg_to_pounds(val_num)} Pounds")
    elif weight_conversion == "Pounds to Kilograms":
        st.write(f"{val_num} Pounds is equal to {convert_pounds_to_kg(val_num)} Kilograms")
    elif weight_conversion == "Kilogram to Gram":
        st.write(f"{val_num} Kilogram is equal to {convert_kilogram_to_gram(val_num)} Gram")
    elif weight_conversion == "Gram to Kilogram":
        st.write(f"{val_num} Gram is equal to {convert_gram_to_kilogram(val_num)} Kilogram")

elif conversion_type == "Temperature":
    temperature_conversion = st.selectbox("Select conversion:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    if temperature_conversion == "Celsius to Fahrenheit":
        st.write(f"{val_num} Celsius is equal to {convert_celsius_to_fahrenheit(val_num)} Fahrenheit")
    elif temperature_conversion == "Fahrenheit to Celsius":
        st.write(f"{val_num} Fahrenheit is equal to {convert_fahrenheit_to_celsius(val_num)} Celsius")

elif conversion_type == "Distance":
    distance_conversion = st.selectbox("Select conversion:", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Yards", "Yards to Meters"])
    if distance_conversion == "Kilometers to Miles":
        st.write(f"{val_num} Kilometers is equal to {convert_km_to_miles(val_num)} Miles")
    elif distance_conversion == "Miles to Kilometers":
        st.write(f"{val_num} Miles is equal to {convert_miles_to_km(val_num)} Kilometers")
    elif distance_conversion == "Meters to Yards":
        st.write(f"{val_num} Meters is equal to {convert_m_to_yards(val_num)} Yards")
    elif distance_conversion == "Yards to Meters":
        st.write(f"{val_num} Yards is equal to {convert_yards_to_m(val_num)} Meters")