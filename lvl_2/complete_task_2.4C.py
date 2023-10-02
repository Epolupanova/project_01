
def remove_word_with_one_em(s):
  words = s.split(' ')
  new_words = []
  for word in words:
    y = word.count('!')
    if y == 0 or y > 1:
      new_words.append(word)
  return ' '.join(new_words)

a = input('Введите текст: ')

print(remove_word_with_one_em(a))

