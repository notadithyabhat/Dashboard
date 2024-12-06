import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.title("EZ Training Dashboard") 
st.subheader("Welcome to the EZ Training Dashboard!")
st.subheader("Meet the Team")
team_members = {
    "Adithya": {"link": "https://www.linkedin.com/in/adithyabhat7/", "img": "https://media-exp1.licdn.com/dms/image/C4E03AQH7U8dW7XpD9g/profile-displayphoto-shrink_200_200/0/1622164444951?e=1638403200&v=beta&t=Qb0q1zG0Gv3qQrF6C7qJyOQv8h6rRcFqYbZmCm6F_8p"},
    "Emily": {"link": "https://www.linkedin.com/in/emily-qiqiu/", "img": "https://media-exp1.licdn.com/dms/image/C4D03AQG7h2QYVbQq5A/profile-displayphoto-shrink_200_200/0/1622164444951?e=1638403200&v=beta&t=Qb0q1zG0Gv3qQrF6C7qJyOQv8h6rRcFqYbZmCm6F_8p"},
    "Zhao": {"link": "https://www.linkedin.com/in/shiyunyang-zhao/", "img": "https://media-exp1.licdn.com/dms/image/C4E03AQEJm3HkVbQq5A/profile-displayphoto-shrink_200_200/0/1622164444951?e=1638403200&v=beta&t=Qb0q1zG0Gv3qQrF6C7qJyOQv8h6rRcFqYbZmCm6F_8p"},
    "Gerson": {"link": "https://www.linkedin.com/in/gersonmoralesd/", "img": "https://media-exp1.licdn.com/dms/image/C4E03AQGZd3HkVbQq5A/profile-displayphoto-shrink_200_200/0/1622164444951?e=1638403200&v=beta&t=Qb0q1zG0Gv3qQrF6C7qJyOQv8h6rRcFqYbZmCm6F_8p"},
    "Chloe": {"link": "https://www.linkedin.com/in/chuyun-deng-3308b8327/", "img": "https://media-exp1.licdn.com/dms/image/C4D03AQH7U8dW7XpD9g/profile-displayphoto-shrink_200_200/0/1622164444951?e=1638403200&v=beta&t=Qb0q1zG0Gv3qQrF6C7qJyOQv8h6rRcFqYbZmCm6F_8p"},
    "Naga": {"link": "https://www.linkedin.com/in/vyjayanthipolapragada/", "img": "https://media-exp1.licdn.com/dms/image/C5603AQFzV3HkVbQq5A/profile-displayphoto-shrink_200_200/0/1622164444951?e=1638403200&v=beta&t=Qb0q1zG0Gv3qQrF6C7qJyOQv8h6rRcFqYbZmCm6F_8p"}
}
st.write("The EZ Training Dashboard was created by the following students:")
for name, info in team_members.items():
    st.write(f"[![{name}](https://media-exp1.licdn.com/dms/image/{info['img']} )]({info['link']})")
st.markdown("""
Use the sidebar to navigate between pages:
- **Top Nutritionists**: Your initial Top Nutritionists Dashboard
- **Active Members**: Active Members' BMI Change and Workout Frequency Analysis
""")
