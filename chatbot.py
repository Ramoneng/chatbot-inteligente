def responder_pergunta(pergunta):
    if "quantidade de erros" in pergunta:
        return "A quantidade total de erros é X."
    elif "rasgado" in pergunta and "12" in pergunta and "15 de maio de 2023" in pergunta:
        return "O número de erros do tipo 'rasgado' entre 12 e 15 de maio de 2023 é Y."
    elif "22 de maio de 2023" in pergunta:
        return "No dia 22 de maio de 2023, tivemos um erro do tipo Z."
    else:
        return "Desculpe, não entendi a pergunta."

# Exemplo de pergunta e resposta
pergunta_exemplo = "Quantos erros tivemos no total?"
resposta_exemplo = responder_pergunta(pergunta_exemplo)
print(resposta_exemplo)
