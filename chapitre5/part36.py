jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
print(jour)
print(jour[2])
print(jour[4])
jour[3] = jour[3] +47
print(jour)
jour[3] = 'Juillet'
print(jour)
print(len(jour))
del(jour[4])
print(jour)
jour.append('samedi')
print(jour)

