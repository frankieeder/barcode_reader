import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

image = st.file_uploader("Upload a photo...")
barcodes = decode(Image.open(image))
st.write(barcodes)

for barcode in barcodes:
    st.write(barcode.data)
