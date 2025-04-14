import streamlit as st
from PIL import Image, ImageOps
import io
from rembg import remove


st.title("Growth Mindset Challenge")
st.subheader("Image Background Remover and Editor")

upload_image = st.file_uploader("Upload An Image", type=["jpg", "jpeg", "png" ])

if upload_image is not None:

    img = Image.open(upload_image).convert("RGBA")
    st.image(img, caption="Original Image", use_column_width=True)

    if st.button("Remove Background"):
        img_no_bg = remove(upload_image.getvalue())
        img_no_bg = Image.open(io.BytesIO(img_no_bg)).convert("RGBA")
        st.image(img_no_bg, caption="Image with Background Removed", use_column_width=True)
        img = img_no_bg

    background_image = st.file_uploader("Upload a New Background Image", type=["jpg", "jpeg", "png" ])

    if background_image is not None:
        new_bg = Image.open(background_image).convert("RGBA")
        new_bg = new_bg.resize(img.size)

        img_alpha = img.split()[-1]

        combined_image = Image.new("RGBA", img.size)

        combined_image.paste(new_bg, (0, 0), new_bg)
        combined_image.paste(img, (0, 0), img_alpha)

        st.image(combined_image, caption="Combined Image", use_column_width=True)

        img = combined_image

    rotate_angle = st.slider("Rotate Image", 0, 360, 0)
    if rotate_angle:
        rotated_image = img.rotate(rotate_angle, expand=True)
        st.image(rotated_image, caption=f"Image Rotated by {rotate_angle} degrees", use_column_width=True)
        img = rotated_image

    if st.button("Crop Image to Square"):
        cropped_image = ImageOps.fit(img, (300, 300))
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)
        img = cropped_image

    if st.button("Download Image"):
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="output_image.png",
            mime="image/png"
        )

else:
    st.write("Please upload an image to get started.")


    st.markdown("---") 
    st.markdown(
        """
        <div style="text-align: center; color: #888888; padding: 20px;">
            <p>Growth Mindset Challenge | Version 1.0</p>
            <p style='font-size: 0.8em;'>© 2025 All rights reserved</p>
            <p style='font-size: 0.8em;'>Created by Ibraz Ur Rehman</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


