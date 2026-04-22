feedback = [
    {"prediction_id": 1, "user_feedback": "correct"},
    {"prediction_id": 2, "user_feedback": "incorrect"},
    {"prediction_id": 3, "user_feedback": "correct"},
    {"prediction_id": 4, "user_feedback": "incorrect"}
]

correct_feedback = sum(item["user_feedback"] == "correct" for item in feedback)
feedback_accuracy = correct_feedback / len(feedback)

print("User Feedback Loop:")
print("Feedback Agreement Rate:", feedback_accuracy)
for item in feedback:
    print(item)
