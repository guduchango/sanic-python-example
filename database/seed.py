import argparse
from faker import Faker
from models.item_model import create_item  # Suponiendo que tienes la función de crear un item en tu modelo
import random

fake = Faker()

def generate_fake_data(n=10):
    """
    Genera datos falsos para insertar en la base de datos.
    """
    for _ in range(n):
        name = fake.word().capitalize()  # Genera una palabra aleatoria como nombre
        description = fake.text(max_nb_chars=200)  # Genera una descripción aleatoria
        price = round(random.uniform(5.0, 500.0), 2)  # Precio aleatorio entre 5 y 500
        create_item(name, description, price)
        print(f"Item creado: {name}, ${price}")

def main():
    parser = argparse.ArgumentParser(description="Generar datos falsos para la base de datos.")
    parser.add_argument("--count", type=int, default=10, help="Número de items a crear")
    args = parser.parse_args()

    generate_fake_data(args.count)

if __name__ == "__main__":
    main()