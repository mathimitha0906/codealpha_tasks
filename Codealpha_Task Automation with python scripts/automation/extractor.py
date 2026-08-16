"""
This module contains the logic for extracting email addresses from text.
"""
import re

# Industry-standard regex for basic email extraction
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def extract_emails_from_text(text):
    """
    Finds all email addresses in the given text.
    Returns a sorted list of unique email addresses.
    """
    emails = re.findall(EMAIL_REGEX, text)
    # Use set to remove duplicates and then sort
    return sorted(list(set(emails)))

def validate_email_list(emails):
    """
    Performs additional validation on extracted emails if needed.
    Currently returns the list as is, but can be expanded.
    """
    return [email.lower() for email in emails]
