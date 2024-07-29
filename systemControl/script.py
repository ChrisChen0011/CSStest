import subprocess
import os

def open_application():
    app_path = '/Applications/Spotify.app'  # Replace with your application path
    subprocess.call(['open', app_path])  # Use subprocess for Mac compatibility

def main():
    file_path = 'example.txt'  # Replace with your file path
    try:
        with open(file_path, 'w') as file:
            # Write some content to the file
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")
            print(f"Content written to {file_path}.")
    except IOError as e:
        print(f"An error occurred trying to write to the file {file_path}: {e}")

if __name__ == "__main__":
    print("Running script...")
    open_application()