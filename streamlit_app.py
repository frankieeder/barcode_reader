import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode
from pillow_heif import register_heif_opener

register_heif_opener()

st.title("Handy Barcode Scanner")
st.write("Upload an image below to scan barcodes,"
         "Reveal it's content "
         "and click to search for the item(s) on a few common websites...")


st.markdown("---")
image = st.file_uploader("Upload photo here", label_visibility='hidden')
st.markdown("---")


def display_links(barcode):
    # TODO: Use cookies to allow users to paste their own custom links if needed
    st.header(f"Barcode: {barcode}")
    st.markdown(f"[Search on Amazon](https://www.amazon.com/s?k={barcode})")
    st.markdown(f"[Search on Discogs](https://www.discogs.com/search/?q={barcode})")
    st.markdown(f"[Search on AbeBooks](https://www.abebooks.com/servlet/SearchResults?kn={barcode})")
    st.markdown(f"[Search on ThriftBooks](https://www.thriftbooks.com/browse/?b.search={barcode})")
    # TODO: RateYourMusic.com?


if image is not None:
    im = Image.open(image)
    im_greyscale = im.convert('L')  # Convert to greyscale to enforce HEIC data
    barcodes = decode(im_greyscale)
    for barcode in barcodes:
        display_links(barcode.data.decode())

    if not barcodes:
        st.warning("No barcodes found, please try again and ensure any barcodes are clearly visible.")
