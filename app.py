import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Maulana Ibrahim – Portofolio", page_icon="⛰️", layout="wide",
                   initial_sidebar_state="collapsed")

base = Path(__file__).parent

# Tampilkan halaman HTML layar penuh (foto disematkan langsung supaya pasti muncul)
html = (base / "halaman.html").read_text(encoding="utf-8")
foto = base / "foto.jpg"
if foto.exists():
    b64 = base64.b64encode(foto.read_bytes()).decode()
    html = html.replace('src="foto.jpg"', f'src="data:image/jpeg;base64,{b64}"')

st.markdown("""
<style>
#MainMenu,footer,header,[data-testid="stToolbar"],[data-testid="stDecoration"]{display:none!important;}
.block-container,[data-testid="stMainBlockContainer"]{padding:0!important;max-width:100%!important;}
[data-testid="stMain"],.stApp{overflow:hidden!important;background:#F5F8F9;}
iframe{position:fixed!important;inset:0;width:100vw!important;height:100vh!important;height:100dvh!important;border:0;z-index:100;}
</style>
""", unsafe_allow_html=True)

components.html(html, height=900, scrolling=True)
