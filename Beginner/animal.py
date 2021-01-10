# Reading the Data...
species = input()
classes = input()
inter_species = input()

# Checking The Conditions...
if (species.lower() == 'vertebrado'):
    if (classes.lower() == 'ave'):
        if (inter_species.lower() == 'carnivoro'):
            print('aguia')
        elif (inter_species.lower() == 'onivoro'):
            print('pomba')
    elif (classes.lower() == 'mamifero'):
        if (inter_species.lower() == 'onivoro'):
            print('homem')
        elif (inter_species.lower() == 'herbivoro'):
            print('vaca')

elif (species.lower() == 'invertebrado'):
    if (classes.lower() == 'inseto'):
        if (inter_species.lower() == 'hematofago'):
            print('pulga')
        elif (inter_species.lower() == 'herbivoro'):
            print('lagarta')
    elif (classes.lower() == 'anelideo'):
        if (inter_species.lower() == 'hematofago'):
            print('sanguessuga')
        elif (inter_species.lower() == 'onivoro'):
            print('minhoca')
