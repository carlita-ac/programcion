import sqlite3
from typing import List, Tuple, Optional
from ui import MotoShopApp

class Database:
    """
    Clase para manejar la base de datos del negocio de motos.
    Administra productos como motos, repuestos y accesorios.
    """

    def __init__(self, db_file: str = "motoshop.db"):
        self.db_file = db_file
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_file)

    def _create_tables(self):
        """Crea las tablas necesarias para el negocio de motos."""
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,   -- moto, repuesto, accesorio
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                description TEXT
            );
            """
        )

        conn.commit()
        conn.close()

    # ----------------------------------------------------------------------
    # CRUD Productos
    # ----------------------------------------------------------------------

    def add_product(self, name: str, category: str, price: float, stock: int, description: str = ""):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO products (name, category, price, stock, description) VALUES (?, ?, ?, ?, ?)",
            (name, category, price, stock, description),
        )

        conn.commit()
        conn.close()

    def get_products(self) -> List[Tuple]:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        conn.close()
        return rows

    def get_product(self, product_id: int) -> Optional[Tuple]:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()

        conn.close()
        return product

    def update_product(self, product_id: int, name: str, category: str, price: float, stock: int, description: str = ""):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products
            SET name = ?, category = ?, price = ?, stock = ?, description = ?
            WHERE id = ?
            """,
            (name, category, price, stock, description, product_id),
        )

        conn.commit()
        conn.close()

    def delete_product(self, product_id: int):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

        conn.commit()
        conn.close()
