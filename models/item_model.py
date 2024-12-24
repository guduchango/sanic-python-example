from database.db import get_connection

def get_all_items():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id,name,description,price FROM items")
        return cursor.fetchall()

def get_item_by_id(item_id):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id,name,description,price FROM items WHERE id = %s", (item_id,))
        return cursor.fetchone()

def create_item(name, description, price):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, description, price) VALUES (%s, %s, %s)",
            (name, description, price)
        )
        conn.commit()

def update_item(item_id, name, description, price):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE items SET name = %s, description = %s, price = %s WHERE id = %s",
            (name, description, price, item_id)
        )
        conn.commit()

def delete_item(item_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
        conn.commit()