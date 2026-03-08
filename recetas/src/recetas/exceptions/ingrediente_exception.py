class IngredienteNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un ingrediente."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje)