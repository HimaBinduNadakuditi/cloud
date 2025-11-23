# =====================================================
# REAL-TIME SENTIMENT ANALYZER (NO SKLEARN, IDLE SAFE)
# =====================================================

import re

# =====================================================
# 1. TEXT PREPROCESSING FUNCTION
# =====================================================

def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'http\S+|www\S+', '', text)   # Remove URLs
    text = re.sub(r'@\w+', '', text)             # Remove usernames
    text = re.sub(r'#', '', text)                # Remove hashtags
    text = re.sub(r'[^\w\s]', '', text)          # Remove punctuation
    text = re.sub(r'\d+', '', text)              # Remove numbers
    text = re.sub(r'\s+', ' ', text).strip()     # Remove extra spaces

    return text


# =====================================================
# 2. SENTIMENT DICTIONARIES (RULE-BASED)
# =====================================================

positive_words = [
    "love", "good", "great", "amazing", "happy", "like", "fantastic",
    "best", "wonderful", "excellent", "awesome", "positive"
]

negative_words = [
    "hate", "bad", "worst", "terrible", "poor", "sad", "angry",
    "unhappy", "regret", "negative", "awful", "disappointed"
]

neutral_words = [
    "okay", "fine", "average", "normal", "neutral", "nothing"
]


# =====================================================
# 3. PREDICTION FUNCTION (NO SKLEARN)
# =====================================================

def predict_sentiment(text):
    text = preprocess_text(text)
    words = text.split()

    pos_score = sum(1 for w in words if w in positive_words)
    neg_score = sum(1 for w in words if w in negative_words)
    neu_score = sum(1 for w in words if w in neutral_words)

    total = pos_score + neg_score + neu_score
    confidence = 0

    if total > 0:
        confidence = int((max(pos_score, neg_score, neu_score) / total) * 100)

    if pos_score > neg_score and pos_score > neu_score:
        return "positive", confidence
    elif neg_score > pos_score and neg_score > neu_score:
        return "negative", confidence
    else:
        return "neutral", confidence


# =====================================================
# 4. REAL-TIME USER INPUT (IDLE SAFE)
# =====================================================

print("\n===== REAL-TIME SENTIMENT ANALYSIS (NO SKLEARN) =====")
print("Type your sentence. Type 'exit' to stop.\n")

while True:
    user_text = input("Enter text: ")

    if user_text.lower() == "exit":
        print("Goodbye!")
        break

    sentiment, confidence = predict_sentiment(user_text)

    print(f"Sentiment: {sentiment.upper()} ({confidence}% confidence)\n")
