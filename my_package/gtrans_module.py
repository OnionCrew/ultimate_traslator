from googletrans import Translator
from googletrans.models import Translated

translator = Translator()

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'hy': 'armenian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'ca': 'catalan',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'km': 'khmer',
    'ko': 'korean',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ml': 'malayalam',
    'mr': 'marathi',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'zu': 'zulu',
}

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translation: Translated = translator.translate(text, src=scr, dest=dest)
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"{detection.lang}, {detection.confidence}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    try:
        # Перевіряємо, чи це код мови
        if lang in LANGUAGES:
            return lang
        # Перевіряємо, чи це назва мови
        for code, name in LANGUAGES.items():
            if name.lower() == lang.lower():
                return code
        return "Error: Language not found"
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        header = f"{'N':<4} {'Language':<20} {'ISO-639 code':<10} {'Text':<40}\n"
        table = "-" * 60 + "\n"
        result = header + table

        translated_texts = []
        if text:
            translated_texts = [translator.translate(text, dest=code).text for code in LANGUAGES]

        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            translated = translated_texts[idx - 1] if text else ""
            result += f"{idx:<4} {lang:<20} {code:<10} {translated:<40}\n"

        if out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(result)
            return "Ok"
        else:
            print(result)
            return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
