from manim import *
class Shift(Scene):
    def construct(self):
        s = Square()
        c = Circle()
        self.add(s,c)

        for _ in range(4):
            self.wait()
            c.shift(RIGHT)
            s.move_to(RIGHT) #move to takes refrence as np.array([0,0,0]) so each time moves to the same pos