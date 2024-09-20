import json
import os
from my_package.deeptrans_module import TransLate, LangDetect


def read_config(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config


def analyze_text(file_path):

    if not os.path.isfile(file_path):
        return None

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    num_chars = len(text)
    num_words = len(text.split())
    num_sentences = text.count('.') + text.count('!') + text.count('?')

    return text, num_chars, num_words, num_sentences


def main():
    config = read_config('config.json')
    text_file = config['text_file']
    target_language = config['target_language']
    output = config['output']


    result = analyze_text(text_file)

    if result is None:
        print("Error: File not found.")
        return

    text, num_chars, num_words, num_sentences = result


    print(f"File: {text_file}, Size: {num_chars} characters, {num_words} words, {num_sentences} sentences")


    if num_chars > config['max_characters'] or num_words > config['max_words'] or num_sentences > config[
        'max_sentences']:
        print("Error: Text exceeds specified limits.")
        return


    detected_lang = LangDetect(text, set="lang")
    print(f"Detected language: {detected_lang}")


    translated_text = TransLate(text, detected_lang, target_language)


    if output == "screen":
        print(f"Translated Text:\n{translated_text}")
    elif output == "file":
        output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        print("Ok, translation saved to", output_file)
    else:
        print("Error: Invalid output option.")


if __name__ == "__main__":
    main()