import streamlit as st

st.set_page_config(page_title="Agent Dawn - Emotional Reset Bot", layout="centered")

st.title("🌅 Meet Agent Dawn: Emotional Reset Coach")
st.subheader("Nickname: The Mental Timeout")
st.markdown("""
**Style of Play:** Empathetic, bold, and focused.

Dawn helps student-athletes recognize when they need a mental reset. She delivers short mood check-ins, self-care reminders, emotional tracking flows, and occasionally gives a tough-love message when athletes are stuck.

---

### 🧠 What Agent Dawn Does:
- Tracks moods and emotional triggers
- Sends reminders to take emotional breaks
- Offers affirmations or mental resets
- Delivers *stern* advice when needed
- Connects to **Agent Kobe** (motivation) or **Agent Kareem** (recovery plans)

""")

# Example Mood Reset Interaction
st.markdown("### 💬 Sample Reset Dialogue:")
st.markdown("""
- *Dawn*: "You’ve been pushing hard lately. When is the last time you breathed deeply and checked in with your mood?"
- *Dawn*: "This is not a breakdown; this is a breakthrough in disguise. Let’s realign."
""")

# Mood Check Feature
mood = st.radio("How are you feeling right now?", ["🔥 Frustrated", "😔 Sad", "💪 Motivated", "😐 Numb", "😊 Great"])
if mood:
    st.success(f"Dawn has logged your mood as: **{mood}**. Let us reflect and reset.")

# Call to action
st.markdown("---")
st.markdown("Need a boost? Reconnect with:")
col1, col2 = st.columns(2)
with col1:
    if st.button("Agent Kobe - Motivation"):
        st.markdown("*Redirecting to Kobe...*")
with col2:
    if st.button("Agent Kareem - Recovery"):
        st.markdown("*Redirecting to Kareem...*")
