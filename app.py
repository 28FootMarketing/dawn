import streamlit as st
import random

st.set_page_config(page_title="Dawn Bot - Wellness Coach", page_icon="🌅", layout="centered")

st.title("🌅 Dawn: The Calm Before the Storm")
st.subheader("Emotional Wellness & Clarity Coach")

st.markdown("**Style of Play:** Graceful, steady, and uplifting")

st.markdown("""
Dawn supports the emotional side of the recruiting grind.  
She offers affirmations, calming prompts, and grounding support when things get tense or uncertain.

> “Dawn brings light to doubt and calm to the chaos. Her timing is perfect when pressure rises.”
""")

affirmations = [
    "“You do not have to rush what is already meant for you.”",
    "“You can be proud and still want more.”",
    "“It is okay to pause. Stillness is strength too.”",
    "“You are seen. You are worthy. You are ready.”",
    "“Progress is happening—even if it is quiet today.”",
    "“Do not let comparison steal your confidence.”",
    "“Today’s reset creates tomorrow’s momentum.”"
]

st.header("Need a reset moment?")
if st.button("Give me an affirmation"):
    st.success("Dawn says:")
    st.markdown(f"**{random.choice(affirmations)}**")

st.header("What kind of emotional support do you need right now?")
support_type = st.radio("Select one:", [
    "Encouragement", "Stillness", "Clarity", "Self-worth", "Energy", "Hope", "Patience"
])

if support_type:
    st.info(f"Dawn says: When you need {support_type.lower()}, listen closely. Your next move will come from a calmer place.")
