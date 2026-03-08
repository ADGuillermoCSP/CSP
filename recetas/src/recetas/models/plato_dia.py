class PlatoDelDia:
    """Representa un plato asignado a una fecha concreta."""

    def __init__(self, id_: int, fecha, tipo, plato):
        self._id = id_
        self.fecha = fecha
        self.tipo = tipo
        self.plato = plato

    def get_fecha(self):
        return self.fecha

    def get_tipo(self):
        return self.tipo

    def get_plato(self):
        return self.plato

    def __str__(self):
        return f"{self.fecha.date()} - {self.plato}"