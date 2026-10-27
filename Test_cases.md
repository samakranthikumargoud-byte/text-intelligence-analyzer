Test Case 1: Standard / Mixed Text (Neutral Tone)
​Input: A standard paragraph containing common English words, some punctuation, and a mix of stop words.
​Expected Output: Accurate character/word/sentence count, correct top 5 keywords (ignoring stop words), and a Neutral / Informational tone.
​
Test Case 2: Positive / Encouraging Text
​Input: Text packed with positive words from your dictionary (e.g., amazing, powerful, successful, love, great).  
​Expected Output: pos_score > neg_score resulting in a Positive / Encouraging tone.
​
Test Case 3: Negative / Critical Text
​Input: Text packed with negative keywords from your dictionary (e.g., bad, difficult, error, fail, poor).  
​Expected Output: neg_score > pos_score resulting in a Negative / Critical tone.
