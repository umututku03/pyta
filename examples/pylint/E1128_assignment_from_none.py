from typing import List

def add_fruit(fruit_basket: List[str], fruit: str) -> None:
    fruit_basket.append(fruit)
    return None


def main():
    fruit_basket = ['apple', 'apple', 'orange']
    new_fruit_basket = add_fruit(fruit_basket, 'banana')  # Error on this line
    print(new_fruit_basket)  # Prints `None`
