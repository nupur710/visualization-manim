from manim import *
class ChangeDuration(Scene):
    def construct(self):
        self.play(Create(Square()), FadeIn(Circle()), run_time=3, rate_func=linear)
        self.wait()

