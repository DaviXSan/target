def inverter_string(string): 
  string_invertida = ""
  for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]
  return string_invertida

# Exemplo:
minha_string = "Serei o próximo contratado da Target"
string_invertida = inverter_string(minha_string)
print(string_invertida)  # Saída: tegraT ad odatartnoc omixórp o iereS
