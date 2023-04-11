
def validar(s):
  w = list('hola')
  for i in s:
    if i.lower() != w[0]:
      w.pop(0)
      if i.lower() != w[0]:
        return False

  return True 

print(validar('HoLa'))
print(validar('hhhhooooollllllaaaaaa'))
print(validar('hhhlllllloooollllla'))
