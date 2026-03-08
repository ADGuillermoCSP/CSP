class MenuSemanal:
    """Representa el menú de una semana."""

    def __init__(self, id_: int, fecha_inicio, fecha_fin):
        self._id = id_
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self._platos_del_dia = []

    def agregar_plato_del_dia(self, plato_dia):
        self._platos_del_dia.append(plato_dia)

    def obtener_platos_por_fecha(self, fecha):
        return [p for p in self._platos_del_dia if p.fecha == fecha]

    def buscar_por_semana(self, fecha):
        return self.fecha_inicio <= fecha <= self.fecha_fin

    def __len__(self):
        return len(self._platos_del_dia)

    def __str__(self):
        return f"Menú semanal ({self.fecha_inicio.date()} - {self.fecha_fin.date()})"