flower1 = int(input('How many petals in flower1: '))
flower2 = int(input('How many petals in flower2: '))

def lovefunc(flower1,flower2):
    if flower1 and flower2 % 2 == 0:
        return False 
    else:
        return True

lovefunc(flower1,flower2)

print(lovefunc(flower1,flower2))