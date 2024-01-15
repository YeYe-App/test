# -*- coding: utf-8 -*-

import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

def plot_membership(ax, x, membership, color, label):
    ax.plot(x, membership, color, linewidth=2, label=label)

def plot_vertical_lines(ax, x, y, color, linestyle='--'):
    ax.plot([x, x], [0, y], color, linewidth=1, linestyle=linestyle)

def calculate_membership(var, set_low, set_mid, set_high, input_value):
    low = fuzz.interp_membership(var, set_low, input_value)
    mid = fuzz.interp_membership(var, set_mid, input_value)
    high = fuzz.interp_membership(var, set_high, input_value)
    return low, mid, high

var_model = np.arange(2002, 2013, 1)
var_km = np.arange(0, 100001, 1)
var_fiyat = np.arange(0, 40001, 1)

set_model_dusuk = mf.trimf(var_model, [2002, 2002, 2007])
set_model_orta = mf.trimf(var_model, [2002, 2007, 2012])
set_model_yuksek = mf.trimf(var_model, [2007, 2012, 2012])

set_km_dusuk = mf.trimf(var_km, [0, 0, 50000])
set_km_orta = mf.trimf(var_km, [0, 50000, 100000])
set_km_yuksek = mf.trimf(var_km, [50000, 100000, 100000])

set_fiyat_dusuk = mf.trimf(var_fiyat, [0, 0, 20000])
set_fiyat_orta = mf.trimf(var_fiyat, [0, 20000, 40000])
set_fiyat_yuksek = mf.trimf(var_fiyat, [20000, 40000, 40000])

fig, axs = plt.subplots(nrows=5, figsize=(15, 20))

plot_membership(axs[0], var_model, set_model_dusuk, 'r', 'Düşük')
plot_membership(axs[0], var_model, set_model_orta, 'g', 'Orta')
plot_membership(axs[0], var_model, set_model_yuksek, 'b', 'Yüksek')
axs[0].set_title("Model")
axs[0].legend()

plot_membership(axs[1], var_km, set_km_dusuk, 'r', 'Düşük')
plot_membership(axs[1], var_km, set_km_orta, 'g', 'Orta')
plot_membership(axs[1], var_km, set_km_yuksek, 'b', 'Yüksek')
axs[1].set_title("Kilometre")
axs[1].legend()

plot_membership(axs[2], var_fiyat, set_fiyat_dusuk, 'r', 'Düşük')
plot_membership(axs[2], var_fiyat, set_fiyat_orta, 'g', 'Orta')
plot_membership(axs[2], var_fiyat, set_fiyat_yuksek, 'b', 'Yüksek')
axs[2].set_title("Fiyat")
axs[2].legend()

input_model = 2011
input_km = 25000

model_fit_dusuk, model_fit_orta, model_fit_yuksek = calculate_membership(var_model, set_model_dusuk, set_model_orta, set_model_yuksek, input_model)
km_fit_dusuk, km_fit_orta, km_fit_yuksek = calculate_membership(var_km, set_km_dusuk, set_km_orta, set_km_yuksek, input_km)

plot_vertical_lines(axs[0], input_model, model_fit_dusuk, 'r')
plot_vertical_lines(axs[0], input_model, model_fit_orta, 'g')
plot_vertical_lines(axs[0], input_model, model_fit_yuksek, 'b')

plot_vertical_lines(axs[1], input_km, km_fit_dusuk, 'r')
plot_vertical_lines(axs[1], input_km, km_fit_orta, 'g')
plot_vertical_lines(axs[1], input_km, km_fit_yuksek, 'b')

rule1 = np.fmin(np.fmin(model_fit_dusuk, km_fit_yuksek), set_fiyat_dusuk)
rule2 = np.fmin(np.fmin(model_fit_orta, km_fit_orta), set_fiyat_orta)
rule3 = np.fmin(np.fmin(model_fit_yuksek, km_fit_dusuk), set_fiyat_yuksek)

axs[3].plot(var_fiyat, rule1, 'r', linestyle='--', linewidth=1, label='Rule-1')
axs[3].plot(var_fiyat, rule2, 'b', linestyle='-.', linewidth=2, label='Rule-2')
axs[3].plot(var_fiyat, rule3, 'g', linestyle=':', linewidth=2, label='Rule-3')
axs[3].set_title("Çıkış Kümeleri")
axs[3].legend()

out1 = np.fmax(rule1, rule2)
out_set_final = np.fmax(out1, rule3)
axs[4].fill_between(var_fiyat, out_set_final, 'b', linestyle=':', linewidth=2, label='out')
axs[4].set_title("Çıkış-Bulanık Küme Birleşimi")

defuzzified_centroid = fuzz.defuzz(var_fiyat, out_set_final, 'centroid')
defuzzified_bisector = fuzz.defuzz(var_fiyat, out_set_final, 'bisector')
defuzzified_mom = fuzz.defuzz(var_fiyat, out_set_final, 'mom')
defuzzified_lom = fuzz.defuzz(var_fiyat, out_set_final, 'lom')
defuzzified_som = fuzz.defuzz(var_fiyat, out_set_final, 'som')

print("Fiyat(centroid)=", defuzzified_centroid)
print("Fiyat(bisector)=", defuzzified_bisector)
print("Fiyat(mom)=", defuzzified_mom)
print("Fiyat(lom)=", defuzzified_lom)
print("Fiyat(som)=", defuzzified_som)

hangisi = defuzzified_centroid
result = fuzz.interp_membership(var_fiyat, out_set_final, hangisi)
axs[4].plot([0, hangisi], [result, result], 'r')
axs[4].plot([hangisi, hangisi], [0, result], 'r')

print("\nÇıkış Düşük Kümesine Üyeliği=", fuzz.interp_membership(var_fiyat, set_fiyat_dusuk, hangisi))
print("Çıkış Orta Kümesine Üyeliği=", fuzz.interp_membership(var_fiyat, set_fiyat_orta, hangisi))
print("Çıkış Yüksek Kümesine Üyeliği=", fuzz.interp_membership(var_fiyat, set_fiyat_yuksek, hangisi))

plt.show()
