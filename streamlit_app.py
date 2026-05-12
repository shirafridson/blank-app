import streamlit as st

# כותרת יפה לאפליקציה
st.title("👠 הסטייליסט האישי של Factory 54")

# הודעת פתיחה
st.write("ברוכה הבאה! אני ה-AI שיעזור לך למצוא את הלוק המושלם.")

# יצירת כפתור להמלצה
if st.button('קבלת המלצה לסטייל'):
    st.balloons() # חגיגה של בלונים על המסך!
    st.success("ההמלצה שלי להיום: שמלת ערב אלגנטית עם נעלי עקב תואמות.")
    # כאן אפשר להוסיף קישור לתמונה אמיתית מהאתר
    st.image("https://www.factory54.co.il/images/logos/f54-logo.png", width=200)