import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

st.title("Handy Barcode Scanner")
st.write("Upload an image below to scan barcodes, and search for the item(s) on a few common websites...")


st.markdown("---")
image = st.file_uploader("Upload photo here", label_visibility=False)
st.markdown("---")


def display_links(barcode):
    # TODO: Use cookies to allow users to paste their own custom links if needed
    st.header(f"Barcode: {barcode}")
    st.markdown(f"[Search on Amazon](https://www.amazon.com/s?k={barcode})")
    st.markdown(f"[Search on AbeBooks](https://www.abebooks.com/servlet/SearchResults?kn={barcode})")
    st.markdown(f"[Search on Discogs](https://www.discogs.com/search/?q={barcode})")
    # TODO: RateYourMusic.com?


if image is not None:
    barcodes = decode(Image.open(image))
    for barcode in barcodes:
        display_links(barcode.data)
