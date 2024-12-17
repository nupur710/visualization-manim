from manim import *
class Shift(Scene):
    def construct(self):
        s = Square()
        c = Circle()
        # Apply move_to 4 times
        for _ in range(4):
            s.move_to(RIGHT)

        # Apply shift 4 times
        for _ in range(4):
            c.shift(RIGHT)

        self.add(s,c)
