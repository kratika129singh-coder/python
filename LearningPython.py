f=set()
print(type(f))

f={}
print(type(f))

city1={'Aligarh','Delhi','Jaipur','Jay'}
city2={'Mathura','Jaipur','Mathura','Goa'}
place=city1.union(city2)#for taking union of both sets
place1=city1.intersection(city2)# fro taking intersection item in both sets
city1.intersection_update(city2)
print(city1)
place2=city1.symmetric_difference(city2)
city1.symmetric_difference_update(city2)
print(city1)
print(city1.isdisjoint(city2))
print(city1.issuperset(city2))
city2.remove("Goa")
print(city2) 
city2.discard("Goa")
print(city2)

