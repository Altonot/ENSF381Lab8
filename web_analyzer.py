import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter

# 1. User Input
url = input("Enter the URL (default is UCalgary Wikipedia): ").strip()
if not url:
    url = "https://en.wikipedia.org/wiki/University_of_Calgary"

# 2. Fetch & Parse HTML
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"✅ Successfully fetched content from {url}")
except Exception as e:
    print(f"❌ Error fetching content: {e}")
    exit()

# 3. Count Tags
headings = sum(len(soup.find_all(f'h{i}')) for i in range(1, 7))
links = len(soup.find_all('a'))
paragraphs = len(soup.find_all('p'))

print(f"\n📊 Tag Analysis:")
print(f"Headings: {headings}")
print(f"Links: {links}")
print(f"Paragraphs: {paragraphs}")

# 4. Keyword Search
keyword = input("\n🔍 Enter a keyword to search in page content: ").lower()
text_content = soup.get_text().lower()
keyword_count = text_content.count(keyword)
print(f"The keyword '{keyword}' appears {keyword_count} times.")

# 5. Word Frequency Analysis
words = text_content.split()
word_freq = Counter(words)
top_5 = word_freq.most_common(5)
print("\n📈 Top 5 most frequent words:")
for word, freq in top_5:
    print(f"{word}: {freq}")

# 6. Longest Paragraph
paragraphs_list = soup.find_all('p')
max_paragraph = ""
max_word_count = 0

for p in paragraphs_list:
    paragraph_text = p.get_text().strip()
    word_count = len(paragraph_text.split())
    if word_count > max_word_count and word_count >= 5:
        max_paragraph = paragraph_text
        max_word_count = word_count

print("\n📝 Longest Paragraph:")
print(max_paragraph)
print(f"\nWord count: {max_word_count}")

# 7. Visualization
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]

plt.bar(labels, values)
plt.title('Lab08 - Group12') 
plt.ylabel('Count')
plt.show()
