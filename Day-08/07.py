b = "neha is good gir"
h = b.split()
print(h)

ong = h[0]
for i in range(len(h)):
    if len(h[i]) > len(ong):
        ong = h[i]

print(ong)
