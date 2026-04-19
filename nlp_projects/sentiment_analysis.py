positive_words = {"good", "great", "excellent", "amazing", "love", "happy", "best"}
negative_words = {"bad", "terrible", "awful", "hate", "worst", "sad", "poor"}

text = "I love this product because it has amazing quality and great performance"

tokens = text.lower().split()
positive_count = sum(word in positive_words for word in tokens)
negative_count = sum(word in negative_words for word in tokens)

print("Text:", text)
print("Positive Count:", positive_count)
print("Negative Count:", negative_count)

if positive_count > negative_count:
    print("Sentiment: Positive")
elif negative_count > positive_count:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
