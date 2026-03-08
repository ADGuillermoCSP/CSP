class Ingrediente:
    """Representa un ingrediente utilizado en recetas."""

    def __init__(self, id_: int, nombre: str, unidad_medida: str):
        self._id = id_
        self.nombre = nombre
        self.unidad_medida = unidad_medida

    @classmethod
    def buscar_platos(cls):
        """Método de ejemplo que buscaría platos por ingrediente."""
        return []

    def __str__(self):
        return f"{self.nombre} ({self.unidad_medida})"

    def __eq__(self, other):
        if not isinstance(other, Ingrediente):
            return False
        return self._id == other._id