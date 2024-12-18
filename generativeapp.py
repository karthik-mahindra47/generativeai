import streamlit as st

# Mock function to simulate AI-generated breakdown analysis
def generate_breakdown_analysis(breakdown_name):
    if not breakdown_name:
        return "Please provide a valid breakdown name."
    
    return f"""
    Analysis for Breakdown: '{breakdown_name}'
    
    ICA: Immediate cause might be improper lubrication or misalignment.
    PCA: Permanent cause might be inadequate operator training or overloading equipment.
    Reasons:
    - Poor maintenance schedule
    - Operator negligence
    - Outdated equipment
    Remedies:
    - Implement regular maintenance checks
    - Provide operator training programs
    - Replace outdated machinery with modern equipment
    """

# Streamlit app
st.title("Plant Breakdown Analysis AI Tool")
st.write("Enter the breakdown name below to generate ICA, PCA, possible reasons, and remedies.")

# User input
breakdown_name = st.text_input("Breakdown Name", placeholder="Enter breakdown name here")

if st.button("Analyze Breakdown"):
    if breakdown_name.strip():  # Ensure non-empty input
        with st.spinner("Generating analysis..."):
            analysis = generate_breakdown_analysis(breakdown_name)
            st.subheader(f"Analysis for '{breakdown_name}':")
            st.text(analysis)
    else:
        st.warning("Please enter a valid breakdown name.")

# Footer to confirm app rendering
st.write("---")
st.write("**Plant Breakdown Analysis AI Tool by Generative AI**")
