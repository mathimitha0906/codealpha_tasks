"""
Main script for the Email Extractor automation tool.
"""
import sys
from automation.extractor import extract_emails_from_text, validate_email_list
from automation.file_handler import read_file, write_emails_to_file

def run_automation(input_file, output_file):
    """Orchestrates the email extraction process."""
    print(f"Starting extraction from: {input_file}")
    
    try:
        # 1. Read input
        content = read_file(input_file)
        
        # 2. Extract emails
        raw_emails = extract_emails_from_text(content)
        
        # 3. Validate/Clean emails
        clean_emails = validate_email_list(raw_emails)
        
        # 4. Save results
        if write_emails_to_file(clean_emails, output_file):
            print(f"Success! Extracted {len(clean_emails)} unique emails.")
            print(f"Results saved to: {output_file}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Default file names
    input_name = "input_text.txt"
    output_name = "extracted_emails.txt"
    
    print("=" * 40)
    print("PROFESSIONAL EMAIL EXTRACTOR TOOL")
    print("=" * 40)
    
    run_automation(input_name, output_name)
    print("=" * 40)

if __name__ == "__main__":
    main()
