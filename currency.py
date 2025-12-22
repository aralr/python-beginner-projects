pesos = int(input('What do you have left in pesos?'))
soles = int(input('What do you have left in soles?'))
reais = int(input('What do you have left in reais?'))
usd_from_reais = reais / 5.58 
usd_from_soles = soles / 3.37 
usd_from_pesos = pesos / 3798.07 
total_usd = usd_from_reais + usd_from_soles +usd_from_pesos
print(total_usd)
