import streamlit as st

st.set_page_config(
    page_title="Paws & Claws Pet Shop",
    page_icon="🐾",
    layout="wide",
)

# Custom CSS for extra polish
st.markdown("""
    <style>
        .big-font {font-size: 2.3em !important; font-weight:bold;}
        .subtitle {font-size: 1.2em; color: #4caf50;}
        .pet-card {
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 2px 10px rgba(76,175,80,0.10);
            padding: 20px;
            margin: 10px;
            text-align: center;
        }
        .pet-img {
            border-radius: 12px;
            margin-bottom: 10px;
            width: 100%;
            object-fit: cover;
        }
        .tag {
            display: inline-block;
            background: #4caf50;
            color: #fff;
            padding: 3px 12px;
            border-radius: 8px;
            font-size: 0.9em;
            margin-bottom: 6px;
        }
        .adopt-btn {
            background: #4caf50;
            color: #fff;
            padding: 8px 24px;
            border-radius: 15px;
            border: none;
            font-weight: bold;
            font-size: 1em;
            margin-top: 8px;
            transition: background 0.2s;
        }
        .adopt-btn:hover {
            background: #a3e635;
            color: #222;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 24px;
            font-size: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar (simulate with columns)
nav1, nav2, nav3, nav4, nav5 = st.columns([2,1,1,1,2])
with nav1: st.markdown('<span class="big-font">🐾 Paws & Claws</span>', unsafe_allow_html=True)
with nav2: st.markdown('[Home](#)', unsafe_allow_html=True)
with nav3: st.markdown('[Pets](#pets)', unsafe_allow_html=True)
with nav4: st.markdown('[About](#about)', unsafe_allow_html=True)
with nav5: st.markdown('<a href="#adopt" style="color:#fff;background:#4caf50;padding:8px 20px;border-radius:14px;text-decoration:none;">Adopt Now</a>', unsafe_allow_html=True)

st.markdown("---")

# Hero section
col1, col2 = st.columns([1,1])
with col1:
    st.markdown('<div class="big-font">Welcome to <span style="color:#4caf50;">Paws & Claws</span></div>', unsafe_allow_html=True)
    st.write("Your new best friend is waiting for you! Discover a world of love and loyalty.")
    st.markdown('<a href="#pets" class="adopt-btn">Meet Our Pets</a>', unsafe_allow_html=True)
with col2:
    st.image("https://images.unsplash.com/photo-1558788353-f76d92427f16?auto=format&fit=crop&w=600&q=80", use_column_width=True)

# Features
st.markdown("### Why Choose Us?")
f1, f2, f3 = st.columns(3)
with f1:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=50)
    st.write("**Easy Adoption**")
    st.write("Find your perfect pet and take them home the same day!")
with f2:
    st.image("https://cdn-icons-png.flaticon.com/512/690/690996.png", width=50)
    st.write("**Grooming Services**")
    st.write("Keep your pets healthy and happy with our professional grooming.")
with f3:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=50)
    st.write("**Pet Care Advice**")
    st.write("Get expert tips on caring for your furry friends.")

# Featured Pets
st.markdown('<a name="pets"></a>', unsafe_allow_html=True)
st.markdown("## 🐶 Featured Pets")
pet_cols = st.columns(3)
pets = [
    {
        "name": "Max",
        "type": "Dog",
        "desc": "2-year-old Labrador, friendly and energetic.",
        "img": "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Bella",
        "type": "Cat",
        "desc": "1-year-old Tabby, playful and loving.",
        "img": "https://images.unsplash.com/photo-1518715308788-3005759c81d8?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Snowy",
        "type": "Rabbit",
        "desc": "6-month-old Rabbit, gentle and cuddly.",
        "img": "https://images.unsplash.com/photo-1502672023488-70e25813f145?auto=format&fit=crop&w=400&q=80"
    },
]
for i, pet in enumerate(pets):
    with pet_cols[i]:
        st.markdown(f'<div class="pet-card">', unsafe_allow_html=True)
        st.markdown(f'<span class="tag">{pet["type"]}</span>', unsafe_allow_html=True)
        st.image(pet["img"], use_column_width=True, caption=pet["name"])
        st.write(pet["desc"])
        st.markdown(f'<button class="adopt-btn">Adopt Me</button>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Gallery
st.markdown("#### Our Happy Adoptions")
g1, g2, g3 = st.columns(3)
with g1:
    st.image("https://images.unsplash.com/photo-1518715308788-3005759c81d8?auto=format&fit=crop&w=200&q=80")
with g2:
    st.image("https://images.unsplash.com/photo-1518717758536-85ae29035b6d?auto=format&fit=crop&w=200&q=80")
with g3:
    st.image("https://images.unsplash.com/photo-1502672023488-70e25813f145?auto=format&fit=crop&w=200&q=80")

# About
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
st.markdown("## 🏪 About Us")
ab1, ab2 = st.columns([1,2])
with ab1:
    st.image("https://images.unsplash.com/photo-1518715308788-3005759c81d8?auto=format&fit=crop&w=400&q=80", use_column_width=True)
with ab2:
    st.write(
        "Paws & Claws Pet Shop is dedicated to helping pets find loving homes.\n\n"
        "We provide adoption, grooming, and pet care services. Visit us and meet your new best friend!"
    )
    st.markdown("""
    - 🐾 100+ Happy Adoptions
    - 🐾 Professional Staff
    - 🐾 Friendly Environment
    """)

# Contact
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown("## 📬 Contact Us")
c1, c2 = st.columns([1,2])
with c1:
    st.image("https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80", use_column_width=True)
with c2:
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        msg = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for contacting us! We'll get back to you soon.")

st.markdown(
    """
    <div class="footer">
        <img src="https://cdn-icons-png.flaticon.com/512/616/616408.png" alt="Footer Paw" width="28"/>
        <br>
        &copy; 2025 Paws & Claws Pet Shop. All rights reserved.<br>
        123 Pet Street, HappyTown | info@pawsclaws.com | +1 234 567 890
    </div>
    """, unsafe_allow_html=True
)
