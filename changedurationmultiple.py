from manim import *
class CDM(Scene):
        def construct(self):
            self.play(Create(Square(), run_time=2, rate_func=smooth), FadeIn(Circle(), run_time=2, rate_func=linear))
            self.wait()