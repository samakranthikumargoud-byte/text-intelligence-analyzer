Hey! This is a lightweight Python command-line utility I built to analyze text files, pull document statistics, check readability, filter out common stop words, and run a quick keyword-based tone/sentiment check.
Detailed Document Statistics: Counts characters (with and without spaces), total words, sentences, and paragraphs.
Estimated Reading Time: Automatically calculates how long it takes to read based on an average speed of 200 words per minute.
Word Frequency Analysis: Filters out common stop words and pulls the top 5 most frequent meaningful keywords.

Keyword-Based Sentiment / Tone Check: Evaluates text against predefined positive and negative word lists to classify the tone as:
​Positive / Encouraging  
​Negative / Critical  
​Neutral / Informational  

​Clean Terminal Output: Formats results neatly into structured sections using custom console dividers.

text-intelligence-analyzer/
│
├── main.py        # Core logic and command-line execution script
└── sample.txt     # Default text file analyzed by the utility

Clone my repository:
 Linkedin (Kranthi@9550): git clone https://github.com/samakranthikumargoud-byte/text-intelligence-analyzer.git
cd text-intelligence-analyzer
