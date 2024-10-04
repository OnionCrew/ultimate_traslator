import re

def sort_words(text):
    words = re.findall(r'\b\w+\b', text)
    ukrainian_words = sorted([word for word in words if re.search(r'[а-яА-ЯїЇєЄіІ]', word)], key=str.casefold)
    english_words = sorted([word for word in words if re.search(r'[a-zA-Z]', word)], key=str.casefold)
    return ukrainian_words + english_words

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            sentence = file.readline().strip()
            print("Перше речення:", sentence)
            sorted_words = sort_words(sentence)
            print("Відсортовані слова:", sorted_words)
            print(f"Кількість слів: {len(sorted_words)}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


filename = "sort_file.txt"
read_file(filename)
