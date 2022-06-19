print("program pembagian")

while True:
    try:
        angka1 = int(input("masukan bilangan angka1: "))
        angka2 = int(input("masukan bilangan angka2: "))
        total = angka1/angka2
        break
    except ZeroDivisionError:
        print("gabesa dibagi nol\n")

print("berhasil, hasil pembagian adalah:" ,total)