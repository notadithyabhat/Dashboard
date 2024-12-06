import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.title("EZ Training Dashboard") 
st.subheader("Welcome to the EZ Training Dashboard!")
st.subheader("Meet the Team")
team_members = {
    "Adithya": {
        "link": "https://www.linkedin.com/in/adithyabhat7/",
        "img": "https://media.licdn.com/dms/image/v2/D5603AQHviNaGneFvdQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1721661966979?e=1738800000&v=beta&t=RohJzfJTevRshMEOxmyV_RpZWp---2esIbmz1dTcUcY",
    },
    "Emily": {
        "link": "https://www.linkedin.com/in/emily-qiqiu/",
        "img": "https://media.licdn.com/dms/image/v2/D4E35AQGL-1KAhdGZyQ/profile-framedphoto-shrink_400_400/profile-framedphoto-shrink_400_400/0/1727676128812?e=1734134400&v=beta&t=ZM5VQfLvoFypDhdexTcfPRjHO2OfrRbEN8n7mNlO2Us",
    },
    "Zhao": {
        "link": "https://www.linkedin.com/in/shiyunyang-zhao/",
        "img": "https://media.licdn.com/dms/image/v2/D4E03AQFMksr8e5y82Q/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1724223257047?e=1738800000&v=beta&t=VZ8_fsg9OmpinZkcz6e83XblDBoB7vyC9m-ncmIEmSM",
    },
    "Gerson": {
        "link": "https://www.linkedin.com/in/gersonmoralesd/",
        "img": "https://media.licdn.com/dms/image/v2/D5603AQE7HFAXtVloyw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1727666744477?e=1738800000&v=beta&t=Kz-DfWpteYKd5uEp3xgpbzPNCgK9PrucNEMKAbrjYjc",
    },
    "Chloe": {
        "link": "https://www.linkedin.com/in/chuyun-deng-3308b8327/",
        "img": "https://media.licdn.com/dms/image/v2/D4D03AQHMLYiksaKOtw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1725584177775?e=1738800000&v=beta&t=z10YpJocU-VAwF4_7PK_Nkfd8Bwdm0dWIU-jqVpd8q0",
    },
    "Naga": {
        "link": "https://www.linkedin.com/in/vyjayanthipolapragada/",
        "img": "https://media.licdn.com/dms/image/v2/D5603AQEKKNZDDtM-hA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1714224906696?e=1738800000&v=beta&t=DWZ19-h5QQ5MoNgRkij-VhrMW2Ku_v03aTRUL4GW4ro",
    },
}

# Title
st.title("The EZ Training Dashboard Team")

# Display team members
st.markdown("### Created by the following students:")

# Render members in a grid format
for name, details in team_members.items():
    st.markdown(
        f"""
        <div style="text-align: center; width: 120px;">
            <a href="{details['link']}" target="_blank" style="text-decoration: none;">
                <img src="{details['img']}" alt="{name}" style="border-radius: 50%; width: 100px; height: 100px; object-fit: cover; margin-bottom: 10px;" />
                <div style="font-size: 16px; font-weight: bold; color: white;">{name}</div>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("""
Use the sidebar to navigate between pages:
- **Top Nutritionists**: Your initial Top Nutritionists Dashboard
- **Active Members**: Active Members' BMI Change and Workout Frequency Analysis
""")
