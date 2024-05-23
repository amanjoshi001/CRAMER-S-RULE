
import streamlit as st

st.title("Cramer's Rule Method")
st.write("---")
st.write("""
Instructions for Solving Linear Equations using Cramer's Rule:

1. Extract Coefficients: Take the coefficient values of x1, x2, and x3 from each linear equation.

2. Form Matrix 'A': Create a matrix A using these coefficient values. Each row represents an equation, and each column represents a variable (x1, x2, x3).

3. Collect Constants: Take the constant values from each equation and organize them into a separate matrix B. Each row of B corresponds to a single equation.

4. Set up Equation: Arrange the matrices A and B in the format AX = B, where X represents the column vector of variables (x1, x2, x3).

5. Calculate Determinant: Find the determinant of matrix A. This determinant is crucial for solving the equations using Cramer's Rule.

6. Solve for Variables: To find the solution, calculate each variable (x1, x2, x3) using the formula xi = |Bi| / |A|, where i = 1, 2, 3.

7. Calculate Bi: To find Bi, substitute the i-th column of matrix A with matrix B, keeping the other columns intact.

8. Find Determinants of Bi: Calculate the determinant of each modified matrix Bi.

9. Compute Solutions: Finally, find the solution for each variable by dividing the determinant of Bi by the determinant of A.

""")
DESCRIPTION = """
GO BACK TO MAIN PAGE! 
"""

link_url = "https://www.gehu.ac.in/"

# Add a hyperlink to the text and apply color formatting
description_with_link = f"<font color='black'><a href='{link_url}' target='_blank'>{DESCRIPTION}</a></font>"

# Display the text with the hyperlink
st.markdown(description_with_link, unsafe_allow_html=True)