import numpy as np
import matplotlib.pyplot as plt

# Yamuk üyelik fonksiyonu
def yamuk_uyelik_hesapla(a, b, c, d, u):
    if a <= u <= b:
        return (u - a) / (b - a)
    elif b < u <= c:
        return 1
    elif c < u <= d:
        return (d - u) / (d - c)
    else:
        return 0

# Evrensel küme
evrensel_kume = np.arange(20, 81, 1)

# Low ve Medium bulanık kümeleri hesapla
low = np.array([yamuk_uyelik_hesapla(20, 25, 35, 40, x) for x in evrensel_kume])
medium = np.array([yamuk_uyelik_hesapla(30, 42, 55, 80, x) for x in evrensel_kume])

# Birleşim hesaplama
union_min = np.minimum(low, medium)
union_max = np.maximum(low, medium)

# Kesişim hesaplama
intersection_min = np.minimum(low, medium)
intersection_max = np.maximum(low, medium)

# Görselleştirme
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(evrensel_kume, low, label='Low')
plt.plot(evrensel_kume, medium, label='Medium')
plt.title('Bulanık Kümeler')
plt.ylim(0, 1.05)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(evrensel_kume, union_min, label='T-Norm (Minimum)')
plt.plot(evrensel_kume, union_max, label='T-Norm (Maximum)')
plt.title('Birleşim (T-Norm)')
plt.ylim(0, 1.05)
plt.legend(loc='upper right')

plt.subplot(2, 2, 3)
plt.plot(evrensel_kume, intersection_min, label='S-Norm (Minimum)')
plt.subplot(2, 2, 4)
plt.plot(evrensel_kume, intersection_max, label='S-Norm (Maximum)')
plt.title('Kesişim (S-Norm)')
plt.ylim(0, 1.05)
plt.legend(loc='upper right')

plt.show()
