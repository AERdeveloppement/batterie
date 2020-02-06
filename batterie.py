import os

#nombre d'elements
elt=input("Saissisez le nombre d'éléments:")
elt=float(elt)

#temperature
temperature=input("Quelle est la temperature dans votre pièce?:")
temperature=float(temperature)

#intensite_charge
intensite_charge=input("Saissisez le nombre d'ampère consommé en une heure:")
intensite_charge=float(intensite_charge)
intensite_charge=intensite_charge/5

#ecart_temperature
ecart_temperature=25-temperature

#ecart_volt
ecart_volt=ecart_temperature*0.005

#tension nominale
tension_nominale=2.1*elt
tension_nominale=format(tension_nominale, '0.1f')

#tension de recharge
tension_recharge=(2.3+ecart_volt)*elt
tension_recharge=format(tension_recharge, '0.1f')

#tension de floating
tension_floating=(2.28+ecart_volt)*elt
tension_floating=format(tension_floating, '0.1f')

print("La tension nominale est de:")
print(tension_nominale)
print("Volt")

print("La tension de recharge est de:")
print(tension_recharge)
print("Volt")

print("La tension de floating est de:")
print(tension_floating)
print("Volt")

print("L'intensité de charge est de:")
print(intensite_charge)
print("Ampère")

os.system("pause")