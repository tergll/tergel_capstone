%%manim -qm EntropyFormulaScene

from manim import *

class EntropyFormulaScene(Scene):
    def construct(self):
       
        formula = MathTex(
            r"H = - \sum_{i=1}^{n} p_i \log_{2}(p_i)",
            font_size=60,
            color=WHITE
        )
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(2)
