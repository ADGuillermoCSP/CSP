class Plato:
    """Representa una receta o plato de cocina."""

    def __init__(self, id_: int, nombre: str, preparacion: str, foto: str, temporada):
        self._id = id_
        self.nombre = nombre
        self.preparacion = preparacion
        self.foto = foto
        self.temporada = temporada
        self._ingredientes = []

    def agregar_ingrediente(self, ingrediente, cantidad: str):
        """Añade un ingrediente al plato."""
        from .plato_ingrediente import PlatoIngrediente

        self._ingredientes.append(PlatoIngrediente(ingrediente, cantidad))

    def get_ingredientes(self):
        return self._ingredientes

    @classmethod
    def buscar_por_nombre(cls, nombre: str):
        """Simula la búsqueda de un plato."""
        return None

    def __str__(self):
        return f"Plato: {self.nombre}"

    def __eq__(self, other):
        if not isinstance(other, Plato):
            return False
        return self._id == other._id