import numpy as np
import matplotlib.pyplot as plt
import math

def uyelik_hesapla(a, b, c, u):
    if u < a:
        return 0
    elif a <= u <= b:
        return 2 * ((u - a) / (c - a))**2
    elif b < u <= c:
        return 1 - 2 * ((u - c) / (c - a))**2
    else:
        return 1

def kuvvet(bulanik_kume, kuvvet_degeri):
    return [uyelik_degeri ** kuvvet_degeri for uyelik_degeri in bulanik_kume]

def derisme(bulanik_kume, derece):
    return [uyelik_degeri * derece for uyelik_degeri in bulanik_kume]

def genisleme(bulanik_kume, derece):
    return [uyelik_degeri ** derece for uyelik_degeri in bulanik_kume]

def yogunlasma(bulanik_kume, derece):
    return [uyelik_degeri ** (1/derece) for uyelik_degeri in bulanik_kume]

x = np.arange(1, 100, 1)
x_sol = []
x_sag = []
b_genislik = 40
c_orta_nokta = 50

z_sag = [uyelik_hesapla(c_orta_nokta - b_genislik, c_orta_nokta - b_genislik / 2, c_orta_nokta, u) if u <= c_orta_nokta else math.nan  for u in x]
z_sol = [1 - uyelik_hesapla(c_orta_nokta, c_orta_nokta + b_genislik / 2, c_orta_nokta + b_genislik, u)  if u >= c_orta_nokta else math.nan  for u in x]

plt.figure(figsize=(10, 6)) 
plt.plot(x, z_sag, label='Sağ Omuz')
plt.plot(x, z_sol, label='Sol Omuz')

kuvvet_degeri = 2
z_sag_kuvvet = kuvvet(z_sag, kuvvet_degeri)
z_sol_kuvvet = kuvvet(z_sol, kuvvet_degeri)

plt.plot(x, z_sag_kuvvet, label=f'Sağ Omuz Kuvvet {kuvvet_degeri}')
plt.plot(x, z_sol_kuvvet, label=f'Sol Omuz Kuvvet {kuvvet_degeri}')

derece = 2
z_sag_derisme = derisme(z_sag, derece)
z_sol_derisme = derisme(z_sol, derece)

plt.plot(x, z_sag_derisme, label=f'Sağ Omuz Derişme {derece}')
plt.plot(x, z_sol_derisme, label=f'Sol Omuz Derişme {derece}')

derece = 2
z_sag_genisleme = genisleme(z_sag, derece)
z_sol_genisleme = genisleme(z_sol, derece)

plt.plot(x, z_sag_genisleme, label=f'Sağ Omuz Genişleme {derece}')
plt.plot(x, z_sol_genisleme, label=f'Sol Omuz Genişleme {derece}')

derece = 2
z_sag_yogunlasma = yogunlasma(z_sag, derece)
z_sol_yogunlasma = yogunlasma(z_sol, derece)

plt.plot(x, z_sag_yogunlasma, label=f'Sağ Omuz Yoğunlaşma {derece}')
plt.plot(x, z_sol_yogunlasma, label=f'Sol Omuz Yoğunlaşma {derece}')


plt.legend(loc = 'upper left',)
plt.show()
