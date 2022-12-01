from movetofront_coding import MoveToFront
from arithmetic_decoding import Arithmetic


def read_alg(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        p = []
        alphabet = lines[0].split()
        try:
            line = lines[1].split()
            for element in line:
                h = element.split("/")
                p.append(int(h[0])/int(h[1]))
                # p[i] = int(p[i].replace(",", "."))
        except Exception:
            p = ""
        return [alphabet, p]


def create_frequency_table(alp):
    frequency_dict = {}
    for i in range(len(alp[0])):
        frequency_dict[alp[0][i]] = alp[1][i]
    return frequency_dict


def validate(data, length, alphabet):
    for i in range(length):
        if data[i] not in alphabet:
            quit("В слове есть лишний символ")


def coder():
    alphabet = read_alg("input_file_mv")
    data = input("Введите слово: ")
    code = MoveToFront(data=data, alphabet=alphabet[0])
    code.create_code()
    print("Ваш код:", code.result)
    print("-"*40)

    alphabet = read_alg("input_file_alg")
    alphabet = create_frequency_table(alp=alphabet)
    data = input("Введите код: ")
    length = input("Введите длину слова:")

    decode = Arithmetic(frequency_table=alphabet)
    decoder, decoded_msg = decode.decode(encoded_msg=data,
                                         length=int(length),
                                         probability_table=decode.probability_table)
    print(f"Ваше слово: {decoded_msg}")


if __name__ == '__main__':
    coder()
