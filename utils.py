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
