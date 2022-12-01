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
        encoded_msg = Decimal(get_number(encoded_msg))
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


def get_number(number):
    dec, zero = str(number).split(".")
    dec = int(dec, 2)
    zero = int(zero, 2)
    result = f"0.{'0'*zero}{dec}"
    return result
