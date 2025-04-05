%%manim -qm LogisticRegressionAssumption
from manim import *

class LogisticRegressionAssumption(Scene):
    def construct(self):
        # Create logistic curve
        logistic_curve = FunctionGraph(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=GREEN,
        )
        logistic_label = Text("Logistic Curve", font_size=24, color=GREEN)
        logistic_label.next_to(logistic_curve, UP, buff=0.5)

        # Create linear relationship
        log_odds_line = FunctionGraph(
            lambda x: x,
            x_range=[-6, 6],
            color=ORANGE,
        )
        log_odds_label = Text("Linear Log-Odds", font_size=24, color=ORANGE)
        log_odds_label.next_to(log_odds_line, UP, buff=0.5)

        # Setup first axes
        axes_logistic = Axes(
            x_range=[-6, 6, 2],
            y_range=[0, 1, 0.2],
            axis_config={"include_tip": True},
        ).add_coordinates()
        logistic_axes_labels = axes_logistic.get_axis_labels(
            x_label="x",
            y_label="P(y=1)"
        )

        # Setup second axes
        axes_log_odds = Axes(
            x_range=[-6, 6, 2],
            y_range=[-6, 6, 2],
            axis_config={"include_tip": True},
        ).add_coordinates()
        log_odds_axes_labels = axes_log_odds.get_axis_labels(
            x_label="x",
            y_label="log(p/(1-p))"
        )

        # Animate transitions
        self.play(Create(axes_logistic), Write(logistic_axes_labels))
        self.play(Create(logistic_curve), Write(logistic_label))
        self.wait(2)

        self.play(
            Transform(axes_logistic, axes_log_odds),
            Transform(logistic_curve, log_odds_line),
            Transform(logistic_label, log_odds_label),
            Transform(logistic_axes_labels, log_odds_axes_labels),
        )
        self.wait(2)

        self.play(
            FadeOut(axes_log_odds),
            FadeOut(log_odds_line),
            FadeOut(log_odds_label),
            FadeOut(axes_logistic),
            FadeOut(logistic_curve),
            FadeOut(logistic_label),
            FadeOut(logistic_axes_labels),
        )
        self.wait(1)
