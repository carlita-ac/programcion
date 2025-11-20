import tkinter as tk
from tkinter import ttk, messagebox
from models import Product
import datetime

class MotoShopApp(tk.Tk):
    """Interfaz gráfica para manejar productos y compras usando el modelo Product."""

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("MotoShop - Gestión y Compras")
        self.geometry("1000x650")

        self._build_ui()
        self.load_products()

    def _build_ui(self):
        form_frame = tk.Frame(self, padx=10, pady=10)
        form_frame.pack(fill="x")

        tk.Label(form_frame, text="Nombre:").grid(row=0, column=0)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Categoría:").grid(row=1, column=0)
        self.category_entry = ttk.Combobox(form_frame, values=["moto", "repuesto", "accesorio"])
        self.category_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Precio:").grid(row=2, column=0)
        self.price_entry = tk.Entry(form_frame)
        self.price_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Stock:").grid(row=3, column=0)
        self.stock_entry = tk.Entry(form_frame)
        self.stock_entry.grid(row=3, column=1)

        tk.Label(form_frame, text="Descripción:").grid(row=4, column=0)
        self.desc_entry = tk.Entry(form_frame, width=50)
        self.desc_entry.grid(row=4, column=1, columnspan=2, sticky="w")

        tk.Label(form_frame, text="Cantidad a comprar:").grid(row=5, column=0)
        self.qty_entry = tk.Entry(form_frame)
        self.qty_entry.grid(row=5, column=1)
        self.qty_entry.insert(0, "1")

        tk.Button(form_frame, text="Agregar Producto", command=self.add_product).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(form_frame, text="Comprar Producto Seleccionado", command=self.buy_product).grid(row=6, column=2, padx=20)

        columns = ("ID", "Nombre", "Categoría", "Precio", "Stock", "Descripción")
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(fill="both", expand=True, pady=10)

    def load_products(self):
        for row in self.table.get_children():
            self.table.delete(row)
        products = self.db.get_products()
        for p in products:
            prod = Product.from_tuple(p)
            self.table.insert("", "end", values=(prod.id, prod.name, prod.category, prod.price, prod.stock, prod.description))

    def add_product(self):
        name = self.name_entry.get().strip()
        category = self.category_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        desc = self.desc_entry.get().strip()

        if not name or not category or not price or not stock:
            messagebox.showerror("Error", "Todos los campos excepto descripción son obligatorios.")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser decimal y stock entero.")
            return

        prod = Product(None, name, category, price, stock, desc)
        self.db.add_product(*prod.to_tuple())
        self.load_products()

        self.name_entry.delete(0, tk.END)
        self.category_entry.set("")
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Producto agregado correctamente.")

    def buy_product(self):
        selected = self.table.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione un producto para comprar.")
            return

        values = self.table.item(selected[0], "values")
        prod_id, name, category, price, stock, desc = values

        price = float(price)
        stock = int(stock)

        try:
            qty = int(self.qty_entry.get())
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida mayor a 0.")
            return

        if qty > stock:
            messagebox.showerror("Stock insuficiente", f"Solo hay {stock} unidades disponibles.")
            return

        new_stock = stock - qty
        self.db.update_product(prod_id, name, category, price, new_stock, desc)
        self.load_products()

        invoice = self.generate_invoice(name, price, qty)
        messagebox.showinfo("Factura Generada", f"Compra realizada. Factura:\n\n{invoice}")

    def generate_invoice(self, product_name, price, qty):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = price * qty
        invoice_text = (
            f"----- FACTURA MOTOSHOP -----\n"
            f"Fecha: {now}\n"
            f"Producto: {product_name}\n"
            f"Cantidad: {qty}\n"
            f"Total: ${total:.2f}\n"
            f"Gracias por su compra."
        )
        return invoice_text