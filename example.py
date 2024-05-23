import streamlit as st
import numpy as np

# Function to replace columns in matrices
def replace_column(matrix, column_index, new_column):
    matrix[:, column_index] = new_column.flatten()

# Function to calculate determinant
def calculate_determinant(matrix):
    return np.linalg.det(matrix)

st.title("CRAMER'S RULE CALCULATOR")
st.subheader("ENGINEERING MATHEMATICS")
st.write("---")
st.write("""
### Enter the coefficients for the system of linear equations
""")

# Input coefficients and constants
A = np.zeros((3, 3))
X = np.zeros((3, 1))

for i in range(3):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        A[i, 0] = st.number_input(f'Enter value of x1 for equation {i+1}:', key=f'x1_{i}')
    with col2:
        A[i, 1] = st.number_input(f'Enter value of x2 for equation {i+1}:', key=f'x2_{i}')
    with col3:
        A[i, 2] = st.number_input(f'Enter value of x3 for equation {i+1}:', key=f'x3_{i}')
    with col4:
        X[i] = st.number_input(f'Enter value of constant for equation {i+1}:', key=f'const_{i}')

# Make copies of the matrix A for column replacements
B = np.copy(A)
C1 = np.copy(B)
C3 = np.copy(B)
C5 = np.copy(B)

# Replace columns in the copied matrices with constants
replace_column(C1, 0, X)
replace_column(C3, 1, X)
replace_column(C5, 2, X)

# Calculate determinants
Determinant_1 = calculate_determinant(B)
Determinant_2 = calculate_determinant(C1)
Determinant_3 = calculate_determinant(C3)
Determinant_4 = calculate_determinant(C5)

if Determinant_1 != 0:
    # Solutions using Cramer's rule
    x1 = Determinant_2 / Determinant_1
    x2 = Determinant_3 / Determinant_1
    x3 = Determinant_4 / Determinant_1

    st.write("\n### Solution using Cramer's rule:")
    st.write(f"x1 = {x1}")
    st.write(f"x2 = {x2}")
    st.write(f"x3 = {x3}")

    # Verify solution
    sol = st.selectbox("Choose the equation to verify the solution:", [1, 2, 3])
    if sol == 1:
        solution = x1 * A[0, 0] + x2 * A[0, 1] + x3 * A[0, 2]
        st.write(f"The solution of equation 1 using Cramer's rule is {solution}")
    elif sol == 2:
        solution = x1 * A[1, 0] + x2 * A[1, 1] + x3 * A[1, 2]
        st.write(f"The solution of equation 2 using Cramer's rule is {solution}")
    elif sol == 3:
        solution = x1 * A[2, 0] + x2 * A[2, 1] + x3 * A[2, 2]
        st.write(f"The solution of equation 3 using Cramer's rule is {solution}")
else:
    st.write("The determinant of the coefficient matrix is zero, so the system has no unique solution.")

st.write('\n')
st.write("---")
st.write('\n')

DESCRIPTION = """
    LEARN HOW TO SOLVE THE CRAMER'S RULE FOR LINEAR EQUATION. CLICK ON IT!
"""
link_url = "https://instruction-page.streamlit.app/"

# Add a hyperlink to the text and apply color formatting
description_with_link = f"<a style='color:white' href='{link_url}' target='_blank'>{DESCRIPTION}</a>"

# Display the text with the hyperlink
st.markdown(description_with_link, unsafe_allow_html=True)

st.subheader("THANK YOU FOR CHOOSING US!")
st.write("~ by Aman Joshi")
