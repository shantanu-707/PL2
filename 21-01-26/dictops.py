d1 = {'name':'Alexios','Nationality':'Spartan','Species':'Demigod','Weapon':'Spear of Leonidas','Occupation':'Mercenary'}
d2 = {'name':'Kassandra','Nationality':'Spartan','Species':'Demigod','Weapon':'Ancient Sword','Occupation':'Cult of Kosmos Operative'}

print(d1)
print(d2)

print(d1['Weapon'])
print(d2['Occupation'])

d2['Nationality'] = 'Ex-Spartan'

d1.pop('Occupation')
print(d1)
print(d2)

d1['Father']  = 'Pythagoras'
print(d1)

d1.update(d2)
print(d1)
