import streamlit as st
import os
from utils.compressor import binary_string_to_file, file_to_binary_string

def render_compressor():
    # Create an input for the decryption key
    key = st.text_input("Encryption Key", value=None)

    # Create a file uploader
    uploaded_file = st.file_uploader("Upload a file to compress", accept_multiple_files = False)

    if uploaded_file is not None:
        compress_button = st.button("Compress File")
        if compress_button:
            file_path = f"data/uploads/{uploaded_file.name}"
            bin_path = f"data/uploads/{uploaded_file.name}.bin"

            # Save the uploaded file
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
                
            # Run the function with the file path as an argument
            with st.spinner(text="Compressing File"):
                if key:
                    file_to_binary_string(file_path.encode(), bin_path.encode(), key.encode())
                else:
                    file_to_binary_string(file_path.encode(), bin_path.encode(), None)
                st.toast("File Compressed Successfully", icon='✅')
            
            # Clean up (delete the file) after processing
            os.remove(file_path)

            with open(bin_path, 'rb') as f:
                bytes = f.read()

            # Create a button for downloading the file
            download = st.download_button(
                label="Download File",
                data=bytes,
                file_name=str(os.path.basename(file_path)) + ".bin",
                mime='application/octet-stream',
            )
            if download:
                os.remove(bin_path)
                st.toast("File removed.", icon="❗")

def render_decompressor():
    # Create an input for the decryption key
    key = st.text_input("Decryption Key", value=None)

    # Create a file uploader
    uploaded_bin = st.file_uploader("Upload a file to decompress", accept_multiple_files = False)

    if uploaded_bin is not None:
        decompress_button = st.button("Deompress File")
        if decompress_button:
            file_path = f"data/uploads/{uploaded_bin.name}"
            output_path = f"data/uploads/{uploaded_bin.name}".replace(".bin","")

            # Save the uploaded file
            with open(file_path, "wb") as f:
                f.write(uploaded_bin.getbuffer())
                
            # Run the function with the file path as an argument
            with st.spinner(text="Compressing File"):
                if key:
                    binary_string_to_file(file_path.encode(), output_path.encode(), key.encode())
                else:
                    binary_string_to_file(file_path.encode(), output_path.encode(), None)
                st.toast("File Deompressed Successfully", icon='✅')
            
            # Clean up (delete the file) after processing
            os.remove(file_path)

            with open(output_path, 'rb') as f:
                bytes = f.read()

            # Create a button for downloading the file
            download = st.download_button(
                label="Download File",
                data=bytes,
                file_name=str(os.path.basename(output_path)),
                mime='application/octet-stream'
            )
            if download:
                os.remove(output_path)
                st.toast("File removed.", icon="❗")


tab1, tab2 = st.tabs(["Compress", "Decompress"])
with tab1:
    render_compressor()
with tab2:
    render_decompressor()