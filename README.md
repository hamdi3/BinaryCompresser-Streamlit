# BinaryCompresser-Streamlit
[![Powered by Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-ff69b4)](https://www.streamlit.io/)
[![Deployment](https://img.shields.io/badge/Deployment-Streamlit-blueviolet)](https://streamsign.streamlit.app/)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](https://your-url)

Welcome to BinaryCompresser-Streamlit, a User interface for the [BinaryCompresser Project](https://github.com/hamdi3/BinaryCompresser) i did.

## Overview

BinaryCompresser-Streamlit is a userfriendly UI for BinaryCompresser, which is a C++ project that provides file compression and decompression functionality. It uses the zlib library for compression and decompression, and offers optional encryption based on the Vernam cipher.

## Features
The website consists of two tabs:
- Compression:
  - The user can upload a file up to 200 mbs
  - There's an optional input field for an encryption key
  - After the file is uploaded the compression process starts
  - The user can download the binary file
- Decomression:
  - The user can upload the binary file
  - There's an optional input field for an encryption key
  - After the file is uploaded the decompression process starts
  - The user can download the decompressed file

## Getting Started
To get started with StreamSign, follow these steps:
1. Clone the repository: `https://github.com/hamdi3/BinaryCompresser-Streamlit.git`
2. Install the required dependencies: `pip install streamlit`
3. Run the application: `streamlit run app.py`
4. Open your web browser and navigate to `http://localhost:8501` to access the StreamSign interface.

## Contributing

We welcome and appreciate contributions to make BinaryCompresser-Streamlit even better! To contribute, please follow these guidelines:

### How to Contribute

1. Fork the repository to your GitHub account.

2. Clone your fork to your local machine:

   ```bash
   git clone https://github.com/hamdi3/BinaryCompresser-Streamlit.git
   cd BinaryCompresser-Streamlit
   ```

3. Create a new branch for your feature or bug fix:

    ```bash
    Copy code
    git checkout -b feature-branch
    ```

4. Make your changes and ensure the code follows the project's coding standards.

5. Commit your changes with a clear and concise commit message:

    ```bash
    Copy code
    git commit -m "Your informative commit message"
    ```

6. Push your changes to your fork:

    ```bash
    Copy code
    git push origin feature-branch
    ```

7. Create a pull request (PR) from your fork to the main repository.

## License

This project is released under the [Unlicensed](LICENSE). You are free to copy, modify, and distribute the code, even for commercial purposes, without asking for permission. See the [Unlicensed](LICENSE) file for more details.


Happy coding!
