from manim import *

class Grid(Scene):
    def construct(self):
        vgrid = VGroup()
        sq = Square(side_length=1)
        vgrid.add(sq)
        for i in range(3):
            square = Square(side_length=1)
            square.next_to(sq, LEFT, buff=0)
            vgrid.add(square)
            sq = square
        
        vgrid.center()
        # grid_width = 51
        # self.camera.frame_width = grid_width + 2

        # self.camera.frame.set_width(vgrid.width+1)
        self.add(vgrid)
    
