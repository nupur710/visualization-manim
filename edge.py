from manim import *

class Edge(Scene):
    # def construct(self):
    #     rect = Rectangle()
    #     rect.to_edge(LEFT)
    #     self.add(rect)
    #     rect2 = Rectangle()
    #     rect2.to_edge(UP)
    #     rect2.to_edge(LEFT)
    #     self.add(rect2)
    #     req = Rectangle()
    #     req.to_edge(DOWN)
    #     req.to_edge(LEFT,buff=0)
    #     self.add(req)

    def construct(self):
        req = Rectangle()
        req.to_corner(UL)
        self.add(req)
        req2 = Circle()
        req2.to_corner(DR, buff=0)
        self.add(req2)