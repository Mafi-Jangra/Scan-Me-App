import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="QR Code Generator", page_icon="🚀")

st.title("🔗 Instant QR Code Generator")
st.write("Enter a URL or text below to generate a custom QR code.")

# User Input
url = st.text_input("Enter your link or text:", placeholder="https://www.google.com")

if url:
    # QR Code Configuration
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create Image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to format Streamlit can display
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Display result
    st.image(byte_im, caption="Generated QR Code", use_column_width=False)

    # Download Button
    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="my_qr_code.png",
        mime="image/png"
    )