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

# https://docs.streamlit.io/

# Streamlit ile multimedya gösterme

st. image(image="1-image_sample.png")
st.video(data="2-video_sample.mp4")
# st.audio(data="ses-yolu")

# Streamlit ile kullanıcı etkileşimi (buton, radio, checkbox, slider, number input, file uploader)
st.write("lütfen bilgilerinizi giriniz")
st.text_input(label="lütfen e-posta adresinizi giriniz:")
st.text_input(label="lütfen şifrenizi giriniz:", type="password")
st.checkbox(label="Şifremi unuttum")
st.divider()
st.number_input(label="Lütfen yaşınızı girin:", min_value=18, max_value=40, value=22)
st.slider(label="Lütfen yaşınızı girin:", min_value=18, max_value=40, value=22)
st.button(label="Giriş Yap")
st.divider()
st.radio(label="Statünüz nedir? ", options=["Öğrenci", "Mezun"])
st.divider()
st.file_uploader(label="Dosya yüklemek için tıklayınız")





