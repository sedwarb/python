from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,filter(lambda numero: numero%2!=0,lista)))