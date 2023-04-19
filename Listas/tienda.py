
class Tienda:
    
    def __init__(self, productos = []):
        """
        Método constructor de la clase
        Params:
            productos(list): Lista de productos de la tienda
        Returns:
            None.
        """
        self.__productos = productos
        self.__etiquetas = ["Producto: ","Nombre: ","Descripción: ", "Precio: ", "Existencias: "]

    def alta(self,clave:str,nombre:str,inf:str,precio:float,cantidad:int):
        """
        Método para dar de alta un nuevo producto
        Params:
            clave(str): Identificador del producto
            nombre(str): Nombre del producto
            inf(str): Descripción del producto
            precio(float): Precio del producto
            cantidad(int): Cantidad en existencia del producto
        Returns:
            str: Mensaje de confirmación
        """
        for prod in self.__productos:
            if prod[0] == clave:
                return f"Ya existe la clave {clave} del producto\n"
            
        producto = [clave,nombre,inf,precio,cantidad]
        self.__productos.append(producto)
        return f"Se ha agregado el producto {nombre} con clave {clave} correctamente\n"

    def validar(self,clave:str):
        """
        Método para validar la existencia de un producto
        Params:
            clave(str): Identificador del producto
        Returns:
            bool: Si el producto existe True, en caso contrario False
        """
        for prod in self.__productos:
            return prod[0] == clave

    def baja(self,clave:str):
        """
        Método para dar de baja un producto
        Params:
            clave(str): Identificador del producto
        Returns:
            str: Mensaje de confirmación
        """
        for prod in self.__productos:
            if prod[0] == clave:
                self.__productos.remove(prod)
                return f"Producto {clave} dado de baja\n"

    def consultarC(self,clave:str):
        """
        Método para consultar un producto por medio del identificador
        Params:
            clave(str): Identificador del producto
        Returns:
            str: Datos del producto
        """
        for producto in self.__productos:
            if producto[0] == clave:
                aux = ""
                for i in range(len(producto)):
                    aux += self.__etiquetas[i] + str(producto[i]) + "\n"
                return aux
                    
        return "Producto no encontrado\n\n"

    def consultarN(self,nombre:str):
        """
        Método para consultar un producto por medio del nombre
        Params:
            nombre(str): Nombre del producto
        Returns:
            str: Datos del producto
        """
        for producto in self.__productos:
            if producto[1] == nombre:
                aux = ""
                for i in range(len(producto)):
                    aux += self.__etiquetas[i] + str(producto[i]) + "\n"
                return aux
            
        return "Producto no encontrado\n\n"

    def consultar(self):
        """
        Método para consultar todos los productos
        Params:
            None.
        Returns:
            str: Datos de los productos
        """
        if len(self.__productos) > 0:
            for producto in self.__productos:
                aux = ""
                for i in range(len(producto)):
                    aux += self.__etiquetas[i] + str(producto[i]) + "\n"
                print(aux)
        else:
            return "No hay productos que mostrar\n\n"

    
        
