class Hotel:

    def __init__(self,habitaciones:list):
        """
        Método constructor de la clase

        Params:
            habitaciones(list): Lista con objetos Habitacion
        """
        self.__habitaciones = habitaciones


    def tipo_habitaciones_dis(self):
        """
        Método para mostrar los tipos de habitaciones en el hotel
        (No están ordenados por el aleatorio en que definimos las habitaciones)

        Params:
            None.
        Returns:
            disp(list): Lista con los nombres de los tipos de habitaciones disponibles en el hotel
        """
        disp = []
        for habitacion in self.__habitaciones:
            aux = habitacion.get_tipo().get_nombre()
            if aux not in disp:
                disp.append(aux)
        return disp

    def precios(self):
        """
        Método para obtener los precios de las habitaciones

        Params:
            None.
        Returns:
            disp(list): Lista con los precios de las habitaciones disponibles en el hotel (como el método anterior)
        """
        disp = []
        for habitacion in self.__habitaciones:
            aux = habitacion.get_tipo().get_precio()
            if aux not in disp:
                disp.append(aux)
        return disp
        
