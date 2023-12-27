import sys
number = []
letter = []
print("usage python3 xorxor.py (# or string) number|language")
if (sys.argv[2] == "number"):
    for i in range(int(sys.argv[1])):
        number.append(i)
    class x:
        x = lambda x: x^x^x
    print(list(map(x.x, number)))
if (sys.argv[2] == "language"):
    for character in str(sys.argv[1]):
        letter.append(ord(character))
    class l:
        l = lambda l: chr(l^l^l)
    print(list(map(l.l, letter)))


