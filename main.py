from spellchecker import SpellChecker

spell = SpellChecker()

word = input("enter the miss spell word:")

corrected_word = spell.correction(word)
print(corrected_word)
