from manim import *
class Animation(Scene):
    # def construct(self):
    #     text = Text('Animation class')
    #     self.add(text)
    #     self.play(
    #         Rotating(text, radians=360 * DEGREES),
    #         run_time=2.5,
    #         rate_funcs=smooth
    #     )

    def construct(self):
        text = Text('Method animation')
        self.add(text)
        self.play(text.animate.rotate(40*DEGREES),run_time=2)