import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Container for the team members */
    .team-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
    }

    /* Individual team member card */
    .team-card {
        background-color: var(--card-background);
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
        padding: 20px;
        transition: transform 0.2s, box-shadow 0.2s;
        width: 200px;
    }

    /* Hover effect for the card */
    .team-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }

    /* Team member image */
    .team-card img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin-bottom: 15px;
    }

    /* Team member name */
    .team-card .name {
        font-size: 18px;
        font-weight: bold;
        color: var(--text-color);
        margin-bottom: 10px;
    }

    /* Team member link */
    .team-card a {
        text-decoration: none;
    }

    /* Adjustments for dark and light themes */
    @media (prefers-color-scheme: dark) {
        :root {
            --card-background: #2c2c2c;
            --text-color: #ffffff;
        }
    }

    @media (prefers-color-scheme: light) {
        :root {
            --card-background: #ffffff;
            --text-color: #000000;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Overview
st.title("EZ Training Dashboard") 
st.markdown("""
### Overview
Welcome to the **EZ Training Dashboard**! This platform provides a comprehensive interface for analyzing and optimizing nutritionist and member performance metrics, empowering you to make data-driven decisions with ease.

### What You’ll Find Here
- **Top Nutritionists Dashboard**: Discover the top-performing nutritionists based on metrics like client health improvement and engagement.
- **Active Members Analysis**: Dive into detailed analytics on active members, including BMI trends, workout frequency, and overall progress.

### Features
- **Interactive Visualizations**: Easily filter and visualize data to uncover actionable insights.
- **Data Exploration Tools**: Gain deep insights into member health trends and nutritionist performance.
- **Customizable Filters**: Tailor your analysis with date ranges, performance metrics, and more.

### Setup Details
- **Database**: The data is hosted on Aiven, ensuring reliable and scalable database management.
- **GitHub**: The codebase is hosted on GitHub for easy collaboration and version control.
- **Streamlit App Deployment**: The dashboard is deployed on Streamlit's free tier, allowing for seamless access and interaction. Secret keys and other sensitive data are stored in Streamlit's secure environment.

### Contribute or Learn More
The source code for this project is available on [GitHub](https://github.com/notadithyabhat/ez-training-dashboard). Feel free to explore, contribute, or adapt the code for your own projects.

---
""")

# Subheader for Team Members
st.subheader("Meet the Team")

team_members = {
    "Adithya": {
        "link": "https://www.linkedin.com/in/adithyabhat7/",
        "img": "https://media.licdn.com/dms/image/v2/D5603AQHviNaGneFvdQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1721661966979?e=1738800000&v=beta&t=RohJzfJTevRshMEOxmyV_RpZWp---2esIbmz1dTcUcY",
    },
    "Chloe": {
        "link": "https://www.linkedin.com/in/chuyun-deng-3308b8327/",
        "img": "https://media.licdn.com/dms/image/v2/D4D03AQHMLYiksaKOtw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1725584177775?e=1738800000&v=beta&t=z10YpJocU-VAwF4_7PK_Nkfd8Bwdm0dWIU-jqVpd8q0",
    },
    "Emily": {
        "link": "https://www.linkedin.com/in/emily-qiqiu/",
        "img": "https://media.licdn.com/dms/image/v2/D4E35AQGL-1KAhdGZyQ/profile-framedphoto-shrink_400_400/profile-framedphoto-shrink_400_400/0/1727676128812?e=1734134400&v=beta&t=ZM5VQfLvoFypDhdexTcfPRjHO2OfrRbEN8n7mNlO2Us",
    },
    "Gerson": {
        "link": "https://www.linkedin.com/in/gersonmoralesd/",
        "img": "https://media.licdn.com/dms/image/v2/D5603AQE7HFAXtVloyw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1727666744477?e=1738800000&v=beta&t=Kz-DfWpteYKd5uEp3xgpbzPNCgK9PrucNEMKAbrjYjc",
    },
    
    "Naga": {
        "link": "https://www.linkedin.com/in/vyjayanthipolapragada/",
        "img": "https://media.licdn.com/dms/image/v2/D5603AQEKKNZDDtM-hA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1714224906696?e=1738800000&v=beta&t=DWZ19-h5QQ5MoNgRkij-VhrMW2Ku_v03aTRUL4GW4ro",
    },
    "Zhao": {
        "link": "https://www.linkedin.com/in/shiyunyang-zhao/",
        "img": "https://media.licdn.com/dms/image/v2/D4E03AQFMksr8e5y82Q/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1724223257047?e=1738800000&v=beta&t=VZ8_fsg9OmpinZkcz6e83XblDBoB7vyC9m-ncmIEmSM",
    }
}

# Display team members in a horizontal layout
cols = st.columns(len(team_members))

for i, (name, details) in enumerate(team_members.items()):
    with cols[i]:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{details['link']}" target="_blank" style="text-decoration: none;">
                    <img src="{details['img']}" alt="{name}" style="border-radius: 50%; width: 100px; height: 100px; object-fit: cover; margin-bottom: 10px;" />
                    <div style="font-size: 16px; font-weight: bold; color: grey;">{name}</div>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
