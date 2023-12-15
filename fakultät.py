zahl = int(input("Gib eine Zahl ein: "))

def berechne_fakultaet(n):
    if n == 0 | n == 1:
        return 1
    else:
        res = n * berechne_fakultaet(n - 1)
        return res
    
result = berechne_fakultaet(zahl)
print(f"Die Fakultät der zahl {zahl} lautet: {result}")