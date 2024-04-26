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

# Streamlit ile arayüz yerleşimi (col, tab, sidebar)
# bunun çalışması için yukardaki kodların yoruma alınması gerekir
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3><b> Kullanıcı Bilgileri </b></h3>", unsafe_allow_html=True)
    st.text_input(label="E-posta adresinizi giriniz: ")
    st.text_input(label="Şifrenizi Giriniz", type="password")
    st.checkbox(label="Şifremi Unuttum")
    st.divider()
    st.button(label="Giriş Yap")

with col2:
    st.markdown("<h3><b> Kullanım Tercihleri </b></h3>", unsafe_allow_html=True)
    st.divider()
    st.radio(label="Hesap Türü", options=["Öğrenci", "Mezun"])
    st.slider(label="Zaman Aşımı Süresi (saniye)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Güncel Özgeçmişinizi Yükleyiniz")

# tab versiyonu
# bunun çalışması için yukardaki kodların yoruma alınması gerekir

# sol tarafa kenar çubuğu ekleme
st.sidebar.markdown("<h4> Uygulamamıza Hoşgeldin! </h4>", unsafe_allow_html=True)
st.sidebar.image("1-image_sample.png")

tab1, tab2 = st.columns(2)
with tab1:

    st.text_input(label="E-posta adresinizi giriniz: ")
    st.text_input(label="Şifrenizi Giriniz", type="password")
    st.checkbox(label="Şifremi Unuttum")
    st.divider()
    st.button(label="Giriş Yap")

with tab2:
    st.radio(label="Hesap Türü", options=["Öğrenci", "Mezun"])
    st.slider(label="Zaman Aşımı Süresi (saniye)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Güncel Özgeçmişinizi Yükleyiniz")



















