import streamlit as st
import sys
import os
import uuid

# Add project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import your existing project modules
from main import run_analysis

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
    
    # Market Opportunity Input
    market_opportunity = st.text_input(
        "Describe the Market Opportunity", 
        placeholder="E.g., AI-powered data labeling for healthcare industry"
    )
    
    # Generate Memo Button
    if st.button("Generate Investment Memo"):
        if market_opportunity:
            with st.spinner('Generating Memorandum...'):
                try:
                    # Generate a unique trace ID
                    trace_id = generate_trace_id()
                    
                    # Run analysis
                    memo_result = run_analysis(market_opportunity, trace_id)
                    
                    # Display Results
                    st.success("Investment Memorandum Generated Successfully!")
                    
                    # Expandable sections for different parts of the memo
                    with st.expander("Market Analysis"):
                        st.write(memo_result.get('market_analysis', 'No market analysis available'))
                    
                    with st.expander("Competitor Landscape"):
                        st.write(memo_result.get('competitor_analysis', 'No competitor analysis available'))
                    
                    # Option to download the full memo
                    st.download_button(
                        label="Download Full Memorandum",
                        data=str(memo_result),
                        file_name=f"investment_memo_{market_opportunity.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
                
                except Exception as e:
                    st.error(f"Error generating memorandum: {e}")
        else:
            st.warning("Please enter a market opportunity description.")

    # Sidebar with additional information
    st.sidebar.header("About GGV Brain")
    st.sidebar.info("""
    An AI-powered platform to generate investment memorandums 
    for AI startups. Provides market analysis, competitor insights, 
    and strategic recommendations.
    """)

    st.sidebar.header("How to Use")
    st.sidebar.info("""
    1. Enter a clear description of the market opportunity
    2. Click 'Generate Investment Memo'
    3. Review the generated insights
    4. Download the full memorandum
    """)

if __name__ == "__main__":
    main()