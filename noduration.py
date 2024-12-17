from manim import *
class NoDuration(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.wait()