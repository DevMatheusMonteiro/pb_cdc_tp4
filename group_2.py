from utils import Trie

# Exercício 6
def exercicio_6():
    print("=== Exercício 6 ===")
    t = Trie()
    for p in ["casa", "carro", "cachorro", "cama", "caminho"]:
        t.insert(p)

    print("busca('casa'):", t.busca("casa"))
    print("busca('casas'):", t.busca("casas"))
    print("busca('cama'):", t.busca("cama"))
    print("tem_prefixo('cam'):", t.verificar_prefixo("cam"))
    print("tem_prefixo('xyz'):", t.verificar_prefixo("xyz"))

# Exercício 7
def exercicio_7():
    print("=== Exercício 7 ===")
    t = Trie()
    for p in ["python", "programa", "programação", "projeto",
              "prova", "pratica", "produto"]:
        t.insert(p)

    for pref in ["pro", "pr", "pra", "py", "xyz"]:
        print(f"sugestões para '{pref}': {t.sugerir(pref)}")

# Exercício 8
def exercicio_8():
    print("=== Exercício 8 ===")
    t = Trie()
    for p in ["casa", "carro", "cachorro", "cama", "caminho", "cão", "cão"]:
        t.insert(p)

    for pref in ["ca", "cam", "car", "cão", "c"]:
        print(f"palavras com prefixo '{pref}': {t.contar_prefixo(pref)}")

# Exercício 9
def prefixo_ip_mais_frequente(ips, k):
    if k < 1 or k > 4:
        raise ValueError("k deve estar entre 1 e 4")

    contagem = {}
    for ip in ips:
        prefixo = ".".join(ip.split(".")[:k])
        contagem[prefixo] = contagem.get(prefixo, 0) + 1

    melhor = max(contagem, key=contagem.get)
    return melhor, contagem[melhor]

def exercicio_9():
    print("=== Exercício 9 ===")
    ips = [
        "192.168.0.1", "192.168.0.2", "192.168.1.10",
        "10.0.0.1", "10.0.0.2", "10.0.0.3", "192.168.0.5",
    ]
    for k in [1, 2, 3]:
        pref, qtd = prefixo_ip_mais_frequente(ips, k)
        print(f"  k={k}: prefixo '{pref}' aparece {qtd} vezes")

# Exercício 10
def exercicio_10():
    print("=== Exercício 10 ===")
    ips = [
        "192.168.0.1", "192.168.0.2", "192.168.1.10",
        "10.0.0.1", "10.0.0.2", "10.0.0.3", "192.168.0.5",
    ]
    t = Trie(separador='.')
    for ip in ips:
        t.insert(ip)

    for k in [1, 2, 3]:
        pref, qtd = t.maior_prefixo_k(k)
        print(f"  k={k}: maior prefixo '{pref}' com {qtd} IPs")

exercicio_6()
print()
exercicio_7()
print()
exercicio_8()
print()
exercicio_9()
print()
exercicio_10()
