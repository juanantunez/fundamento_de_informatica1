#desafio 8 
ceb=30
def calc(per):
    ml=per*ceb
    if ml<=1000:
      return ml
    else:
      return "vas a necesitar mas de un termo"  