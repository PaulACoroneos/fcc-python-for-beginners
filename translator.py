def llama_translator(phrase):
  translated_phrase = ""
  for letter in phrase:
    if letter.lower() in 'aeiou':
      if letter.isupper():
        translated_phrase += 'L'
      else:
        translated_phrase += 'l'
    else:
      translated_phrase += letter

  return translated_phrase


print(llama_translator("giraffe"))