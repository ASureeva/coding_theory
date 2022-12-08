import copy


class MoveToFront:
    def __init__(self, data, alphabet):
        self.string = data
        self.data = []
        self.alphabet = alphabet
        self.alphabet_ = copy.deepcopy(alphabet)
        self.length = len(data)
        self.word = data
        self.dec = ""
        self.line = -1
        self.result = ""

    def create_code(self):
        count = 0
        while 2 ** count < len(self.alphabet):
            count += 1
        for i in range(self.length):
            if self.word[i] in self.alphabet:
                now = self.alphabet.index(self.word[i])
                self.result += bin(now)[2:].zfill(count)
                self.alphabet.remove(self.word[i])
                self.alphabet.insert(0, self.word[i])
            # else:
                # print("Error:WordNotInAlphabet")
                # break


if __name__ == '__main__':
    data = "sbc"
    alphabet = ["s", "b", "c", "i", "n", "g"]
    mtf_ = MoveToFront(data, alphabet)
    mtf_.create_code()
    print(mtf_.result)
