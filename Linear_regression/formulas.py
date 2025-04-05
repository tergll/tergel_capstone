%%manim -qm LinearRegressionComparisonScene
from manim import *

class LinearRegressionComparisonScene(Scene):
    def construct(self):
        # Create simple regression section
        simple_text = Text("Simple Linear Regression").scale(0.8)
        simple_formula = MathTex("y = b_0 + b_1 x").next_to(simple_text, DOWN)

        # Create multiple regression section
        multiple_text = Text("Multiple Linear Regression").scale(0.8)
        multiple_formula = MathTex("y = b_0 + b_1 x_1 + \\cdots + b_n x_i").next_to(multiple_text, DOWN)
        
        # Group and position elements
        simple_group = VGroup(simple_text, simple_formula)
        multiple_group = VGroup(multiple_text, multiple_formula)
        multiple_group.next_to(simple_group, DOWN, buff=1)
        full_group = VGroup(simple_group, multiple_group).move_to(ORIGIN)
        
        # Animate the texts and formulas together
        self.play(Write(simple_group))
        self.play(Write(multiple_group))
        self.wait(2)

