# python -m venv venv
# .\venv\Scripts\activate
# pip install -r requirements.txt
# python app.py
# streamlit run app.py => çalıştırmak için CTRL+C durdurmak için

# streamlit kütüphanesini ekleme
import streamlit as st

# streamlit uygulamasını başlatma
# st.write("Hello world")

# Streamlit ile sayfa bilgilerini düzenleme
# emoji sitesi https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# set_page_config komutu streamlit uygulamasında vermemzi gereken ilk komut olmalı yoksa hata verir
st.set_page_config(page_title="Streamlit 101", page_icon=":robot_face:")

# Streamlit ile metin gösterme
st.write("En yaygın metin gösterme yöntemi")

st.markdown("_Biçimlendirilmiş metin_")
st.header("Bu bir header örneğidir")
st.subheader("Bu bir subheader örneğidir")
st.code('for i in range(10): my_function()')
st.latex(r''' e^{i/pi} + 1 = 0 ''')




