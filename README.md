# Contador de Palavras com Regex

Este exercício utiliza expressões regulares em Python para contar o número de palavras em um texto.

## Funcionalidade

- Define a função `contar_palavras` que recebe um texto como entrada.
- Usa regex para identificar todas as palavras no texto.
- Retorna a quantidade total de palavras encontradas.

## Exemplo de uso

```python
texto = "Olá mundo! Essa é uma frase de teste"
numero_palavras = contar_palavras(texto)

print(f"No texto contem {numero_palavras} palavras")
```
## Saída esperada

```
No texto contem 8 palavras
```

## Regex utilizada

```
r'\b\w+\b'
```
