from manim import *
class GridAnimation(Scene):
    def construct(self):
        n, m = 8, 7
        square_size= 1.0
        grid = VGroup()
        for i in range(n):
            for j in range(m):
                square = Square(side_length=1.0, stroke_width=2, stroke_color=WHITE)
                square.move_to([j*square_size - (m-1)*square_size/2, 
                              -i*square_size + (n-1)*square_size/2, 
                              0])
                grid.add(square)

        # grid_width = 51
        # self.camera.frame_width = grid_width + 2

        # self.camera.frame.set_width(vgrid.width+1)
        self.play(Write(grid), run_time=2)

        start_pt= grid[0].get_corner(UP+LEFT)
        text = Text("UL")
        text.move_to(start_pt)
        self.add(text)
        self.wait(1)

        

        