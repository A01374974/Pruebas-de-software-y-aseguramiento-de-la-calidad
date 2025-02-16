import json
import os
import unittest


class Hotel:
    def __init__(self, nombre, ubicacion, total_habitaciones):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.total_habitaciones = total_habitaciones
        self.habitaciones_disponibles = total_habitaciones

    def reservar_habitacion(self):
        if self.habitaciones_disponibles > 0:
            self.habitaciones_disponibles -= 1
            return True
        return False

    def cancelar_reserva(self):
        if self.habitaciones_disponibles < self.total_habitaciones:
            self.habitaciones_disponibles += 1
            return True
        return False

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "total_habitaciones": self.total_habitaciones,
            "habitaciones_disponibles": self.habitaciones_disponibles
        }

    @classmethod
    def desde_dict(cls, datos):
        return cls(
            datos['nombre'],
            datos['ubicacion'],
            datos['total_habitaciones']
        )


class Cliente:
    def __init__(self, id_cliente, nombre, informacion_contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.informacion_contacto = informacion_contacto

    def a_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "informacion_contacto": self.informacion_contacto
        }

    @classmethod
    def desde_dict(cls, datos):
        return cls(
            datos['id_cliente'],
            datos['nombre'],
            datos['informacion_contacto']
        )


class Reserva:
    def __init__(self, cliente, hotel):
        self.cliente = cliente
        self.hotel = hotel
        self.esta_activa = False

    def crear(self):
        if self.hotel.reservar_habitacion():
            self.esta_activa = True
            return True
        return False

    def cancelar(self):
        if self.esta_activa:
            if self.hotel.cancelar_reserva():
                self.esta_activa = False
                return True
        return False

    def a_dict(self):
        return {
            "cliente": self.cliente.a_dict(),
            "hotel": self.hotel.a_dict(),
            "esta_activa": self.esta_activa
        }

    @classmethod
    def desde_dict(cls, datos):
        cliente = Cliente.desde_dict(datos["cliente"])
        hotel = Hotel.desde_dict(datos["hotel"])
        return cls(cliente, hotel)


class AdministradorDeHoteles:
    @staticmethod
    def crear_hotel(hotel):
        if not os.path.exists("hoteles.json"):
            with open("hoteles.json", "w") as archivo:
                json.dump([], archivo)
        with open("hoteles.json", "r+") as archivo:
            hoteles = json.load(archivo)
            hoteles.append(hotel.a_dict())
            archivo.seek(0)
            json.dump(hoteles, archivo)

    @staticmethod
    def eliminar_hotel(nombre_hotel):
        if os.path.exists("hoteles.json"):
            with open("hoteles.json", "r+") as archivo:
                hoteles = json.load(archivo)
                hoteles = [hotel for hotel in hoteles
                           if hotel["nombre"] != nombre_hotel]
                archivo.seek(0)
                archivo.truncate()
                json.dump(hoteles, archivo)

    @staticmethod
    def mostrar_hoteles():
        if os.path.exists("hoteles.json"):
            with open("hoteles.json", "r") as archivo:
                hoteles = json.load(archivo)
                for hotel in hoteles:
                    print(hotel)

    @staticmethod
    def modificar_info_hotel(nombre_hotel, datos_actualizados):
        if os.path.exists("hoteles.json"):
            with open("hoteles.json", "r+") as archivo:
                hoteles = json.load(archivo)
                for hotel in hoteles:
                    if hotel["nombre"] == nombre_hotel:
                        hotel.update(datos_actualizados)
                        archivo.seek(0)
                        archivo.truncate()
                        json.dump(hoteles, archivo)
                        return True
        return False


class AdministradorDeClientes:
    @staticmethod
    def crear_cliente(cliente):
        if not os.path.exists("clientes.json"):
            with open("clientes.json", "w") as archivo:
                json.dump([], archivo)
        with open("clientes.json", "r+") as archivo:
            clientes = json.load(archivo)
            clientes.append(cliente.a_dict())
            archivo.seek(0)
            json.dump(clientes, archivo)

    @staticmethod
    def eliminar_cliente(id_cliente):
        if os.path.exists("clientes.json"):
            with open("clientes.json", "r+") as archivo:
                clientes = json.load(archivo)
                clientes = [cliente for cliente in clientes
                            if cliente["id_cliente"] != id_cliente]
                archivo.seek(0)
                archivo.truncate()
                json.dump(clientes, archivo)

    @staticmethod
    def modificar_info_cliente(id_cliente, datos_actualizados):
        if os.path.exists("clientes.json"):
            with open("clientes.json", "r+") as archivo:
                clientes = json.load(archivo)
                for cliente in clientes:
                    if cliente["id_cliente"] == id_cliente:
                        cliente.update(datos_actualizados)
                        archivo.seek(0)
                        archivo.truncate()
                        json.dump(clientes, archivo)
                        return True
        return False


class AdministradorDeReservas:
    @staticmethod
    def crear_reserva(reserva):
        if reserva.crear():
            if not os.path.exists("reservas.json"):
                with open("reservas.json", "w") as archivo:
                    json.dump([], archivo)
            with open("reservas.json", "r+") as archivo:
                reservas = json.load(archivo)
                reservas.append(reserva.a_dict())
                archivo.seek(0)
                json.dump(reservas, archivo)

    @staticmethod
    def cancelar_reserva(reserva):
        if reserva.cancelar():
            if os.path.exists("reservas.json"):
                with open("reservas.json", "r+") as archivo:
                    reservas = json.load(archivo)
                    reservas = [res for res in reservas
                                if res["cliente"]["id_cliente"]
                                != reserva.cliente.id_cliente]
                    archivo.seek(0)
                    archivo.truncate()
                    json.dump(reservas, archivo)


class Prueba(unittest.TestCase):

    def test_crear_hotel(self):
        hotel = Hotel("Hilton", "Avenida Juarez", 100)
        AdministradorDeHoteles.crear_hotel(hotel)
        with open("hoteles.json", "r") as archivo:
            hoteles = json.load(archivo)
            self.assertEqual(len(hoteles), 1)

    def test_crear_cliente(self):
        cliente = Cliente("11", "Octavio Altamirano", "55638902")
        AdministradorDeClientes.crear_cliente(cliente)
        with open("clientes.json", "r") as archivo:
            clientes = json.load(archivo)
            self.assertEqual(len(clientes), 1)

    def test_crear_reserva(self):
        hotel = Hotel("Hilton", "Avenida Juarez", 100)
        cliente = Cliente("11", "Octavio Altamirano", "55638902")
        reserva = Reserva(cliente, hotel)
        AdministradorDeReservas.crear_reserva(reserva)
        with open("reservas.json", "r") as archivo:
            reservas = json.load(archivo)
            self.assertEqual(len(reservas), 1)

    def test_cancelar_reserva(self):
        hotel = Hotel("Hilton", "Avenida Juarez", 100)
        cliente = Cliente("11", "Octavio Altamirano", "55638902")
        reserva = Reserva(cliente, hotel)
        AdministradorDeReservas.crear_reserva(reserva)
        AdministradorDeReservas.cancelar_reserva(reserva)
        with open("reservas.json", "r") as archivo:
            reservas = json.load(archivo)
            self.assertEqual(len(reservas), 0)


if __name__ == "__main__":
    unittest.main()
