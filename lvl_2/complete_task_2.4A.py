
def remove_exclamation_marks(s):
  x = s.replace("!","")
  return x

a = input('Введите текст: ')

print(remove_exclamation_marks(a))
