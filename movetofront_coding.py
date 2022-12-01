import math


class MoveToFront:
    def __init__(self, data, alphabet):
        self.data = data
        self.alphabet = sorted(alphabet)
        self.length = len(data)
        self.word = ""
        self.line = -1
        self.result = ""

    def reordering(self):
        order_data = list(range(self.length))
        order_data[0] = self.data
        for i in range(1, self.length):
            order_data[i] = order_data[i - 1][-1] + order_data[i - 1][0:-1]
        order_data = sorted(order_data)
        for i in range(self.length):
            self.word += order_data[i][-1]
            if order_data[i] == self.data:
                 self.line = i

    def create_code(self):
        count = round(math.sqrt(len(self.alphabet))) + 1
        self.reordering()
        for i in range(self.length):
            if self.word[i] in self.alphabet:
                now = self.alphabet.index(self.word[i])
                self.result += bin(now)[2:].zfill(count)
                self.alphabet.remove(self.word[i])
                self.alphabet.insert(0, self.word[i])
