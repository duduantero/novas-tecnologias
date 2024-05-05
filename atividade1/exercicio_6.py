import math

a = 1  
b = 5  
c = 6  

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes da equação são x' = {x1} e x'' = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui uma única raiz real x = {x}")
else:
    print("A equação não possui raízes reais.")
