class Faker(object):
    def __init__(self, tellos_ints):
        self.tellos = tellos_ints

    def __enter__(self):
        print("Starting Faker")
        return self

    def __exit__(self):
        print("Exiting Faker")
