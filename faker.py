from contextlib import contextmanager
from typing import Tuple, Union, Optional


class Faker(object):
    def __init__(self, tellos_ints):
        self.tellos = tellos_ints
        self.grid_x = []
        self.grid_y = []
        self.grid_z = []
        self.tello_map = {}

    def __enter__(self):
        print("Starting Faker")
        for tello in self.tellos:
            self.tello_map[tello] = {}
        return self

    def __exit__(self):
        print("Exiting Faker")

    @contextmanager
    def sync_these():
        try:
            print('Syncing!')
        finally:
            print()

    def takeoff(self, tello: Union[int, str] = 'All', sync: bool = True) -> None:

        self.tello_map[tello]
