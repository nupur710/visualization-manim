from manim import *
class Animations(Scene):
    def construct(self):
        text = Text("Hello word")
        self.play(
            Write(text),
            # FadeIn(text),
            # GrowFromCenter(text),
            # FadeInFromLarge(text, scale_factor=2), # <- Some animations require more arguments to work.
        )
        self.wait() # <- It is advisable to always have a wait at the end