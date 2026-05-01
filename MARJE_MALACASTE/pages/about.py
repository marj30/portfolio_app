import streamlit as st

st.set_page_config(page_title="About Marje", page_icon="♀️", layout="wide")

st.markdown("""
<style>
.profile-card {
    background: linear-gradient(135deg, #FF69B4, #E6E6FA) !important;
    border: 3px solid #FF69B4 !important;
    border-radius: 25px !important;
    padding: 3rem !important;
    text-align: center !important;
    box-shadow: 0 20px 40px rgba(255,105,180,0.2) !important;
}
.edu-card {
    background: linear-gradient(135deg, #BA55D3, #DDA0DD) !important;
    border-left: 6px solid #FF69B4 !important;
    padding: 2rem !important;
    border-radius: 20px !important;
    margin: 1rem 0 !important;
}
h1, h2, h3 { color: #2C3E50 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 👩‍💻 Marje M. Malacaste")
st.markdown("## ♀️ 21 | 3rd Year BSCS | Matugnao, Palanas, Masbate")

# Profile Card
st.markdown('<div class="profile-card">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <h2 style='color: #2C3E50;'>🌟 Student Profile</h2>
    <ul style='color: #2C3E50; font-size: 1.2rem;'>
        <li><strong>Name:</strong> Marje M. Malacaste</li>
        <li><strong>Age:</strong> 21 ♀️</li>
        <li><strong>Birthday:</strong> Capricorn ♑</li>
        <li><strong>Address:</strong> Matugnao, Palanas, Masbate</li>
        <li><strong>Program:</strong> BSCS (3rd Year)</li>
    </ul>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <h2 style='color: #2C3E50;'>💖 Passions</h2>
    <ul style='color: #2C3E50; font-size: 1.2rem;'>
        <li>🍫 Chocolate</li>
        <li>🍗 Adobo</li>
        <li>👩‍🍳 Cooking</li>
        <li>✨ Designing</li>
    </ul>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Education
st.markdown("---")
st.markdown("## 🎓 Education Background")

st.markdown("""
<div class="edu-card">
    <h3>🏫 Elementary School</h3>
    <p><strong>Location:</strong> Matugnao area school<br>
    - Built strong foundation<br>
    - Excelled in academics</p>
</div>
<div class="edu-card">
    <h3>🎓 High School</h3>
    <p><strong>Location:</strong> Palanas, Masbate<br>
    - Prepared for BSCS<br>
    - Science track student</p>
</div>
<div class="edu-card">
    <h3>🎓 College (Current)</h3>
    <p><strong>3rd Year BSCS</strong><br>
    - Programming & Algorithms<br>
    - Web Development<br>
    - Building portfolio!</p>
</div>
""", unsafe_allow_html=True)

# BSCS Subjects
st.markdown("---")
st.markdown("## 📚 3rd Year BSCS Subjects")

subjects = [
    "Advanced Programming",
    "Data Structures",
    "Database Systems", 
    "Software Engineering",
    "Web Programming",
    "Computer Networks"
]

cols = st.columns(2)
for i, subject in enumerate(subjects):
    with cols[i%2]:
        st.markdown(f"• **{subject}**")

st.markdown("---")
st.markdown("## 🎯 Goals This Semester")

goals = [
    "Complete 3 coding projects",
    "Master database design",
    "Build personal website", 
    "Join programming contest",
    "90+ average target ♀️"
]

for goal in goals:
    st.markdown(f"• {goal}")

if st.button("📧 Contact Me", use_container_width=True):
    st.switch_page("pages/contact.py")