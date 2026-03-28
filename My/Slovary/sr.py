s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ch = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
sl = {key:value for key,value in zip(s,ch)}
sl[" "]=0

def koch(slovo):
    k = 0
    for x in slovo:
        k += sl[x]
    return k

print(koch("ABCD"))

igra = {"Петя":["ABC","KUY","TVS"],"Ваня":["HHH","LAC","HSH"]}
for x in igra.items():
    print(x)