import streamlit as st

st.set_page_config(page_title="Contact Marje", page_icon="♀️", layout="wide")

st.markdown("""
<style>
.contact-main {
    background: linear-gradient(135deg, #FF69B4, #BA55D3) !important;
    border-radius: 25px !important;
    padding: 3rem !important;
    color: white !important;
    text-align: center !important;
    box-shadow: 0 20px 40px rgba(255,105,180,0.4) !important;
    margin: 2rem 0 !important;
}
.info-card {
    background: linear-gradient(135deg, #E6E6FA, #DDA0DD) !important;
    border: 3px solid #FF69B4 !important;
    padding: 2rem !important;
    border-radius: 20px !important;
    margin: 1rem 0 !important;
}
.success-card {
    background: linear-gradient(135deg, #98FB98, #90EE90) !important;
    color: #2C3E50 !important;
    padding: 2rem !important;
    border-radius: 20px !important;
    border: 3px solid #32CD32 !important;
    margin-top: 1rem !important;
}
h1, h2, h3 { color: #2C3E50 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 💌 Contact Marje M. Malacaste")
st.markdown("## 👩‍💻 3rd Year BSCS | Matugnao, Palanas, Masbate ♀️")

# Contact Info
st.markdown('<div class="contact-main">', unsafe_allow_html=True)
st.markdown("""
<h1>📱 Reach Out!</h1>
<h2>3rd Year BSCS Student ♀️</h2>
<p style='font-size: 1.5rem;'>Ready to connect with fellow students & coders!</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="info-card">
        <h3 style='color: #2C3E50;'>📧 Email</h3>
        <p style='font-size: 1.4rem; font-weight: bold; color: #2C3E50;'>
        marjemalacastee@gmail.com
        </p>
        <h3 style='color: #2C3E50;'>📱 Phone</h3>
        <p style='font-size: 1.4rem; font-weight: bold; color: #2C3E50;'>
        0981-026-0839
        </p>
        <h3 style='color: #2C3E50;'>📍 Address</h3>
        <p style='font-size: 1.2rem; color: #2C3E50;'>
        Matugnao, Palanas, Masbate
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3 style='color: #2C3E50;'>💕 Interests</h3>
        <ul style='color: #2C3E50; font-size: 1.1rem;'>
            <li>🍫 Chocolate</li>
            <li>🍗 Adobo</li>
            <li>👩‍🍳 Cooking</li>
            <li>✨ Designing</li>
            <li>♑ Capricorn ♀️</li>
        </ul>
        <h3 style='color: #2C3E50;'>🤝 Looking For</h3>
        <p style='color: #2C3E50;'>BSCS study buddies & coding partners!</p>
    </div>
    """, unsafe_allow_html=True)

# FIXED FORM SECTION
st.markdown("---")
st.markdown('<h2 style="text-align: center; color: #2C3E50;">💬 Send Message</h2>', unsafe_allow_html=True)

with st.form(key="marje_contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Your Name")
        email = st.text_input("📧 Your Email")
    with col2:
        subject = st.selectbox("📂 Subject", ["BSCS Study Group", "Coding Project", "Cooking Tips", "Design Collab", "Hi Marje!"])
        phone = st.text_input("📱 Phone (optional)")
    
    message = st.text_area("💌 Message", height=120, 
                          placeholder="Hi Marje! 3rd year BSCS here... 👩‍💻")
    
    col1, col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button("✨ Send to Marje", use_container_width=True)
    
    if submitted:
        if name and email and message:
            st.markdown("""
            <div class="success-card">
                <h2 style='color: #2C3E50;'>🎉 Message Sent Successfully!</h2>
                <h3 style='color: #2C3E50;'>Delivered to Marje:</h3>
                <p style='font-size: 1.3rem; color: #2C3E50; font-weight: bold;'>
                marjemalacastee@gmail.com
                </p>
                <p style='color: #2C3E50;'>♀️ 3rd Year BSCS from Matugnao will reply soon!</p>
            </div>
            """, unsafe_allow_html=True)
            st.success("📨 Message logged!")
            st.balloons()
        else:
            st.error("❌ Please fill name, email, and message!")

# Navigation
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with col2:
    st.info("👩‍💻 Marje's BSCS Portfolio ♀️")

# Footer
st.markdown("""
<div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #FF69B4, #BA55D3); color: white; border-radius: 25px; margin-top: 2rem;'>
    <h1 style='font-size: 3rem;'>Marje M. Malacaste</h1>
    <h2>3rd Year BSCS Student ♀️</h2>
    <p>Matugnao, Palanas, Masbate | marjemalacastee@gmail.com</p>
</div>
""", unsafe_allow_html=True)