from manim import *
class MultipleAnimations(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Create(square),FadeIn(circle))

        self.wait()