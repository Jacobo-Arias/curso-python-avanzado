DATA = [
    {
        "name": "Facundo",
        "age": 72,
        "organization": "Platzi",
        "position": "Technical Coach",
        "language": "python",
    },
    {
        "name": "Luisana",
        "age": 33,
        "organization": "Globant",
        "position": "UX Designer",
        "language": "javascript",
    },
    {
        "name": "Héctor",
        "age": 19,
        "organization": "Platzi",
        "position": "Associate",
        "language": "ruby",
    },
    {
        "name": "Gabriel",
        "age": 20,
        "organization": "Platzi",
        "position": "Associate",
        "language": "javascript",
    },
    {
        "name": "Isabella",
        "age": 30,
        "organization": "Platzi",
        "position": "QA Manager",
        "language": "java",
    },
    {
        "name": "Karo",
        "age": 23,
        "organization": "Everis",
        "position": "Backend Developer",
        "language": "python",
    },
    {
        "name": "Ariel",
        "age": 32,
        "organization": "Rappi",
        "position": "Support",
        "language": "",
    },
    {
        "name": "Juan",
        "age": 17,
        "organization": "",
        "position": "Student",
        "language": "go",
    },
    {
        "name": "Pablo",
        "age": 32,
        "organization": "Master",
        "position": "Human Resources Manager",
        "language": "python",
    },
    {
        "name": "Lorena",
        "age": 56,
        "organization": "Python Organization",
        "position": "Language Maker",
        "language": "python",
    },
]


def run():
    all_python_devs = [
        worker["name"] for worker in DATA if worker["language"] == "python"
    ]
    print(all_python_devs)

    all_platzi_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    for dev in all_platzi_devs:
        print(dev["name"])

    all_platzi_workers = [
        worker["name"] for worker in DATA if worker["organization"] == "Platzi"
    ]
    print(all_platzi_workers)

    all_platzi_workers = list(
        filter(lambda worker: worker["organization"] == "Platzi", DATA)
    )
    for worker in all_platzi_workers:
        print(worker["name"])

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print(adults)

    # El simbolo de pipe | une dos diccionarios pero solo en python 3.9
    # old_people = list(map(lambda worker: worker | {'old':worker['age']>70},DATA))
    def union(dict1, old):
        dict1["old"] = old
        return dict1

    old_people = list(map(lambda worker: union(worker, worker["age"] > 70), DATA))
    for old in old_people:
        print(old)


if __name__ == "__main__":
    run()
