import streamlit as st

st.title("GUIDE")
st.write("")

c1, sep1, c2, sep2, c3 = st.columns([1, 0.05, 1, 0.05, 1])

with c1:
    st.markdown(
    """
    <div style="text-align:left">
        <p style="font-size:22px;">JEE Main</p>
        <ul style="font-size:16px;">
            <li>+4 / −1 marking scheme is generally favourable.</li>
            <li>Guessing is reasonable if at least one option is eliminated.</li>
            <li>Works better over multiple attempts, not single questions.</li>
            <li>Negative marks can still accumulate if overused.</li>
            <li>Useful for students on the edge of cutoffs.</li>
        </ul>
        <p style="font-size:14px;">
        Bottom line: informed guessing can help when used selectively.
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )

with sep1:
    st.markdown(
        "<div style='border-left:1px solid #cccccc; min-height:100vh;'></div>",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
    """
    <div style="text-align:left">
        <p style="font-size:22px;">BITSAT</p>
        <ul style="font-size:16px;">
            <li>+3 / −1 marking scheme is less forgiving.</li>
            <li>Blind guessing can quickly reduce score.</li>
            <li>Guessing is safer only after eliminating two options.</li>
            <li>Attempting all unlocks bonus section.</li>
	    <li>So useful to attempt all only if wish to attempt bonus </li>
            <li>Time pressure makes excessive guessing risky.</li>
        </ul>
        <p style="font-size:14px;">
        Bottom line: guessing requires caution and strong time control.
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )

with sep2:
    st.markdown(
        "<div style='border-left:1px solid #cccccc; min-height:100vh;'></div>",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
    """
    <div style="text-align:left">
        <p style="font-size:22px;">CUET</p>
        <ul style="font-size:16px;">
            <li>Marking scheme is +5 / −1, which is quite favourable.</li>
            <li>Elimination-based attempts are safer than blind guesses.</li>
            <li>Guessing is recommended if time is not a major constraint.</li>
            <li>Section-wise time management is crucial.</li>
        </ul>
        <p style="font-size:14px;">
        Bottom line: informed guessing is a useful tool.
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )
