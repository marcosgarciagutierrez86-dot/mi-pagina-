from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Conecta a la base de datos
    conn = sqlite3.connect('don_cheto.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Consultamos las categorías para el menú de tu imagen
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    conn.close()
    
    # Enviamos los datos al archivo HTML
    return render_template('Mi Pagina.html', categorias=categorias)

if __name__ == '__main__':
    app.run(debug=True)
