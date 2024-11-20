import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Streamlit interface
st.title("Affine Transformations with OpenCV")

# File uploader
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    try:
        # Convert the uploaded file to a NumPy array
        image = np.array(Image.open(uploaded_file))

        # Input: Choose a caption
        caption = st.selectbox(
            "Select a Caption for Your Image:",
            ["Original Image", "Translated Image", "Rotated Image", "Scaled Image", "Sheared Image"]
        )

        # Input: Provide a name for the image
        image_name = st.text_input("Enter the name for your image:", value="my_image")

        # Display the original image with the selected caption
        st.image(image, caption=f"{caption}: {image_name}", use_container_width=True)

        rows, cols, _ = image.shape

        # Perform transformations
        # Translation
        dx, dy = 50, 50
        translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
        translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))

        # Rotation
        angle = 45
        center = (cols // 2, rows // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

        # Scaling
        scale_x, scale_y = 1.5, 1.5
        scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

        # Shearing
        shear_factor = 0.2
        shear_matrix = np.float32([[1, shear_factor, 0], [shear_factor, 1, 0]])
        sheared_image = cv2.warpAffine(image, shear_matrix, (cols, rows))

        # Display transformations with the selected caption
        st.image(translated_image, caption=f"{caption}: Translated", use_container_width=True)
        st.image(rotated_image, caption=f"{caption}: Rotated", use_container_width=True)
        st.image(scaled_image, caption=f"{caption}: Scaled", use_container_width=True)
        st.image(sheared_image, caption=f"{caption}: Sheared", use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please upload an image file to proceed.")
