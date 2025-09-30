import streamlit as st


hitoo = {
    "image_url":"https://media.discordapp.net/attachments/968551920958599188/1422463774958555207/da350b614c630ba098a17e98f37e2a39.jpg?ex=68dcc420&is=68db72a0&hm=05940d66425415d1ab559eb5ef67d1563c74eb1393c2fb675064783e55dba601&=&format=webp&width=703&height=260"
}




st.title("오늘의 추천곡")
st.image(hitoo["image_url"])
st.link_button("오토 레이니☔ -  월광식당", "https://youtu.be/7bfiY4H0qoQ?si=0J-oUm4RcBPcYAmU")

