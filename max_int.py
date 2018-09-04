# notandi setur inn tölur aftur og aftur þar til negatív tala er slegin onn
# lykkja tekur á móti inputinu og finnur stærstu töluna sem notandi setur inn
num_int = int(input("input a number "))

num_int = 0
max_int = 0


while num_int >= 0:
    num_int = int(input("input a number"))
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)