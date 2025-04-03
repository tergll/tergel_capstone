%%manim -qm DecisionTreeFood
from manim import *

class DecisionTreeFood(Scene):
    def construct(self):
        # Initial question node - positioned higher
        initial_q = Text("Өлсөж байна уу?", color=BLUE, font_size=32)
        initial_q.to_edge(UP, buff=1)

        # Second level questions
        second_level_y = initial_q.get_center()[1] - 2
        healthy_q = Text("Эрүүл хоол уу?", color=BLUE, font_size=28)
        healthy_q.move_to(LEFT * 3 + UP * second_level_y)

        not_hungry_text = Text("Хоол алгасах", color=RED, font_size=28)
        not_hungry_text.move_to(RIGHT * 3 + UP * second_level_y)

        # Third level
        third_level_y = second_level_y - 2
        meat_q = Text("Махтай хоол уу?", color=BLUE, font_size=24)
        meat_q.move_to(LEFT * 4 + UP * third_level_y)

        not_healthy_text = Text("Пицца захиалах", color=RED, font_size=24)
        not_healthy_text.move_to(RIGHT * 0.5 + UP * third_level_y)

        # Fourth level (Final decisions)
        fourth_level_y = third_level_y - 2
        meat_dish_text = Text("Махтай хоол", color=GREEN, font_size=20)
        meat_dish_text.move_to(LEFT * 5 + UP * fourth_level_y)  # YES branch → left

        salad_text = Text("Салат хийх", color=GREEN, font_size=20)
        salad_text.move_to(LEFT * 3 + UP * fourth_level_y)      # NO branch → right

        # Decision labels
        midpoint_y1 = (initial_q.get_center()[1] + healthy_q.get_center()[1]) / 2
        yes_1 = Text("Тийм", color=GREEN, font_size=20).move_to(LEFT * 1.5 + UP * midpoint_y1)
        no_1 = Text("Үгүй", color=RED, font_size=20).move_to(RIGHT * 1.5 + UP * midpoint_y1)

        midpoint_y2 = (healthy_q.get_center()[1] + meat_q.get_center()[1]) / 2
        yes_2 = Text("Тийм", color=GREEN, font_size=20).move_to(LEFT * 3.5 + UP * midpoint_y2)
        no_2 = Text("Үгүй", color=RED, font_size=20).move_to(RIGHT * 1.5 + UP * midpoint_y2)

        midpoint_y3 = (meat_q.get_center()[1] + meat_dish_text.get_center()[1]) / 2
        yes_3 = Text("Тийм", color=GREEN, font_size=20).move_to(LEFT * 5.5 + UP * midpoint_y3)
        no_3 = Text("Үгүй", color=RED, font_size=20).move_to(LEFT * 3.5 + UP * midpoint_y3)

        # Lines between nodes
        line_1_yes = Line(initial_q.get_bottom(), healthy_q.get_top(), buff=0.3)
        line_1_no = Line(initial_q.get_bottom(), not_hungry_text.get_top(), buff=0.3)

        line_2_yes = Line(healthy_q.get_bottom(), meat_q.get_top(), buff=0.3)
        line_2_no = Line(healthy_q.get_bottom(), not_healthy_text.get_top(), buff=0.3)

        line_3_yes = Line(meat_q.get_bottom(), meat_dish_text.get_top(), buff=0.3)
        line_3_no = Line(meat_q.get_bottom(), salad_text.get_top(), buff=0.3)

        # Animation
        self.play(Write(initial_q), run_time=1.5)
        self.wait(1)

        # First branching
        self.play(Create(line_1_yes), Create(line_1_no), FadeIn(yes_1), FadeIn(no_1))
        self.play(Write(healthy_q), Write(not_hungry_text))
        self.wait(1)

        # Second branching
        self.play(Create(line_2_yes), Create(line_2_no), FadeIn(yes_2), FadeIn(no_2))
        self.play(Write(meat_q), Write(not_healthy_text))
        self.wait(1)

        # Third branching
        self.play(Create(line_3_yes), Create(line_3_no), FadeIn(yes_3), FadeIn(no_3))
        self.play(Write(meat_dish_text), Write(salad_text))
        self.wait(1)

        # Highlight tree
        decision_tree = VGroup(
            initial_q, healthy_q, not_hungry_text,
            meat_q, not_healthy_text,
            salad_text, meat_dish_text,
            yes_1, no_1, yes_2, no_2, yes_3, no_3,
            line_1_yes, line_1_no,
            line_2_yes, line_2_no,
            line_3_yes, line_3_no
        )

        self.play(decision_tree.animate.set_color(YELLOW).set_opacity(0.8), run_time=1.5)
        self.play(decision_tree.animate.set_color(WHITE).set_opacity(1), run_time=1.5)
        self.wait(2)
