from manim import *
class Rect(Scene):
    def construct(self):
        req = Rectangle()
        req.move_to([-3,2,0])
        self.play(Create(req))
        self.wait()