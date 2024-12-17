from manim import *
class Rect(Scene):
    def construct(self):
        r = Rectangle()
        c = Circle()
        e = Ellipse()
        r.move_to(np.array([-3,2,0]))
        c.move_to(LEFT * 3 + UP * 2)
        e.move_to(UP * 2 + LEFT)
        self.play(Create(r), Create(c), Create(e))
        self.wait()