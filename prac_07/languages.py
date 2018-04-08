from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = []
languages.append(ruby)
languages.append(python)
languages.append(visual_basic)

print("The dynamically typed languages are:")
for language in languages:
    if language.typing == "Dynamic":
        print(language.name)

# dynamic_languages = [language.name for language in languages if language.typing == "Dynamic"]
# for i in range(len(dynamic_languages)):
#     print(dynamic_languages[i])