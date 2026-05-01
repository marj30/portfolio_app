import streamlit as st

st.set_page_config(
    page_title="Marje M. Malacaste - BSCS",
    page_icon="👩‍💻",
    layout="wide"
)

# Beautiful CSS for Marje's style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;600&display=swap');
.main-header {
    font-family: 'Dancing Script', cursive !important;
    font-size: 4.5rem !important;
    background: linear-gradient(45deg, #FF69B4, #BA55D3, #9370DB) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center !important;
}
.subtitle { 
    font-family: 'Poppins', sans-serif; 
    font-size: 1.4rem; 
    color: #2C3E50; 
    text-align: center; 
    margin-bottom: 2rem; 
}
.hero-card {
    background: linear-gradient(135deg, #FF69B4, #E6E6FA) !important;
    border-radius: 25px !important;
    padding: 2.5rem !important;
    box-shadow: 0 15px 35px rgba(255,105,180,0.3) !important;
}
.stat-card {
    background: linear-gradient(135deg, #BA55D3, #DDA0DD) !important;
    color: white !important;
    padding: 2rem !important;
    border-radius: 20px !important;
    text-align: center !important;
    box-shadow: 0 10px 25px rgba(186,85,211,0.3) !important;
}
.hobby-card {
    background: linear-gradient(135deg, #9370DB, #E0BBE4) !important;
    border-left: 6px solid #FF69B4 !important;
    padding: 1.5rem !important;
    border-radius: 15px !important;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div style="text-align: center; padding: 2rem;">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">Marje M. Malacaste</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">👩‍💻 3rd Year BSCS Student | 21 | Matugnao, Palanas, Masbate ♀️</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👩‍💻 About Me", use_container_width=True):
        st.switch_page("pages/about.py")
with col2:
    if st.button("📧 Contact", use_container_width=True):
        st.switch_page("pages/contact.py")
with col3:
    st.info("🍫 Capricorn ♀️ | Loves Cooking & Designing")

# Hero Section
st.markdown('<div class="hero-card">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <h2 style='color: #2C3E50;'>🌟 About Marje</h2>
    <p style='font-size: 1.2rem; color: #2C3E50; line-height: 1.6;'>
    3rd year <strong>Bachelor of Science in Computer Science</strong> student!  
    Passionate about coding, cooking, and designing.  
    Capricorn girl from beautiful Matugnao, Palanas, Masbate! ♀️
    </p>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <h3 style='color: #2C3E50;'>Favorites 🍫</h3>
    <ul style='color: #2C3E50; font-size: 1.1rem;'>
        <li>🍫 Chocolate</li>
        <li>🍗 Adobo</li>
        <li>✨ Designing</li>
        <li>👩‍🍳 Cooking</li>
    </ul>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Stats
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>📊 Quick Stats</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-card">
        <h1 style='font-size: 3rem;'>21</h1>
        <p>Age ♀️</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card">
        <h1 style='font-size: 3rem;'>3rd</h1>
        <p>Year BSCS</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card">
        <h1 style='font-size: 3rem;'>♑</h1>
        <p>Capricorn</p>
    </div>
    """, unsafe_allow_html=True)

# Hobbies
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>💖 Hobbies & Interests</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="hobby-card">
        <h3 style='color: #2C3E50;'>👩‍🍳 Cooking</h3>
        <p style='color: #2C3E50;'>Love creating delicious adobo and experimenting with recipes!</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="hobby-card">
        <h3 style='color: #2C3E50;'>✨ Designing</h3>
        <p style='color: #2C3E50;'>Creative designs for web and graphics!</p>
    </div>
    """, unsafe_allow_html=True)

# Interactive
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>📱 Quick Poll</h2>", unsafe_allow_html=True)
favorite = st.selectbox("🍫 Favorite Food?", ["Chocolate 🍫", "Adobo 🍗", "Both! 😋"])
if st.button("Submit", type="primary"):
    st.success(f"🎉 Great choice Marje! {favorite} is awesome!")
    st.balloons()

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #2C3E50;'>
    <h3>👩‍💻 Marje M. Malacaste | 3rd Year BSCS | Matugnao, Palanas, Masbate</h3>
</div>
""", unsafe_allow_html=True)