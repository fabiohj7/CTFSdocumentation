def gen_data():
    file = open("test.txt")
    data = file.read()
    incoming = open("incoming.txt").read().split()
    return data, incoming


if __name__ == "__main__":
    a, b = gen_data()
    print(a)
    print(b)
