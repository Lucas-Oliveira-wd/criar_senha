import random
import string


def gerar_senha(tamanho):
    if tamanho % 4 != 0:
        raise ValueError(
            "O tamanho da senha deve ser múltiplo de 4 para garantir proporção igual entre os tipos de caracteres.")

    # Número de caracteres por grupo
    n = tamanho // 4

    maiusculas = random.choices(string.ascii_uppercase, k=n)
    minusculas = random.choices(string.ascii_lowercase, k=n)
    numeros = random.choices(string.digits, k=n)
    especiais = random.choices(string.punctuation, k=n)

    senha_lista = maiusculas + minusculas + numeros + especiais
    random.shuffle(senha_lista)

    senha = ''.join(senha_lista)
    return senha


# Exemplo de uso
tamanho_desejado = 8  # deve ser múltiplo de 4
senha_gerada = gerar_senha(tamanho_desejado)
print("Senha gerada:", senha_gerada)
