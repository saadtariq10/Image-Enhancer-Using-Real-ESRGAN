# Image Enhancer ✨

Enhance your images effortlessly using the advanced Real-ESRGAN model. This simple web app allows you to upload an image, choose an enhancement scale, and process it using state-of-the-art deep learning models for image upscaling.

## Features
- **Image Upload**: Upload your image in JPG, PNG, or JPEG format.
- **Enhancement Settings**: Choose from different enhancement scales (2x, 3x, 4x).
- **Real-ESRGAN Processing**: Enhance your image using the Real-ESRGAN model for improved resolution.
- **Download Enhanced Image**: After the image is enhanced, download the improved version with just a click.

## Requirements
To run this app locally, make sure you have the following libraries installed:

- Python 3.x
- Streamlit
- Pillow
- torch
- realesrgan

You can install the necessary Python libraries with:

```bash
pip install streamlit Pillow torch realesrgan
```

## How to Use
1. Clone or download this repository.
2. Install the required dependencies as mentioned above.
3. Run the Streamlit app by navigating to the directory and executing:

```bash
streamlit run app.py
```

4. Once the app opens in your browser, simply upload an image.
5. Select the enhancement scale (2x, 3x, or 4x).
6. Click on "Enhance Image" to start the image enhancement process.
7. After processing, download your enhanced image!

## Model Information
The app uses the [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) model for image enhancement. Make sure the weights for the Real-ESRGAN model are properly set (`RealESRGAN_x{scale}plus.pth`).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Powered by [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) for image enhancement.
- Built with ❤️ using [Streamlit](https://streamlit.io/).
