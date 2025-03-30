import re

def contar_palavras(texto):
    padrao_palavra = r'\b\w+\b'
    palavras = re.findall(padrao_palavra, texto)
    return len(palavras)

texto = "Olá mundo! Essa é uma frase de teste"
numero_palavras = contar_palavras(texto)

print(f"No texto contem {numero_palavras} palavras")