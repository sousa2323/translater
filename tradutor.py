from translate import Translator

s = Translator(from_lang="Portuguese", to_lang="English")
print(s.translate(input("Digite aqui... ")))