# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:24:28 2023

@author: sedat
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Evrensel küme tanımlamaları
sicaklik = ctrl.Antecedent(np.arange(20, 81, 1), 'sicaklik')
sicaklik_degisim = ctrl.Antecedent(np.arange(0, 6, 0.1), 'sicaklik_degisim')
motor_hizi = ctrl.Consequent(np.arange(100, 1001, 1), 'motor_hizi')

# Üyelik fonksiyonları tanımlamaları
sicaklik['Low'] = fuzz.trimf(sicaklik.universe, [20, 25, 35])
sicaklik['Med'] = fuzz.trimf(sicaklik.universe, [30, 42, 55])
sicaklik_degisim['Low'] = fuzz.trimf(sicaklik_degisim.universe, [0, 0.3, 1])
sicaklik_degisim['Med'] = fuzz.trimf(sicaklik_degisim.universe, [0.5, 1.3, 2])
motor_hizi['Slow'] = fuzz.trimf(motor_hizi.universe, [300, 400, 500])


# Kurallar
rule1 = ctrl.Rule(sicaklik['Low'] & sicaklik_degisim['Low'], motor_hizi['Fast'])
rule2 = ctrl.Rule(sicaklik['Med'] & sicaklik_degisim['Med'], motor_hizi['Slow'])
rule3 = ctrl.Rule(sicaklik['Low'] & sicaklik_degisim['Med'], motor_hizi['Fast'])
rule4 = ctrl.Rule(sicaklik['Med'] & sicaklik_degisim['Low'], motor_hizi['Med'])

# Kuralları içeren kontrol sistemi oluştur
motor_hizlari_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

# Kuralları kontrol sistemi ile birleştir
motor_hizlari = ctrl.ControlSystemSimulation(motor_hizlari_ctrl)

# Giriş değerlerini sisteme ver
motor_hizlari.input['sicaklik'] = 35
motor_hizlari.input['sicaklik_degisim'] = 1

# Çıkarımı yap
motor_hizlari.compute()

# Sonucu görüntüle
print(motor_hizlari.output['motor_hizi'])

# Çıkarım grafiğini çiz
motor_hizi.view(sim=motor_hizlari)
