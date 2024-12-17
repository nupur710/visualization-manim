from manim import *
class Get(Scene):
    def construct(self):
        r = Rectangle()
        self.add(r)

        center = r.get_center()
        right = r.get_right()
        left = r.get_left()
        top = r.get_top()
        bottom = r.get_bottom()

        up_right = r.get_corner(UR)
        up_left = r.get_corner(UL)
        down_right = r.get_corner(DR)
        down_left = r.get_corner(DL)

        for n,p in zip(["C", "R", "L", "T", "B", "UR", "UL", "DR", "DL"],
                       [center, right, left, top, bottom, up_right, up_left, down_right, down_left]):
            t = Text(f"{n}", color=RED)
            t.move_to(p)
            self.add(t)