import string

def analyze_text(text):
    """Analyzes text and returns statistics, word frequency, and basic tone."""
    
    # 1. Basic Counts
    char_count = len(text)
    char_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    paragraphs = [p for p in text.split("\n") if p.strip()]
    paragraph_count = len(paragraphs)
    
    sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    sentence_count = len(sentences)
    
    # Clean text for word processing
    # Remove punctuation and convert to lowercase
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()
    word_count = len(words)
    
    # 2. Estimated Reading Time (Assuming average reading speed of 200 words per minute)
    reading_time_seconds = (word_count / 200) * 60
    
    # 3. Word Frequency (Top 5 most common words)
    # Filter out common stop words to make insights more meaningful
    stop_words = {"the", "is", "at", "which", "and", "a", "an", "in", "it", "to", "for", "of", "with", "on"}
    filtered_words = [word for word in words if word not in stop_words]
    
    word_freq = {}
    for word in filtered_words:
        word_freq[word] = word_freq.get(word, 0) + 1
        
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_words[:5]
    
    # 4. Basic Sentiment / Tone Check (Keyword-based)
    positive_words = {"amazing", "powerful", "versatile", "easy", "clean", "success", "good", "great", "love", "help"}
    negative_words = {"bad", "hard", "difficult", "issue", "error", "fail", "slow", "poor"}
    
    pos_score = sum(1 for word in words if word in positive_words)
    neg_score = sum(1 for word in words if word in negative_words)
    
    if pos_score > neg_score:
        tone = "Positive / Encouraging "
    elif neg_score > pos_score:
        tone = "Negative / Critical "
    else:
        tone = "Neutral / Informational "

    # Compile Results
    report = {
        "char_count": char_count,
        "char_no_spaces": char_no_spaces,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "reading_time_seconds": round(reading_time_seconds, 2),
        "top_words": top_words,
        "tone": tone
    }
    
    return report

def main():
    print("=" * 50)
    print("      PRJ-09: TEXT INTELLIGENCE ANALYZER      ")
    print("=" * 50)
    
    # Read from sample.txt
    try:
        with open("sample.txt", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: sample.txt not found. Please create one.")
        return

    print("\n[INFO] Analyzing 'sample.txt'...\n")
    results = analyze_text(content)
    
    # Display Results neatly
    print(f"--- DOCUMENT STATISTICS ---")
    print(f"• Total Characters (with spaces): {results['char_count']}")
    print(f"• Total Characters (no spaces):   {results['char_no_spaces']}")
    print(f"• Total Words:                    {results['word_count']}")
    print(f"• Total Sentences:                {results['sentence_count']}")
    print(f"• Total Paragraphs:               {results['paragraph_count']}")
    print(f"• Estimated Reading Time:         {results['reading_time_seconds']} seconds")
    
    print(f"\n--- INTELLIGENCE INSIGHTS ---")
    print(f"• Detected Tone / Sentiment:      {results['tone']}")
    print(f"• Top Frequent Keywords (Filtered):")
    for word, freq in results['top_words']:
        print(f"  - '{word}': {freq} times")
    print("=" * 50)

if __name__ == "__main__":
    main()