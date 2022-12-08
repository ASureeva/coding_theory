class BurrowsWheeler:
    def __init__(self, data, length):
        self.data = data
        self.line = -1
        self.length = length
        self.result = ""
        self.word = ""

    def ordering(self):
        self.line = int(f"0b{self.line}", 2)
        g = [list(self.word) for _ in range(self.length)]
        c = [[] for _ in range(self.length)]
        if self.length > 1:
            for i in range(1, self.length):
                c[i] = sorted(g[i-1])
                for j in range(self.length):
                    g[i][j] += c[i][j]
            result_dict = sorted(g[-1])
            self.result = result_dict[self.line]
        else:
            self.result = self.word

    def reordering(self):
        order_data = list(range(self.length))
        order_data[0] = self.data
        for i in range(1, self.length):
            order_data[i] = order_data[i - 1][-1] + order_data[i - 1][0:-1]
        order_data = sorted(order_data)
        for i in range(self.length):
            self.word += order_data[i][-1]
            if order_data[i] == self.data:
                self.line = bin(i).replace("0b", "")


if __name__ == '__main__':
    data = "string"
    length = len(data)
    by_ = BurrowsWheeler(data, length)
    by_.reordering()
    by_.ordering()
    print(by_.result)
