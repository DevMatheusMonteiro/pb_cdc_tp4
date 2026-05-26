from utils import Heap

# Exercício 1
def exercicio_1():
    print("=== Exercício 1 ===")
    heap = Heap(modo='min')
    for v in [7, 3, 9, 1, 4, 8, 2]:
        heap.insert(v)
    print("Heap interna:", heap.data)
    print("Menor (peek):", heap.peek())
    print("Removendo em ordem:")
    while len(heap) > 0:
        print(heap.pop(), end=" ")
    print()

# Exercício 2
def build_heap(arr):
    return Heap.from_list(arr, modo='min').data

def exercicio_2():
    print("=== Exercício 2 ===")
    vetor = [10, 4, 15, 2, 8, 1, 7, 3]
    print("Entrada:", vetor)
    heap = build_heap(vetor)
    print("Heap valida:", heap)

# Exercício 3
def exercicio_3():
    print("=== Exercício 3 ===")
    heap = Heap(modo='max')
    for v in [5, 12, 3, 18, 7, 1, 20, 9]:
        heap.insert(v)
    print("Heap interna:", heap.data)
    print("Removendo em ordem decrescente:")
    while len(heap) > 0:
        print(heap.pop(), end=" ")
    print()

# Exercício 4
def exercicio_4():
    print("=== Exercício 4 ===")
    fila = Heap(modo='min')
    fila.insert((2, 10, "A"))
    fila.insert((1, 15, "B"))
    fila.insert((1, 12, "C"))
    fila.insert((3,  5, "D"))
    fila.insert((2,  8, "E"))

    print("Ordem de atendimento:")
    while len(fila) > 0:
        prio, tc, id_ = fila.pop()
        print(f"id={id_} prioridade={prio} chegada={tc}")

# Exercício 5
def simular_pista(avioes):
    avioes = sorted(avioes, key=lambda a: a[1])

    heap = Heap(modo='min')
    ordem = []
    sem_combustivel = 0
    tempo_atual = 0
    idx = 0
    n = len(avioes)

    while idx < n or len(heap) > 0:
        while idx < n and avioes[idx][1] <= tempo_atual:
            id_, ts, comb, tp = avioes[idx]
            heap.insert((comb, ts, id_, tp))
            idx += 1

        if len(heap) == 0:
            tempo_atual = avioes[idx][1]
            continue

        comb, ts, id_, tp = heap.pop()

        espera = tempo_atual - ts
        if espera > comb:
            sem_combustivel += 1
            ordem.append((id_, "CAIU"))
        else:
            ordem.append((id_, "POUSOU"))
            tempo_atual += tp

    return ordem, sem_combustivel

def exercicio_5():
    print("=== Exercício 5 ===")
    avioes = [
        ("AV1", 0, 10, 3),
        ("AV2", 1, 5, 2),
        ("AV3", 2, 4, 2),
        ("AV4", 3, 20, 3),
        ("AV5", 4, 1, 2),
    ]
    ordem, caidos = simular_pista(avioes)
    for id_, status in ordem:
        print(f"{id_}: {status}")
    print(f"Total sem combustível: {caidos}")

exercicio_1()
print()
exercicio_2()
print()
exercicio_3()
print()
exercicio_4()
print()
exercicio_5()
