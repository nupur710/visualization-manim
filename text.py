from manim import *
class TextTest(Scene):
    def construct(self):
        text = Text("Hello, world!")
        self.play(Write(text))
        self.wait()

# manim -pql text.py TextTest
# manim - calls ManimCE library
# -pql - 
# preview opens video with default video software.
# quality indicates that the next command will define one of the resolutions that come by default in Manim
# low resolution indicates that the video will be rendered at 854x480 at 15 fps