from decimal import Decimal


class Arithmetic:
    def __init__(self, frequency_table):
        self.probability_table = self.get_probability_table(frequency_table)

    def get_probability_table(self, frequency_table):
        total_f = sum(list(frequency_table.values()))

        probability_table = {}
        for key, value in frequency_table.items():
            probability_table[key] = value/total_f
        return probability_table

    def interval(self, probability_table, left, right):
        probs = {}
        segment = right - left
        for element in range(len(probability_table.items())):
            term = list(probability_table.keys())[element]
            term_prob = Decimal(probability_table[term])
            left_prob = term_prob * segment + left
            probs[term] = [left, left_prob]
            left = left_prob
        return probs

    def decode(self, encoded_msg, length, probability_table):
        global msg_term
        decoder = []
        decoded_msg = ""
        encoded_msg = Decimal(text_from_bits(encoded_msg))
        left = Decimal(0.0)
        right = Decimal(1.0)

        for _ in range(length):
            probs = self.interval(probability_table, left, right)
            for term, value in probs.items():
                if encoded_msg >= value[0] and encoded_msg <= value[1]:
                    break

            decoded_msg = decoded_msg + term
            left = probs[term][0]
            right = probs[term][1]

            decoder.append(probs)

        probs = self.interval(probability_table, left, right)
        decoder.append(probs)

        return decoder, decoded_msg


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


if __name__ == '__main__':
    alphabet = ['a', 'b']
    probability = [0.75, 0.25]
    N = 14
    sequence = "aabaaabaacdaae"
    frequency_table = {"a": 0.2,
                       "b": 0.1,
                       "c": 0.3,
                       "d": 0.2,
                       "e": 0.2}

    AE = Arithmetic(frequency_table)
