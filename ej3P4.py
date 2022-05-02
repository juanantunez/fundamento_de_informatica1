def ult(arch, n):
  with open(arch, "r") as f:
    print(f.readlines()[-n:]) #[-2:] anteultima posicion hasta el final  

ult("acasepo.txt", 2)