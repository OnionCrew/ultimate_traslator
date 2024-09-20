from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return "Confidence level not supported in langdetect"
        else:
            return detected_lang
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    try:
        translator = GoogleTranslator()  # Создаем экземпляр
        lang_dict = translator.get_supported_languages(as_dict=True)
        if lang in lang_dict:
            return lang_dict[lang]
        else:
            for code, name in lang_dict.items():
                if name == lang:
                    return code
        return "Error: Language not found"
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        translator = GoogleTranslator()
        lang_dict = translator.get_supported_languages(as_dict=True)
        result = f"{'N':<4} {'Language':<20} {'ISO-639 code':<10} {'Text':<40}\n" + "-" * 60 + "\n"

        if text:
            for idx, (code, lang) in enumerate(lang_dict.items(), start=1):
                translated = translator.translate(text, target=code)
                result += f"{idx:<4} {lang:<20} {code:<10} {translated:<40}\n"
        else:
            for idx, (code, lang) in enumerate(lang_dict.items(), start=1):
                result += f"{idx:<4} {lang:<20} {code:<10}\n"

        if out == "file":
            with open("deep_language_list.txt", "w", encoding="utf-8") as f:
                f.write(result)
            return "Ok"
        else:
            print(result)
            return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
