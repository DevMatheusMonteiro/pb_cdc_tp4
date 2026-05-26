class Heap:
    def __init__(self, modo='min'):
        self.data = []
        self.__cmp = (lambda a, b: a < b) if modo == 'min' else (lambda a, b: a > b)

    def insert(self, valor):
        self.data.append(valor)
        self.__sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        topo = self.data[0]
        ultimo = self.data.pop()
        if self.data:
            self.data[0] = ultimo
            self.__sift_down(0)
        return topo

    def peek(self):
        return self.data[0] if self.data else None

    def __sift_up(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self.__cmp(self.data[i], self.data[pai]):
                self.data[i], self.data[pai] = self.data[pai], self.data[i]
                i = pai
            else:
                break

    def __sift_down(self, i):
        n = len(self.data)
        while True:
            esq = 2 * i + 1
            dir = 2 * i + 2
            alvo = i
            if esq < n and self.__cmp(self.data[esq], self.data[alvo]):
                alvo = esq
            if dir < n and self.__cmp(self.data[dir], self.data[alvo]):
                alvo = dir
            if alvo == i:
                break
            self.data[i], self.data[alvo] = self.data[alvo], self.data[i]
            i = alvo

    @classmethod
    def from_list(cls, arr, modo='min'):
        heap = cls(modo)
        heap.data = arr[:]
        for i in range(len(heap.data) // 2 - 1, -1, -1):
            heap.__sift_down(i)
        return heap

    def __len__(self):
        return len(self.data)

class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_chave = False
        self.qtd = 0

class Trie:
    def __init__(self, separador=None):
        self.raiz = TrieNode()
        self.__sep = separador

    def __tokenizar(self, s):
        return s.split(self.__sep) if self.__sep else s

    def insert(self, chave):
        atual = self.raiz
        for parte in self.__tokenizar(chave):
            if parte not in atual.filhos:
                atual.filhos[parte] = TrieNode()
            atual = atual.filhos[parte]
            atual.qtd += 1
        atual.fim_chave = True

    def busca(self, chave):
        no = self.__walk(chave)
        return no is not None and no.fim_chave

    def verificar_prefixo(self, prefixo):
        return self.__walk(prefixo) is not None

    def contar_prefixo(self, prefixo):
        no = self.__walk(prefixo)
        return no.qtd if no else 0

    def sugerir(self, prefixo):
        no = self.__walk(prefixo)
        if no is None:
            return []
        resultado = []
        sep = self.__sep or ''

        def dfs(no, caminho):
            if no.fim_chave:
                resultado.append(sep.join(caminho))
            for parte, filho in no.filhos.items():
                dfs(filho, caminho + [parte])

        dfs(no, list(self.__tokenizar(prefixo)))
        return resultado

    def maior_prefixo_k(self, k):
        sep = self.__sep or ''
        melhor = [None, 0]

        def dfs(no, prof, caminho):
            if prof == k:
                if no.qtd > melhor[1]:
                    melhor[0] = sep.join(caminho)
                    melhor[1] = no.qtd
                return
            for parte, filho in no.filhos.items():
                dfs(filho, prof + 1, caminho + [parte])

        dfs(self.raiz, 0, [])
        return melhor[0], melhor[1]

    def __walk(self, s):
        atual = self.raiz
        for parte in self.__tokenizar(s):
            if parte not in atual.filhos:
                return None
            atual = atual.filhos[parte]
        return atual
