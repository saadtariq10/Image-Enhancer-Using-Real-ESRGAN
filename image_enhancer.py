# import streamlit as st
# from PIL import Image
# import os
# import subprocess

# # Title of the Streamlit app
# st.title("Image Enhancer")

# # Instructions
# st.write("Upload an image to enhance its quality using Real-ESRGAN models.")

# # Upload image
# uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

# # Specify enhancement options
# enhancement_options = ["x2", "x3", "x4"]
# selected_model = st.selectbox("Select enhancement scale (Real-ESRGAN model)", enhancement_options)

# # Enhance button
# if uploaded_file and st.button("Enhance Image"):
#     try:
#         # Get the absolute path of the current script directory
#         script_dir = os.path.dirname(os.path.abspath(__file__))

#         # Define paths for Real-ESRGAN executable and model directory
#         real_esrgan_exe = os.path.join(script_dir, "realesrgan-ncnn-vulkan.exe")
#         model_dir = os.path.join(script_dir, "models")
#         model_name = "realesrgan-x4plus"


#         # Save the uploaded image temporarily
#         input_path = os.path.join(script_dir, f"input_image.{uploaded_file.name.split('.')[-1]}")
#         output_path = os.path.join(script_dir, "enhanced_image.png")
#         input_image = Image.open(uploaded_file)
#         input_image.save(input_path)

#         # Debugging: Print paths (optional)
#         st.write(f"Model Directory: {model_dir}")
#         st.write(f"Model Name: {model_name}")
#         st.write(f"Input Image Path: {input_path}")
#         st.write(f"Output Image Path: {output_path}")

#         # Run Real-ESRGAN enhancement using subprocess
#         result = subprocess.run(
#             [
#                 real_esrgan_exe,
#                 "-i", input_path,
#                 "-o", output_path,
#                 "-n", model_name,
#                 "-m", model_dir
#             ],
#             check=True,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )

#         # Display enhanced image
#         st.image(output_path, caption="Enhanced Image", use_column_width=True)
#         st.success("Enhancement completed successfully!")

#         # Provide download link for the enhanced image
#         with open(output_path, "rb") as file:
#             st.download_button(
#                 label="Download Enhanced Image",
#                 data=file,
#                 file_name="enhanced_image.png",
#                 mime="image/png"
#             )

#     except subprocess.CalledProcessError as e:
#         st.error(f"Enhancement failed with error:\n{e.stderr.decode()}")
#     except Exception as e:
#         st.error(f"An unexpected error occurred: {e}")


















import streamlit as st
from PIL import Image
import os
import subprocess

# Set page configuration
st.set_page_config(
    page_title="Image Enhancer",
    page_icon="✨",
    layout="centered",
)

# Main container
with st.container():
    # Add a header with some styling
    st.markdown(
        """
        <h1 style="text-align: center; color: #4CAF50;">✨ Image Enhancer ✨</h1>
        <p style="text-align: center; color: #555;">Enhance your images effortlessly using advanced Real-ESRGAN models.</p>
        """,
        unsafe_allow_html=True,
    )

# Upload section
st.markdown("### 📤 Upload Your Image")
uploaded_file = st.file_uploader(
    "Choose an image file to enhance",
    type=["jpg", "png", "jpeg"],
    help="Supported formats: JPG, PNG, JPEG",
)

# Enhancement options section
st.markdown("### ⚙️ Choose Enhancement Settings")
enhancement_options = ["x2", "x3", "x4"]
selected_model = st.selectbox(
    "Select enhancement scale:",
    enhancement_options,
    help="Scale refers to the level of upscaling applied to the image.",
)

# Enhance button
if uploaded_file:
    st.markdown("### 🔮 Process Your Image")
    if st.button("Enhance Image"):
        with st.spinner("Enhancing your image... 🔄"):
            try:
                # Get the absolute path of the current script directory
                script_dir = os.path.dirname(os.path.abspath(__file__))

                # Define paths for Real-ESRGAN executable and model directory
                real_esrgan_exe = os.path.join(script_dir, "realesrgan-ncnn-vulkan.exe")
                model_dir = os.path.join(script_dir, "models")
                model_name = f"realesrgan-x4plus"

                # Save the uploaded image temporarily
                input_path = os.path.join(script_dir, f"input_image.{uploaded_file.name.split('.')[-1]}")
                output_path = os.path.join(script_dir, "enhanced_image.png")
                input_image = Image.open(uploaded_file)
                input_image.save(input_path)

                # Run Real-ESRGAN enhancement using subprocess
                result = subprocess.run(
                    [
                        real_esrgan_exe,
                        "-i", input_path,
                        "-o", output_path,
                        "-n", model_name,
                        "-m", model_dir,
                    ],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

                # Display enhanced image
                st.success("✨ Image enhanced successfully!")
                st.image(output_path, caption="Enhanced Image", use_column_width=True)

                # Provide download link for the enhanced image
                with open(output_path, "rb") as file:
                    st.download_button(
                        label="Download Enhanced Image",
                        data=file,
                        file_name="enhanced_image.png",
                        mime="image/png",
                    )

            except subprocess.CalledProcessError as e:
                st.error(f"Enhancement failed with error:\n{e.stderr.decode()}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

# Footer
st.markdown(
    """
    <hr>
    <p style="text-align: center; color: #888;">Powered by <b>Real-ESRGAN</b> | Created with ❤️ using <b>Streamlit</b></p>
    """,
    unsafe_allow_html=True,
)
