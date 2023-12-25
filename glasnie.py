word = input()
a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

glasnie = a + e + i + o + u
print("Гласные буквы:", glasnie)
print("Согласные буквы:", len(word) - glasnie)

if a == 0:
    print("a - false")
else:
    print("a =", a)
if e == 0:
    print("e - false")
else:
    print("e =", e)
if i == 0:
    print("i - false")
else:
    print("i =", i)
if o == 0:
    print("o = false")
else:
    print("o =", o)
if u == 0:
    print("u - false")
else:
    print("u =", u)
