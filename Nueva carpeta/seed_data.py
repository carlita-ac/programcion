def populate_initial_moto_products(db):
    """Puebla la base de datos con productos iniciales del negocio de motos."""

    productos = [
        # ----------------------- MOTOS -----------------------
        ("Honda CB190R", "moto", 4200.00, 5, "Moto deportiva 190cc"),
        ("Yamaha FZ25", "moto", 5200.00, 3, "Moto naked 250cc"),
        ("Bajaj Pulsar NS200", "moto", 3800.00, 6, "Moto deportiva 200cc"),

        # ----------------------- CASCOS -----------------------
        ("Casco LS2 FF353", "accesorio", 120.00, 15, "Casco integral certificado"),
        ("Casco MT Thunder 3", "accesorio", 150.00, 10, "Casco sport touring"),

        # ----------------------- LLANTAS -----------------------
        ("Llanta Pirelli Diablo Rosso II", "repuesto", 95.00, 12, "Llanta trasera deportiva"),
        ("Llanta Michelin Pilot Street", "repuesto", 80.00, 10, "Llanta delantera 17"),

        # ----------------------- ACEITES -----------------------
        ("Aceite Motul 7100 10W40", "accesorio", 18.00, 25, "Aceite sintético premium"),
        ("Aceite Yamalube 20W50", "accesorio", 12.00, 30, "Aceite mineral para motos"),

        # ----------------------- REPUESTOS -----------------------
        ("Filtro de aire Honda CB190R", "repuesto", 14.00, 20, "Filtro original"),
        ("Bujía NGK Iridium", "repuesto", 10.00, 40, "Bujía de alto rendimiento"),
        ("Pastillas de freno Yamaha FZ", "repuesto", 16.00, 18, "Repuesto original"),
    ]

    for p in productos:
        db.add_product(*p)

    print("Inventario inicial de MotoShop cargado exitosamente.")
