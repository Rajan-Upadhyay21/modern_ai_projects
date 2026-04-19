import re

resume_text = """
Rajan Upadhyay
Email: rajan@example.com
Skills: Python, Machine Learning, Deep Learning, NLP
Education: Master's in Computer Science, Roosevelt University
"""

email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)
skills = re.findall(r"Python|Machine Learning|Deep Learning|NLP", resume_text)

print("Email Found:")
print(email)

print("\nSkills Found:")
print(skills)
