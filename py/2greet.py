def greet(greeting: str, people: list[str]) -> None:
    for person in people:
        print(f'{greeting}, {person}!')

greet('Ciao', ['Lia','Hency','Zyrel','JM'])