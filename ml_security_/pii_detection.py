import re

text = """
Name: Rajan Upadhyay
Email: rajan@example.com
Phone: +1 312-555-7890
"""

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
phone_pattern = r"\+?\d[\d\-\s]{7,}\d"

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("Detected Emails:")
print(emails)

print("\nDetected Phone Numbers:")
print(phones)
