import streamlit as st

st.markdown(
    """
    <style>
    div[data-testid="stButton"] > button {
        height: 140px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(page_title="Exam Guessing Tool", layout="centered")

# ---- TITLE ----
st.title("Engineering Exam Guessing Tool")
st.subheader("Make informed real-time decisions using probability")

st.write("")
st.write("")
st.write("")
st.write("")

# ---- TWO ICON BUTTONS ----
col1, col2 = st.columns(2)

with col1:
    calc_clicked = st.button(
        " ",
        key="calc_btn",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="
            pointer-events:none;
            text-align:center;
            margin-top:-150px;
        ">
            <span style="font-size:90px;">🧮</span>
            <p></p>
            <p style="font-size:30px;"><b>Calculator</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if calc_clicked:
        st.switch_page("pages/calculator.py")


with col2:
    guide_clicked = st.button(
        " ",
        key="guide_btn",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="
            pointer-events:none;
            text-align:center;
            margin-top:-150px;
        ">
            <span style="font-size:90px;">📓</span>
            <p></p>
            <p style="font-size:30px;"><b>Guide</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if guide_clicked:
        st.switch_page("pages/guide.py")



