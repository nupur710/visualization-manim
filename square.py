from manim import *

class Pith(Scene):
    def construct(self):
        square = Square(side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.5)
        self.play(Create(square), run_time=3, rate_func=smooth, remover=True)
        self.wait()