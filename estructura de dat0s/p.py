class provedor:#creamos clase con un provedor 
    def _init_(self,precio,vendedor)
      self.precio= precio 
      self.vendedeor= vendedor
    
    def mostrar(self):
        print("precio: ", self.precio,"vendedor:", self.vendedor)
    
while True:
        p1= provedor("pepsi",80)
        p1.mostrar()
        
        producto=input("ingrese el nombre de la gaseosa: ")
        precio= int(input("ingrese el precio de la gaseosa/producto "))
        
        
        
        p2= provedor(precio, vendedor)
        p2.mostrar()
        
        o=input( " desea crear otra gaseosa7producto: s/n")
        if o=="n":
         break
        else:
            precio= input("ingrese el precio de la provedor3:")
            vendedor= int(input("ingrese el provedor de la provedor3")) 
            p3=provedor(precio,vendedor)
            p3.mostrar()
        
            
        