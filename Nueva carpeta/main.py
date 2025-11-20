from database import Database
from ui import MotoShopApp
from seed_data import populate_initial_moto_products


def main():
    """Punto de entrada principal de la aplicación MotoShop."""

    # 1. Inicializar la base de datos
    db = Database(db_file="motoshop.db")

    # 2. Poblar la base de datos con datos iniciales si está vacía
    if not db.get_products():  # Pythonic: las listas vacías son False
        populate_initial_moto_products(db)
        print("✅ Base de datos poblada con productos iniciales para negocio de motos.")

    # 3. Inicializar la interfaz de usuario
    app = MotoShopApp(db)

    # 4. Ejecutar la aplicación
    app.mainloop()


if __name__ == "__main__":
    main()
