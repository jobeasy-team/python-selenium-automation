address = 4
n=3
min=1
if address % 2 == 0:
    opposite = 1 + ((n*2) - address)
else:
    opposite = n*2 - (address-min)

print(opposite)