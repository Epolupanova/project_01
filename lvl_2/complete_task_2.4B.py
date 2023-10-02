
def remove_last_em(s):
  if s[-1] == '!':
    x = s[0:-1]
  else:
    x = s
  return x

a = input('Введите текст: ')

print(remove_last_em(a))
