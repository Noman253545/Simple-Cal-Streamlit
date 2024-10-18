import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define scientific functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def sine(x):
    return np.sin(np.radians(x))

def cosine(x):
    return np.cos(np.radians(x))

def tangent(x):
    return np.tan(np.radians(x))

def logarithm(x):
    if x > 0:
        return np.log(x)
    else:
        return "Error! Logarithm of non-positive number."

def exponential(x):
    return np.exp(x)

# Create the Streamlit app
def scientific_calculator():
    st.title("Scientific Graphical Calculator")

    # Select operation
    operation = st.selectbox(
        "Select Operation:",
        ["Add", "Subtract", "Multiply", "Divide", "Sine", "Cosine", "Tangent", "Logarithm", "Exponential", "Plot Function"]
    )

    if operation in ["Add", "Subtract", "Multiply", "Divide"]:
        num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
        num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

        # Perform calculation based on the selected operation
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)

        if st.button("Calculate"):
            st.write(f"Result: {result}")

    elif operation in ["Sine", "Cosine", "Tangent", "Logarithm", "Exponential"]:
        num = st.number_input("Enter the number", value=0.0, step=1.0)

        if operation == "Sine":
            result = sine(num)
        elif operation == "Cosine":
            result = cosine(num)
        elif operation == "Tangent":
            result = tangent(num)
        elif operation == "Logarithm":
            result = logarithm(num)
        elif operation == "Exponential":
            result = exponential(num)

        if st.button("Calculate"):
            st.write(f"Result: {result}")

    # Plotting a mathematical function
    elif operation == "Plot Function":
        function = st.selectbox("Choose function to plot", ["Sine", "Cosine", "Tangent"])
        x = np.linspace(-360, 360, 500)

        if function == "Sine":
            y = np.sin(np.radians(x))
        elif function == "Cosine":
            y = np.cos(np.radians(x))
        elif function == "Tangent":
            y = np.tan(np.radians(x))

        # Create plot
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=function)
        plt.title(f"{function} Function")
        plt.xlabel("Degrees")
        plt.ylabel(f"{function}(x)")
        plt.grid(True)
        plt.legend()

        # Display plot
        st.pyplot(plt)

# Run the app
if __name__ == "__main__":
    scientific_calculator()
