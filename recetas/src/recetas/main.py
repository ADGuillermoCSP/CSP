from datetime import datetime, timedelta

from recetas.models.plato import Plato
from recetas.models.menu_semanal import MenuSemanal
from recetas.models.plato_dia import PlatoDelDia
from recetas.models.ingrediente import Ingrediente
from recetas.enums.tipo_plato import TipoPlato
from recetas.enums.temporada import Temporada


def main():
    ingrediente = Ingrediente(1, "Tomate", "gramos")

    plato = Plato(1, "Ensalada", "Cortar y mezclar", "foto.jpg", Temporada.VERANO)
    plato.agregar_ingrediente(ingrediente, "200g")

    plato_dia = PlatoDelDia(1, datetime.now(), TipoPlato.COMIDA, plato)

    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=7)

    menu = MenuSemanal(1, fecha_inicio, fecha_fin)
    menu.agregar_plato_del_dia(plato_dia)

    print(menu)
    print(plato)

    print("\nIngredientes del plato:")
    for ingrediente_plato in plato.get_ingredientes():
        print(ingrediente_plato)

    print("\nNúmero de platos en el menú:")
    print(len(menu))

    print("\nBuscar platos por fecha:")
    platos = menu.obtener_platos_por_fecha(plato_dia.get_fecha())
    for p in platos:
        print(p)

    print("\n¿La fecha pertenece a la semana del menú?")
    print(menu.buscar_por_semana(datetime.now()))

    print("\nComparación de ingredientes:")
    ingrediente2 = Ingrediente(1, "Tomate", "gramos")
    print(ingrediente == ingrediente2)

    print("\nComparación de platos:")
    plato2 = Plato(1, "Ensalada", "Cortar y mezclar", "foto.jpg", Temporada.VERANO)
    print(plato == plato2)


if __name__ == "__main__":
    main()