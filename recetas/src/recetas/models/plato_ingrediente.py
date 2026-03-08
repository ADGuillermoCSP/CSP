class PlatoIngrediente:
    """Relaciona un plato con un ingrediente y su cantidad."""

    def __init__(self, ingrediente, cantidad: str):
        self._ingrediente = ingrediente
        self._cantidad = cantidad

    def get_ingrediente(self):
        return self._ingrediente

    def get_cantidad(self):
        return self._cantidad

    def __str__(self):
        return f"{self._cantidad} de {self._ingrediente}"