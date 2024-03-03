import nltk
from nltk.tokenize import word_tokenize
import re 

# Baixar recursos necessários do NLTK (só necessário na primeira execução)
nltk.download('punkt')



# Dados da tabela
tabela = [
    {"Item": 1, "Data": "12-mai.-2023", "Componente": "AAAA", "Tipo de erro": "rasgado"},
    {"Item": 2, "Data": "13-mai.-2023", "Componente": "BBBB", "Tipo de erro": "furado"},
    {"Item": 3, "Data": "14-mai.-2023", "Componente": "CCCC", "Tipo de erro": "molhado"},
    {"Item": 4, "Data": "15-mai.-2023", "Componente": "AAAA", "Tipo de erro": "cortado"},
    {"Item": 5, "Data": "16-mai.-2023", "Componente": "BBBB", "Tipo de erro": "rasgado"},
    {"Item": 6, "Data": "17-mai.-2023", "Componente": "CCCC", "Tipo de erro": "furado"},
    {"Item": 7, "Data": "18-mai.-2023", "Componente": "AAAA", "Tipo de erro": "molhado"},
    {"Item": 8, "Data": "19-mai.-2023", "Componente": "BBBB", "Tipo de erro": "cortado"},
    {"Item": 9, "Data": "20-mai.-2023", "Componente": "CCCC", "Tipo de erro": "rasgado"},
    {"Item": 10, "Data": "21-mai.-2023", "Componente": "AAAA", "Tipo de erro": "furado"},
    {"Item": 11, "Data": "22-mai.-2023", "Componente": "BBBB", "Tipo de erro": "molhado"},
    {"Item": 12, "Data": "23-mai.-2023", "Componente": "CCCC", "Tipo de erro": "cortado"},
    {"Item": 13, "Data": "24-mai.-2023", "Componente": "AAAA", "Tipo de erro": "rasgado"},
    {"Item": 14, "Data": "25-mai.-2023", "Componente": "BBBB", "Tipo de erro": "furado"},
    {"Item": 15, "Data": "26-mai.-2023", "Componente": "CCCC", "Tipo de erro": "molhado"}
]

# Função para processar a pergunta do usuário
def processar_pergunta(pergunta):
    # Padronizar a pergunta para facilitar a identificação das palavras-chave
    pergunta = pergunta.lower()  # Converter para minúsculas
    pergunta = re.sub(r'[^\w\s]', '', pergunta)  # Remover caracteres especiais

    # Identificar palavras-chave usando padrões
    palavras_chave = {
        "quantidade de erros": ["quantidade", "erros"],
        "erros rasgados entre 12 e 15 de maio de 2023": ["rasgado", "12", "15", "maio", "2023"],
        "tipo de erro em 22 de maio de 2023": ["tipo", "erro", "22", "maio", "2023"],
        "posso obter ajuda": ["ajuda"]
    }

    # Verificar se algum padrão de palavras-chave corresponde à pergunta
    for padrao, palavras in palavras_chave.items():
        if all(palavra in pergunta for palavra in palavras):
            return padrao

    # Se nenhum padrão corresponder, retornar uma mensagem de ajuda
    return "posso obter ajuda"


# Função para responder perguntas com base nos dados da tabela
def responder_pergunta(pergunta):
    # Processar a pergunta do usuário
    padrao = processar_pergunta(pergunta)

    # Lógica para responder perguntas com base no padrão identificado
    if padrao == "quantidade de erros":
        quantidade_total = len(tabela)
        return f"A quantidade total de erros é {quantidade_total}."
    elif padrao == "erros rasgados entre 12 e 15 de maio de 2023":
        erros_rasgados = sum(1 for linha in tabela if linha["Tipo de erro"] == "rasgado" and "12-mai.-2023" <= linha["Data"] <= "15-mai.-2023")
        return f"O número de erros do tipo 'rasgado' entre 12 e 15 de maio de 2023 é {erros_rasgados}."
    elif padrao == "tipo de erro em 22 de maio de 2023":
        erro_22_maio = next((linha["Tipo de erro"] for linha in tabela if linha["Data"] == "22-mai.-2023"), None)
        return f"No dia 22 de maio de 2023, tivemos um erro do tipo '{erro_22_maio}'."
    elif padrao == "posso obter ajuda":
        return fornecer_sugestoes()  # Chamada da função de fornecer sugestões
    else:
        return "Desculpe, não entendi a pergunta."


# Função para fornecer sugestões de respostas
def fornecer_sugestoes():
    sugestoes = [
        "Por favor, reformule sua pergunta.",
        "Você pode perguntar sobre a quantidade total de erros ou tipos específicos de erros.",
        "Experimente perguntar 'Quantidade de erros no total?' ou 'Que tipo de erro tivemos em 22 de maio de 2023?'",
        "Se precisar de ajuda, digite 'Ajuda' para ver uma lista de comandos disponíveis."
    ]
    return "Aqui estão algumas sugestões de respostas:\n" + "\n".join(sugestoes)


# Definição das perguntas de exemplo
pergunta1 = "Quantidade de erros no total?"
pergunta2 = "Quantos erros rasgados tiveram entre 12 e 15 de maio de 2023?"
pergunta3 = "Que tipo de erro tivemos em 22 de maio de 2023?"
pergunta4 = "Posso obter ajuda?"
pergunta5 = "Como posso reformular minha pergunta?"
pergunta6 = "O que eu posso perguntar?"

# Testar com as perguntas de exemplo
resposta1 = responder_pergunta(pergunta1)
resposta2 = responder_pergunta(pergunta2)
resposta3 = responder_pergunta(pergunta3)
resposta4 = responder_pergunta(pergunta4)
resposta5 = responder_pergunta(pergunta5)
resposta6 = responder_pergunta(pergunta6)

# Imprimir as respostas
print("Pergunta 1:", pergunta1)
print("Resposta 1:", resposta1)
print("Pergunta 2:", pergunta2)
print("Resposta 2:", resposta2)
print("Pergunta 3:", pergunta3)
print("Resposta 3:", resposta3)
print("Pergunta 4:", pergunta4)
print("Resposta 4:", resposta4)
print("Pergunta 5:", pergunta5)
print("Resposta 5:", resposta5)
print("Pergunta 6:", pergunta6)
print("Resposta 6:", resposta6)

