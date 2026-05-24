from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def conectar_db():
    conn = sqlite3.connect('don_cheto.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = conectar_db()
    # Traemos las categorías de la tabla que creaste
    categorias = db.execute('SELECT * FROM categorias').fetchall()
    db.close()
    return render_template('Mi Pagina.html', categorias=categorias)

if __name__ == '__main__':
    app.run(debug=True)
