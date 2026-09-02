import streamlit as st
import pandas as pd
from datetime import date
import urllib.parse
import requests  # <-- Added at the top

# Page Configuration
st.set_page_config(
    page_title="Baddie and Badda",
    page_icon="✈️",
    layout="wide"
)

# Custom Styling with Graffiti Google Font and Bright Yellow Hindi Title
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Modak&family=Yatra+One&display=swap');

    .main-title {
        font-family: 'Modak', 'Yatra One', cursive;
        font-size: 4.2rem;
        color: #FFE600; /* Bright Yellow */
        text-align: center;
        letter-spacing: 2px;
        line-height: 1.2;
        text-shadow: 
            4px 4px 0px #000000,
           -4px -4px 0px #000000,
            4px -4px 0px #000000,
           -4px 4px 0px #000000,
            8px 8px 0px #FA0707; /* Graffiti Pop Shadow */
        margin-bottom: 10px;
    }
    .tagline {
        font-size: 1.3rem;
        text-align: center;
        color: #DDDDDD;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .desi-card {
        background-color: #1A1A1A;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #FFE600;
        margin-bottom: 1rem;
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# Header in Hindi with Graffiti Style
st.markdown("<div class='main-title'> बैडी और बड्डा </div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>mazee karwa denge!!</div>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=400", use_container_width=True)
st.sidebar.title("📌 Ki Baat Hai ")
nav = st.sidebar.radio("Go to:", ["🏠 Home", "🗺️ Tour Packages", "📝 Book Your Safar", "📞 Contact Us"])

# Data: Tour Packages
tours = {
    "Goa Chill & Chilling": {
        "price": "₹14,999",
        "duration": "4 Nights / 5 Days",
        "vibes": "Shacks, Fenny, Beach Sunset, Baddie Party Beats",
        "itinerary": [
            "Day 1: Arrival & Welcome Drinks (Chill at Baga)",
            "Day 2: South Goa Heritage & Quiet Beaches",
            "Day 3: Water Sports at Calangute & Sunset Cruise",
            "Day 4: Full Night Party at Curlies",
            "Day 5: Souvenir Shopping & Departure"
        ]
    },
    "Manali - Pahad & Chai Vibe": {
        "price": "₹18,500",
        "duration": "5 Nights / 6 Days",
        "vibes": "Maggi at Solang, Snow, Warm Cafe Corners",
        "itinerary": [
            "Day 1: Overnight Volvo journey from Delhi",
            "Day 2: Check-in & Old Manali Cafe Hopping",
            "Day 3: Solang Valley Snow Sports",
            "Day 4: Kasol & Manikaran Sahib Day Trip",
            "Day 5: Local Sightseeing & Mall Road Shopping",
            "Day 6: Return Journey"
        ]
    },
    "Jaipur & Udaipur - Shahi Andaaz": {
        "price": "₹22,000",
        "duration": "5 Nights / 6 Days",
        "vibes": "Palaces, Laal Maas, Royal Fort Photoshoots",
        "itinerary": [
            "Day 1: Royal Welcome in Jaipur & Amber Fort",
            "Day 2: Hawa Mahal, City Palace & Local Bazars",
            "Day 3: Scenic Drive to Udaipur (City of Lakes)",
            "Day 4: Boat Ride on Lake Pichola & City Palace",
            "Day 5: Saheliyon Ki Bari & Sunset at Monsoon Palace",
            "Day 6: Departure with Shahi Memories"
        ]
    }
}

# --- HOME PAGE ---
if nav == "🏠 Home":
    st.subheader(" Popular Safar Destinations")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=400", caption="Goa Beach Vibes")
        st.markdown("**Goa Chill & Chilling**")
        st.caption("Starting at ₹14,999")
        
    with col2:
        st.image("https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=400", caption="Manali Snow & Mountains")
        st.markdown("**Manali Pahad Vibe**")
        st.caption("Starting at ₹18,500")

    with col3:
        st.image("https://images.unsplash.com/photo-1477587458883-47145ed94245?w=400", caption="Rajasthan Royal Heritage")
        st.markdown("**Jaipur & Udaipur Shahi Trip**")
        st.caption("Starting at ₹22,000")

    st.markdown("---")
    st.markdown("### 💡 Why Baddie & Badda?")
    st.write("✔️ **Alcohol:** Sab bhai ek sath daru piyenge")
    st.write("✔️ **Photography:** Naa aata ho toh sikha bhi denge")
    st.write("✔️ **Authentic Cusine:** Khud cook karke khilayenge")
    st.write("✔️ **Treking and Camping:** Mazee karwa denge")
    st.write("✔️ **Drugs:** Fukwaa denge")
    st.write("✔️ **24/7 Jugaad Support:** Stuck somewhere? Badda is just one call away.")

# --- TOUR PACKAGES PAGE ---
elif nav == "🗺️ Tour Packages":
    st.subheader("🎒 Detailed Itineraries")
    
    selected_tour = st.selectbox("Select a package to explore:", list(tours.keys()))
    tour = tours[selected_tour]
    
    st.markdown(f"### {selected_tour}")
    st.markdown(f"**Price:** {tour['price']} per person | **Duration:** {tour['duration']}")
    st.markdown(f"**Vibe Check:** *{tour['vibes']}*")
    
    st.write("#### 📍 Day-by-Day Itinerary:")
    for step in tour['itinerary']:
        st.write(f"- {step}")
        
    st.info("💡 Tip: Want to customize this tour? Contact Badda directly via the Contact tab!")

# --- ONLINE BOOKING PAGE ---
elif nav == "📝 Book Your Safar":
    st.subheader("⚡ Book Your Spot Now")
    st.caption("Fill in your details below to lock in your trip with Badda!")

    with st.form("booking_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Full Name*", placeholder="e.g. Rahul Sharma")
            email = st.text_input("Email Address*", placeholder="rahul@example.com")
            phone = st.text_input("WhatsApp Number*", placeholder="+91 98765 43210")
            
        with col2:
            chosen_tour = st.selectbox("Select Destination", list(tours.keys()))
            travel_date = st.date_input("Travel Date", min_value=date.today())
            guests = st.number_input("Number of Travellers", min_value=1, max_value=20, value=2)

        special_requests = st.text_area(
            "Special Requests / Notes", 
            placeholder="Let us know about dietary needs, extra beds, or special arrangements..."
        )
        
        submitted = st.form_submit_button("🚀 Submit Booking Request", use_container_width=True)

    if submitted:
        if not full_name or not email or not phone:
            st.error("Please fill in all required fields marked with *.")
        else:
            st.success("Booking request submitted! Check your email for confirmation.")
# --- CONTACT PAGE ---
elif nav == "📞 Contact Us":
    st.subheader("🤙 Bol Bhai Ki Baat Hai")
    
    col_x, col_y = st.columns(2)
    
    with col_x:
        st.markdown("""
        **Head Office (Baddie and Badda's Den):**  
        Suite 420, Connaught Place, New Delhi, India 🇮🇳  
        
        **WhatsApp / Call:**  
        +91 99009 990099
        
        **Email:**  
        safarbaddieandbadda@gmail.com
        
        **Instagram:**  
        `@baddie_and_badda_travels`
        """)
        
    with col_y:
        st.markdown("<div class='desi-card'>", unsafe_allow_html=True)
        st.markdown("### 💬 Quick Inquiry")
        st.text_input("Your Name")
        st.text_area("Message")
        st.button("Send Message")
        st.markdown("</div>", unsafe_allow_html=True)