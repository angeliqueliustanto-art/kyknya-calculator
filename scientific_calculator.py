
import streamlit as st
import math

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background-color: #e8edf3;
    }

    .main-title {
        background-color: #26364b;
        color: white;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 20px;
    }

    .calculator-box {
        background-color: #26364b;
        padding: 25px;
        border-radius: 18px;
        color: white;
    }

    .screen {
        background-color: #cbd7c6;
        color: #17271d;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 20px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }

    div.stButton > button {
        background-color: #344b65;
        color: white;
        border-radius: 8px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #526982;
        color: white;
    }

    h2, h3 {
        color: #26364b;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="main-title">
    <h1>CASIO Scientific Calculator</h1>
    <p>Advanced Mathematical Calculator</p>
    <small>CLASSWIZ INSPIRED DESIGN</small>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="screen">
    SCIENTIFIC CALCULATOR | DEG MODE
</div>
""", unsafe_allow_html=True)


st.subheader("Calculator")

operation = st.selectbox(
    "Select an operation:",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Logarithm (log base 10)",
        "Natural Logarithm (ln)",
        "Sine",
        "Cosine",
        "Tangent",
        "Factorial"
    ]
)


st.divider()


if operation in [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Power"
]:

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input(
            "First number",
            value=0.0
        )

    with col2:
        num2 = st.number_input(
            "Second number",
            value=0.0
        )

else:

    num = st.number_input(
        "Enter a number",
        value=0.0
    )


if st.button("CALCULATE", use_container_width=True):

    try:

        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":

            if num2 == 0:
                st.error("Cannot divide by zero.")
                st.stop()

            result = num1 / num2

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Square Root":

            if num < 0:
                st.error("Square root requires a non-negative number.")
                st.stop()

            result = math.sqrt(num)

        elif operation == "Logarithm (log base 10)":

            if num <= 0:
                st.error("Logarithm requires a positive number.")
                st.stop()

            result = math.log10(num)

        elif operation == "Natural Logarithm (ln)":

            if num <= 0:
                st.error("Natural logarithm requires a positive number.")
                st.stop()

            result = math.log(num)

        elif operation == "Sine":
            result = math.sin(math.radians(num))

        elif operation == "Cosine":
            result = math.cos(math.radians(num))

        elif operation == "Tangent":

            angle = math.radians(num)

            if math.isclose(math.cos(angle), 0, abs_tol=1e-12):
                st.error("Tangent is undefined at this angle.")
                st.stop()

            result = math.tan(angle)

        elif operation == "Factorial":

            if num < 0 or not num.is_integer():
                st.error("Factorial requires a non-negative integer.")
                st.stop()

            if num > 170:
                st.error("Number is too large.")
                st.stop()

            result = math.factorial(int(num))

        if isinstance(result, complex) or not math.isfinite(result):
            st.error("Calculation is outside the supported range.")
            st.stop()

        st.success("Calculation completed!")

        st.markdown("### Result")

        st.metric(
            label=operation,
            value=f"{result:.10g}"
        )

        st.caption(f"Exact numerical result: {result}")

    except ValueError:
        st.error("Please enter a valid number.")

    except OverflowError:
        st.error("Calculation is out of range.")

    except ZeroDivisionError:
        st.error("Cannot divide by zero.")


st.divider()

st.markdown("""
<div style="text-align:center; color:#526982;">
    <small>Scientific Calculator | Python & Streamlit</small>
</div>
""", unsafe_allow_html=True)
