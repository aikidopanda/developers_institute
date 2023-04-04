from translate import Translator
to_lang = 'en'
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator(from_lang='fr', to_lang='en')
translation = []
for i in range(len(french_words)):
    translation.append(translator.translate(french_words[i]))
# translation = Translator.translate(french_words)
print(translation)