
class Producto:
    def __init__(self,nombre,precio):#agregamos los atributos init y parametros
        self.nombre=nombre
        self.precio=precio 
    def mostrar(self):
        print("producto:", self.nombre,"precio: ", self.precio)
    
    


p1= Producto("tatin", 60)
p2= Producto("terrabusi", 70)
p3= Producto("sol serrano", 50)
p4= Producto("aguila", 90)

while True:
    menu= input("1-tatin\n 2-terrabusi\n 3-sol serrano\n 4-aguila\n ingrese: ")
    if menu=="1":
        p1.mostrar()
        cantidad= int(input("ingrese la cantidad: "))
        total= cantidad*60
        print("el total es: ",total)
    elif menu=="2":
        p2.mostrar()
        cantidad= int(input("ingrese la cantidad: "))
        total= cantidad*70
        print(" el total es:",total)
    elif menu=="3":
        p3.mostrar()
        cantidad= int(input("ingrese la cantidad: "))
        total= cantidad*50
        print(" el total es:",total)
    else:
        p4.mostrar()
        cantidad= int(input("ingrese la cantidad: "))
        total= cantidad*90
        print(" el total es:",total)
            
    preg=input("desea ingresar otro producto s/n")  
    if preg=="n":
        
     break
    