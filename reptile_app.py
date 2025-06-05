import json
import os

DATA_FILE = 'reptiles.json'

def load_reptiles():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_reptiles(reptiles):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(reptiles, f, indent=2, ensure_ascii=False)


def add_reptile():
    name = input('Name: ')
    species = input('Species: ')
    age = input('Age: ')
    reptiles = load_reptiles()
    reptiles.append({'name': name, 'species': species, 'age': age})
    save_reptiles(reptiles)
    print('Added!')


def list_reptiles():
    reptiles = load_reptiles()
    if not reptiles:
        print('No reptiles stored.')
    for r in reptiles:
        print(f"{r['name']} ({r['species']}) - age {r['age']}")


def remove_reptile():
    reptiles = load_reptiles()
    name = input('Name to remove: ')
    filtered = [r for r in reptiles if r['name'] != name]
    if len(filtered) == len(reptiles):
        print('Reptile not found!')
        return
    save_reptiles(filtered)
    print('Removed!')


def main():
    while True:
        print('1) Add reptile')
        print('2) List reptiles')
        print('3) Remove reptile')
        print('4) Quit')
        choice = input('> ')
        if choice == '1':
            add_reptile()
        elif choice == '2':
            list_reptiles()
        elif choice == '3':
            remove_reptile()
        elif choice == '4':
            break
        else:
            print('Invalid option!')


if __name__ == '__main__':
    main()
