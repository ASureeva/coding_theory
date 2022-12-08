from movetofront_coding import MoveToFront
from arithmetic_decoding import Arithmetic
from by import BurrowsWheeler


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


def main():
    FLAG = False
    Move = False
    FLAG2 = False
    Arith = False
    data = ""
    alphabet = read_alg("input_file_mv")

    while not FLAG:
        while not data:
            data = input(" Введите слово: ")
        for word in data:
            if word not in alphabet[0]:
                print("\033[31m {}\033[0m".format("Error:WordNotInAlphabet"))
                FLAG = False
                data = ""
                break
            else:
                FLAG = True

    try:
        by_ = BurrowsWheeler(data=data, length=len(data))
        by_.reordering()
        data = by_.word

        code = MoveToFront(data=data, alphabet=alphabet[0])
        code.create_code()
        Move = True
    except:
        print("\033[31m {}\033[0m".format("Произошла неизвестная ошибка"))

    if Move:
        print(" Ваше код: \033[47m{}\033[0m".format(code.result))
        print(" Ваша строка: \033[47m{}\033[0m".format(by_.line))
    print("-"*40)

    alphabet = read_alg("input_file_alg")
    alphabet = create_frequency_table(alp=alphabet)

    data2 = ""
    length = -1
    while not FLAG2:
        # print(" Введите код:")
        while not data2:
            data2 = input(" Введите код: ")
        for word in data2:
            if word not in ["0", "1"]:
                print("\033[31m {}\033[0m".format("Error:WordNotInAlphabet"))
                FLAG2 = False
                data2 = ""
                break
            else:
                FLAG2 = True
        while length == -1:
            length = input(" Введите длину слова: ")
            try:
                length = int(length)
                if length < 0:
                    length = -1
                    print("\033[31m {}\033[0m".format("Error:NotNaturalNumber"))
            except:
                length = -1
                print("\033[31m {}\033[0m".format("Error:NotInt"))

    try:
        decode = Arithmetic(frequency_table=alphabet)
        decoder, decoded_msg = decode.decode(encoded_msg=data2,
                                             length=int(length),
                                             probability_table=decode.probability_table)
    except:
        print("\033[31m {}\033[0m".format("Произошла неизвестная ошибка"))
        decoded_msg = False

    if decoded_msg:
        print(" Ваше слово: \033[47m{}\033[0m".format(decoded_msg))


if __name__ == '__main__':
    main()
