import streamlit as st

st.set_page_config(
    page_title="FormLens",
    page_icon="📄",
    layout="wide",
)

st.title("FormLens")
st.subheader("Document Analysis and Validation")
st.info("Prototype in progress. Document extraction is being implemented.")

uploaded = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"],
)

if uploaded is not None:
    st.success("Document uploaded successfully.")
    st.write({
        "Filename": uploaded.name,
        "Size (KB)": round(uploaded.size / 1024, 2),
    })
    st.caption("No extraction or document validation has run yet.")
else:
    st.caption("Upload a PDF to begin.")
