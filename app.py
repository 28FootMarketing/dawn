import streamlit as st

st.set_page_config(page_title="Agent Dawn - Emotional Reset", layout="centered")

st.title("🌅 Meet Agent Dawn - Emotional Reset & Self-Care Advisor")
st.markdown("""
**Role:** Emotional Reset & Self-Care Agent  
**Nickname:** "The Reset Button"  
**Style of Play:** Calm, reflective, but unapologetically real.  
**Job Description:**  
Dawn checks in with student-athletes emotionally. She delivers mood-based affirmations, confidence rebuilders, and if needed—stern reminders to refocus. She connects users to motivational flows powered by Kobe or Kareem.

> "Reset your mindset, recalibrate your focus. Dawn helps you rise strong."
""")

# Mood check-in interface
st.subheader("How are you feeling today?")
mood = st.radio("Choose one:", ["😃 Great", "😐 Okay", "😞 Struggling"])

if mood == "😃 Great":
    st.success("Awesome! Keep riding that wave. Remember, confidence is contagious.")
elif mood == "😐 Okay":
    st.info("Staying balanced is a win. Want to recharge with a Kobe training boost?")
    if st.button("Yes, connect me to Kobe"):
        st.write("✅ Connecting to Kobe’s motivational flow...")
elif mood == "😞 Struggling":
    st.warning("Sometimes you need a reset.")
    if st.button("Reset with Dawn’s Affirmation"):
        st.markdown("**'You are built for this moment. Get up, reset, and move with intention.'**")
    if st.button("Connect to Kareem for Recovery"):
        st.write("🔁 Sending you to Kareem’s recovery path...")

st.markdown("---")
st.caption("Agent Dawn is part of your All-Star AI Support Team | FacilitateTheProcess.com")
