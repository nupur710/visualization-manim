from manim import *

class Grid(Scene):
    def construct(self):
        for i in range (0,5):
            for j in range (0,4):
                square = Square(side_length=2)
                self.play(Create(square),remove=True)
        self.wait()