
from my_package.deeptrans_module import TransLate, LangDetect, CodeLang, LanguageList

if __name__ == "__main__":
    print(TransLate("Hello", "en", "uk"))
    print(LangDetect("Привіт", "all"))
    print(CodeLang("uk"))
    print(LanguageList("screen", "Добрий день"))
