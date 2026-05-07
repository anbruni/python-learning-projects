words = [
    "apple", "banana", "apple", "cherry", "banana", "apple",
    "date", "elderberry", "fig", "banana", "cherry", "date"
]

# Your code here:
# 1. Build a dict: word -> count
word_count = {}

# 2. Print only words with count > 1, sorted alphabetically, in this format:
#    apple: 3
#    banana: 3
#    cherry: 2
#    date: 2
for word in words:
    if word not in word_count:
        word_count[word] = 0
    
    word_count[word] += 1

def my_filtering_function(pair):
    key, value = pair
    if value > 1:
        return True
    else:
        return False
 
word_count = dict(filter(my_filtering_function, sorted(word_count.items())))

for word, count in word_count.items():
  print(f"{word}: {count}")
