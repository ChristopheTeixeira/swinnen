nbsecan = 117582195
reste = nbsecan % 31536000
année = nbsecan - reste
année = année / 31536000
ResteMois = reste % 2592000
mois = reste - ResteMois
mois = mois / 2592000
ResteJours = ResteMois % 86400
jours = ResteMois - ResteJours
jours = jours / 86400
ResteHeures = ResteJours % 3600
heures = ResteJours - ResteHeures
heures = heures / 3600
ResteMinutes = ResteHeures % 60
minutes = ResteHeures - ResteMinutes
minutes = minutes / 60
secondes = ResteMinutes
print(nbsecan, "secondes équivaut à",int(année),"an(s),",int(mois),"mois,",int(jours),"jour(s),",int(heures),"heure(s),",int(minutes),"minute(s) et", int(secondes),"seconde(s).")



