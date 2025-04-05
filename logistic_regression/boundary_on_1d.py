from manim import *

class StudentGradesBoundary(Scene):
    def construct(self):
        # Create number line
        line = NumberLine(
            x_range=[0, 100, 10],
            length=10,
            include_numbers=True,
            label_direction=UP,
        )
        line.to_edge(DOWN, buff=2)
        self.play(Create(line))

        # Add grade points
        grades = [20, 35, 50, 60, 75, 85, 90]
        dots = VGroup(*[Dot(color=BLUE).move_to(line.n2p(grade)) for grade in grades])
        labels = VGroup(*[
            Text(str(grade), font_size=20).next_to(dot, UP, buff=0.2)
            for dot, grade in zip(dots, grades)
        ])

        self.play(FadeIn(dots, shift=DOWN), Write(labels))

        # Add boundary
        boundary_line = Line(ORIGIN, UP * 1.5, color=RED, stroke_width=6)
        boundary_label = Text("Boundary", font_size=24, color=RED).next_to(boundary_line, UP, buff=0.2)
        
        boundary_line.move_to(line.n2p(50))
        boundary_label.next_to(boundary_line, UP)

        self.play(Create(boundary_line), Write(boundary_label))

        # Animate boundary movement
        for pos in [30, 70, 50]:
            self.play(
                boundary_line.animate.move_to(line.n2p(pos)),
                boundary_label.animate.next_to(boundary_line, UP)
            )
            self.wait(1)

        
