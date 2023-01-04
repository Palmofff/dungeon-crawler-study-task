from chars.char_creation import *
from utils.details import *
from chains.chain import *


def run():
    create_char()
    while game_exe.progress:
        chained(death)
