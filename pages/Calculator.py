import streamlit as st
import math

st.title("Exam Guessing Probability Calculator")

g = st.number_input("No. of questions guessed", min_value=1)
n = st.number_input("Options per question", min_value=2)
m = st.number_input("Marks for correct answer", value=4,min_value=1)
k = st.number_input("Negative marks", value=1,min_value=0)

p = 1/n
expected = g * (p*m - (1-p)*k)

st.write("### Expected Score:", round(expected, 2))

if expected > 0:
    st.success("Guessing may be mathematically beneficial")
else:
    st.error("Guessing is not recommended")

from math import comb

distribution = []

prob_gain = 0
prob_loss = 0
prob_even = 0

for x in range(g + 1):
    prob_x = comb(g, x) * (p**x) * ((1-p)**(g-x))
    score = m*x - k*(g-x)

    distribution.append((x, score, prob_x))

    if score > 0:
        prob_gain += prob_x
    elif score < 0:
        prob_loss += prob_x
    else:
        prob_even += prob_x

st.write("### Outcome probabilities")

st.write(f"Probability of gaining marks: {prob_gain*100:.2f}%")
st.write(f"Probability of breaking even: {prob_even*100:.2f}%")
st.write(f"Probability of losing marks: {prob_loss*100:.2f}%")

st.write("### Feasible outcomes")

st.write("Correct | Net Score | Probability")

for x, score, prob_x in distribution:
    if prob_x >= 0.035:
        st.write(f"{x} | {score} | {prob_x*100:.2f}%")
