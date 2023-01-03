class Game_Object():
    def __init__(self, progress: bool, difficult: int):
        self.progress = progress
        self.difficult = difficult

game = Game_Object(True, 1)