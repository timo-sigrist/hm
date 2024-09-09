verkaufte_menge = 20000
nettoerloes = 2000000
handels_W_A = 1200000 # W = Wertschöpfung? A = Aufwand --> Variable (Einzel-)Kosten
gemeinkosten = 600000 # Fixe Kosten

# Reingewinn
reingewinn = nettoerloes - handels_W_A - gemeinkosten
print(f"Reingewinn: {reingewinn}\n")

# DB pro Stück
db_pro_stueck = (nettoerloes / verkaufte_menge) - (handels_W_A / verkaufte_menge)
print(f"DB / Bruttogewinn pro Stück: {db_pro_stueck}\n")

# Nutzschwelle
mengenmaessige_nutzschwelle = gemeinkosten / db_pro_stueck
print(f"Nutzschwelle: {mengenmaessige_nutzschwelle} Stück\n")

# Wieviel Stück müssen verkauft werden, damit der Reingewinn xxx beträgt?
reingewinn = 0.3e6
gesuchte_anzahl = (handels_W_A - reingewinn) / db_pro_stueck
print(f"Um {reingewinn} Reingewinn zu erreichen, müssen {gesuchte_anzahl} Stück verkauft werden.")