✨ Image Enhancer Using Real-ESRGAN
This project is a user-friendly web app for enhancing and upscaling images using Real-ESRGAN models. Built with Streamlit, the app provides a clean interface for uploading images, selecting enhancement scales, and downloading enhanced versions.

🚀 Features
Upload & Enhance: Easily upload low-resolution images and enhance them with AI.
Multiple Scales: Choose from x2, x3, or x4 enhancement scales.
Download Enhanced Image: Get the high-resolution output with a single click.
Intuitive UI: Designed with Streamlit for a seamless user experience.
🛠️ Setup & Usage
Prerequisites
Install Python: Ensure Python 3.8+ is installed on your system.

Clone the repository:

git clone https://github.com/saadtariq10/Image-Enhancer-Using-Real-ESRGAN.git
cd Image-Enhancer-Using-Real-ESRGAN
Install required dependencies:

pip install -r requirements.txt
Add Real-ESRGAN Executable and Models:

Place the realesrgan-ncnn-vulkan.exe file in the project directory.
Place the models folder (containing .bin and .param files) in the project directory.
Run the App Locally
Start the app:

streamlit run app.py
Open the app in your browser at http://localhost:8501.

🌐 Deployment on Streamlit Cloud
Push your project to GitHub:

git add .
git commit -m "Initial commit"
git push origin main
Go to Streamlit Cloud.

Create a new app and connect your GitHub repository.

Add the realesrgan-ncnn-vulkan.exe file and models folder to the repository.

Deploy the app and access your Streamlit-hosted URL.

📂 Project Structure
image-enhancer/
├── models/                     # Real-ESRGAN model files (bin & param)
├── app.py                      # Main Streamlit app code
├── realesrgan-ncnn-vulkan.exe  # Real-ESRGAN executable
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
🖼️ Preview
Include a screenshot of your app here or link to the live demo (e.g., on Streamlit Cloud).

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

✨ Credits
Real-ESRGAN: AI model for super-resolution.
Streamlit: Framework for building interactive web apps.
Feel free to update this README.md file with additional details or your own branding!

Requirements File (requirements.txt)
Make sure to include a requirements.txt file in your repository with the following contents:

streamlit
torch
realesrgan
Pillow
