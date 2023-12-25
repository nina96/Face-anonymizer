**Face Anonymizer Project Readme**

### Introduction

Welcome to the Face Anonymizer project! This robust tool is designed to help you easily anonymize faces in images, videos, or through your webcam using the powerful Mediapipe Face Detector.

### About Mediapipe Face Detector

Mediapipe Face Detector, developed by Google, is an advanced facial detection library that employs state-of-the-art machine learning models. Its accuracy and efficiency make it an excellent choice for identifying and locating faces in various multimedia contexts. In our project, we've seamlessly integrated this detector to provide a reliable and efficient face detection mechanism.

### Installation

Before you get started, ensure that you have the necessary dependencies installed. You can quickly install them by running the following command:

```bash
pip install -r requirement.txt
```

### Usage

The Face Anonymizer project incorporates two crucial parameters: `mode` and `filepath`.

- `mode`: This variable defines the type of input you wish to anonymize. It can take one of three values: 'image', 'video', or 'webcam' (default).

- `filepath`: This variable specifies the file path of the image or video you intend to process. For 'webcam' mode, you can leave it as the default value (None).

### Examples

#### Anonymize Faces in an Image

To anonymize faces in a specific image file, use the following command:

```bash
python main.py --mode image --filepath path/to/your/image.jpg
```

#### Anonymize Faces in a Video

For video anonymization, input the following command with the desired video file path:

```bash
python main.py --mode video --filepath path/to/your/video.mp4
```

#### Anonymize Faces via Webcam (Default)

If you wish to use your webcam for anonymization, simply execute the script without providing a file path:

```bash
python main.py
```

### Tips for Beginners

- Ensure you have Python installed on your system before running the script.
- In 'webcam' mode, the script uses the default webcam.
- For 'image' and 'video' modes, replace "path/to/your/image.jpg" or "path/to/your/video.mp4" with the actual file path.
- Experiment with different modes to gain familiarity with the face anonymizer.

Feel free to reach out if you have any questions or feedback. This Face Anonymizer project aims to make face anonymization accessible and effective. Happy face anonymizing! 🎭