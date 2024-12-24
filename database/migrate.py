import mysql.connector
from mysql.connector import Error
import os

def create_tables():
    """
    Crea las tablas necesarias en la base de datos.
    """
    try:
        # Configuración de conexión a MySQL
        connection = mysql.connector.connect(
            host= os.getenv('MYSQL_HOST', 'localhost'),   # Cambia esto según tu configuración
            user=os.getenv('MYSQL_USER', 'root'),          # Cambia el usuario
            password=os.getenv('MYSQL_PASSWORD', 'root_password'),   # Cambia la contraseña
            database=os.getenv('MYSQL_DATABASE', 'test_db')  # Cambia el nombre de la base de datos
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Crear tabla "items"
            create_items_table_query = """
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_items_table_query)
            connection.commit()
            print("Tabla 'items' creada exitosamente.")

    except Error as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    create_tables()