"""
This module handles file reading and writing operations.
"""
import os

def read_file(file_path):
    """Reads content from a file safely."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_emails_to_file(emails, output_path):
    """Writes a list of emails to a specified file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            if not emails:
                f.write("No emails found.\n")
            else:
                for email in emails:
                    f.write(f"{email}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False
