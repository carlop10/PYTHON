""" Electiva de profundización 3 - 7A """
""" Autor: Carlos Lopez """
""" Fecha: 8 de octubre de 2025 """
""" Descripción: Implementación de la funcionalidad solicitada: total de una factura con posibles subfacturas. """
""" Ejercicio propuesto: 7) Crea una función que calcule el total a pagar de los ítems 
    y los subitems de una factura teniendo en cuenta esta estructura"""

class Factura:

    def __init__(self, factura):
        self.factura = factura

    def calcular_total(self):
        return self._calcular_total_factura(self.factura)

    def _calcular_total_factura(self, factura):
        total = 0
        for item, precio in factura.items():
            if isinstance(precio, dict):
                total += self._calcular_total_factura(precio)
            else:
                total += precio
        return total
    
if __name__ == "__main__":
    factura = {
        "Kit Escolar": {
            "Lápiz": 800,
            "Cuaderno": 3000,
            "Estuche de colores": {
                "Caja de colores": 8500,
                "Sacapuntas": 1200
            }
        },
        "Mochila": 25000,
        "Borrador": 1000
    }
    
    factura_obj = Factura(factura)
    total_a_pagar = factura_obj.calcular_total()
    print(f"Total a pagar de la factura: {total_a_pagar}")
