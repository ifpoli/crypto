import random

filename = "tests/book.txt"

file = open(filename, 'rt')
text = file.read()
file.close()
words = text.split()
words = [w.lower() for w in words]
import string
table = str.maketrans('','',string.punctuation)
stripped = [w.translate(table) for w in words]
(stripped[:15])

book_text = " ".join(stripped)
book_text[:103]

text_len = len(book_text) // 2
print("Длина книги:", text_len)

meaningful_text1 = book_text[:10000]
with open("tests/meaningful1.txt", 'w') as f:
    f.write(meaningful_text1)
    
meaningful_text2 = book_text[10000:2*10000]
with open("tests/meaningful2.txt", 'w') as f:
    f.write(meaningful_text2)
    
def generate_random_chars(alphabet, lenght):
    ans = ""
    max_idx = len(alphabet) - 1
    for _ in range(lenght):
        ans += alphabet[random.randint(0, max_idx)]
    return ans
    
alphabet = [chr(ord("а") + i) for i in range(32)]

random_text1 = generate_random_chars(alphabet, 10000)
with open("tests/random1.txt", 'w') as f:
    f.write(random_text1)
    
random_text2 = generate_random_chars(alphabet, 10000)
with open("tests/random2.txt", 'w') as f:
    f.write(random_text2)
    
def generate_random_words(base, lenght):
    gen_len = 0
    ans = ""
    while gen_len < lenght:
        possible_words = list(filter(lambda x: len(x) <= lenght - gen_len, base))
        idx = random.randint(0, len(possible_words)-1)
        ans += possible_words[idx]
        gen_len += len(possible_words[idx])
        if gen_len < lenght:
            ans += " "
            gen_len += 1
    return ans

word_base = list(set(stripped))

words_text1 = generate_random_words(word_base, 10000)
with open("tests/words1.txt", 'w') as f:
    f.write(words_text1)
    
words_text2 = generate_random_words(word_base, 10000)
with open("tests/words2.txt", 'w') as f:
    f.write(words_text2)
    
def compare_texts(text1, text2):
    lenght = len(text1)
    equals = 0
    for i in range(lenght):
        if text1[i] == text2[i]:
            equals += 1
    return equals / lenght
    
ans = compare_texts(meaningful_text1, meaningful_text2)
print(f"Два осмысленных текста : {ans * 100:.2f}%")

ans = compare_texts(meaningful_text1, random_text1)
print(f"Осмысленный текст и текст из случайных букв: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text1, random_text2)
print(f"Осмысленный текст и текст из случайных букв: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text2, random_text1)
print(f"Осмысленный текст и текст из случайных букв: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text2, random_text2)
print(f"Осмысленный текст и текст из случайных букв: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text1, words_text1)
print(f"Осмысленный текст и текст из случайных слов: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text1, words_text2)
print(f"Осмысленный текст и текст из случайных слов: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text2, words_text1)
print(f"Осмысленный текст и текст из случайных слов: {ans * 100:.2f}%")

ans = compare_texts(meaningful_text2, words_text2)
print(f"Осмысленный текст и текст из случайных слов: {ans * 100:.2f}%")

ans = compare_texts(random_text1, random_text2)
print(f"Два текста из случайных букв: {ans * 100:.2f}%")

ans = compare_texts(words_text1, words_text2)
print(f"Два текста из случайных слов: {ans * 100:.2f}%")
