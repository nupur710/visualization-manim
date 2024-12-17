from manim import *
class MA(Scene):
    def construct(self):
        text = Text('Hello World')
        self.play(Write(text))
        self.wait()
        self.play(Rotate(text, PI/2))
        self.wait()
        self.play(Indicate(text))
        self.wait()
        self.play(FocusOn(text))
        self.wait()
        self.play(FadeOut(text))
        self.wait()