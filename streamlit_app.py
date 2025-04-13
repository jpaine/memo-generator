import streamlit as st
import sys
import os
import uuid
import traceback

# Robust import handling
try:
    from main import run_analysis
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.error(traceback.format_exc())
    run_analysis = None

def generate_trace_id():
    """Generate a unique trace ID for tracking."""
    return str(uuid.uuid4())

def main():
    st.set_page_config(
        page_title="GGV Brain Investment Memorandum Generator",
        page_icon="💡",
        layout="wide"
    )

    st.title("🚀 GGV Brain Investment Memorandum Generator")
    
    # Comprehensive dependency check
    if run_analysis is None:
        st.error("Critical Error: Unable to load analysis module")
        st.info("Possible reasons:")
        st.info("1. Incorrect Python version")
        st.info("2. Missing dependencies")
        st.info("3. Project structure issues")
        return

    # Rest of the Streamlit app code...