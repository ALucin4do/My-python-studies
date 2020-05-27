x=input("Por favor, entre com o número de segundos que deseja converter: ")
d=int(x)//86400
t=int(x)%86400
h=t//3600
y=t%3600
m=y//60
s=y%60
print(d,"dias,",h,"horas,",m,"minutos e",s,"segundos.")
