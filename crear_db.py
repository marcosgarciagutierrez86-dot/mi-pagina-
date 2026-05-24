import sqlite3

# Crear/Conectar a la base de datos
conexion = sqlite3.connect('don_cheto.db')
cursor = conexion.cursor()

# Crear la tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        archivo_html TEXT NOT NULL
    )
''')

# Insertar datos de prueba
datos = [
    ('Limpieza', 'limpieza.html'),
    ('Bebidas', 'bebidas.html'),
    ('Lácteos', 'lacteos.html')
]

cursor.executemany('INSERT INTO categorias (nombre, archivo_html) VALUES (?, ?)', datos)

conexion.commit()
conexion.close()
print("Base de datos creada con éxito")
