##UNION BETWEEN CONJUNTOS
set_a = {'col','mex','bol'}
set_b = {'per','bol'}
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

##INTERSECTION
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

##DIFFERENCE (Elements of A menus the common elements)
set_c = set_a.difference(set_b)
print(set_c)
print(set_a-set_b)

#SYMETRIC DIFFERENCE (Union between two conjuntos without the common elements)
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
