from manim import *
class NextTo(Scene):
    def construct(self):
        rm = Rectangle()
        red_dot = Dot(color=RED)
        blue_dot = Dot(color=BLUE)
        green_dot = Dot(color=GREEN)
        t = Text("Text")
        red_dot.next_to(rm,LEFT)
        blue_dot.next_to(rm, DR, buff=0)
        green_dot.next_to(blue_dot, LEFT, buff =1)
        t.next_to(rm, DOWN, aligned_edge=LEFT)
        self.add(rm,red_dot, blue_dot, green_dot,t)

    # def construct(self):
    #     side_len= 0.5
    #     s1= Square(side_length=side_len)
    #     s2 = Square(side_length=side_len)
    #     s2.next_to(s1, RIGHT, buff=0)
    #     s3 = Square(side_length=side_len)
    #     s3.next_to(s2, RIGHT, buff=0)
    #     s4 = Square(side_length=side_len)
    #     s4.next_to(s3, RIGHT, buff=0)
    #     s5 = Square(side_length=side_len)
    #     s5.next_to(s1, DOWN, buff=0)
    #     self.add(s1,s2,s3,s4,s5)