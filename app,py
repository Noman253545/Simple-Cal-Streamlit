import streamlit as st

# Define the calculator functions
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

# Create the Streamlit app
def calculator():
    st.title("Simple Calculator")

    # Select operation
    operation = st.selectbox("Select Operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Input numbers
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

    # Display the result
    if st.button("Calculate"):
        st.write(f"Result: {result}")

# Run the app
if __name__ == "__main__":
    calculator()
