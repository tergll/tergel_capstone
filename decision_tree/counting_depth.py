%%manim -qm MaximumDepthScene

from manim import *

class MaximumDepthScene(Scene):
    def construct(self):
        # Шийдвэрийн модны гүнийг харуулах үндсэн зангилаа
        tree_root = Circle(radius=0.5, color=WHITE)
        tree_root.shift(UP * 2)
        
        # 1-р түвшний зангилаанууд
        l1_left = Circle(radius=0.5, color=WHITE)
        l1_left.shift(UP * 0.5 + LEFT * 2)
        l1_right = Circle(radius=0.5, color=WHITE)
        l1_right.shift(UP * 0.5 + RIGHT * 2)
        
        # 2-р түвшний зангилаанууд
        l2_ll = Circle(radius=0.5, color=WHITE)
        l2_ll.shift(DOWN * 1 + LEFT * 3)
        l2_lr = Circle(radius=0.5, color=WHITE)
        l2_lr.shift(DOWN * 1 + LEFT * 1)
        l2_rl = Circle(radius=0.5, color=WHITE)
        l2_rl.shift(DOWN * 1 + RIGHT * 1)
        l2_rr = Circle(radius=0.5, color=WHITE)
        l2_rr.shift(DOWN * 1 + RIGHT * 3)
        
        # 3-р түвшний зангилаанууд (хамгийн их гүнийг давсан)
        l3_lll = Circle(radius=0.5, color=RED, fill_opacity=0.3)
        l3_lll.shift(DOWN * 2.5 + LEFT * 3.5)
        l3_llr = Circle(radius=0.5, color=RED, fill_opacity=0.3)
        l3_llr.shift(DOWN * 2.5 + LEFT * 2.5)
        
        # Зангилаануудыг холбосон шугамууд
        edges = VGroup(
            Line(tree_root.get_bottom(), l1_left.get_top()),
            Line(tree_root.get_bottom(), l1_right.get_top()),
            Line(l1_left.get_bottom(), l2_ll.get_top()),
            Line(l1_left.get_bottom(), l2_lr.get_top()),
            Line(l1_right.get_bottom(), l2_rl.get_top()),
            Line(l1_right.get_bottom(), l2_rr.get_top()),
        )
        
        # 3-р түвшний болзошгүй холболтууд (улаан)
        potential_edges = VGroup(
            Line(l2_ll.get_bottom(), l3_lll.get_top(), color=RED),
            Line(l2_ll.get_bottom(), l3_llr.get_top(), color=RED),
        )
        
        # Гүний тайлбарууд
        depth_labels = VGroup(
            Text("Гүн 0", font_size=24).next_to(tree_root, RIGHT),
            Text("Гүн 1", font_size=24).next_to(l1_right, RIGHT),
            Text("Гүн 2", font_size=24).next_to(l2_rr, RIGHT),
            Text("Гүн 3 (Максимум)", font_size=24, color=RED).next_to(l3_llr, RIGHT),
        )
        
        # Модыг үе шаттайгаар зурж харуулах
        self.play(Create(tree_root), Create(edges[0:2]), FadeIn(depth_labels[0]))
        self.wait(1)
        
        self.play(
            Create(l1_left),
            Create(l1_right),
            FadeIn(depth_labels[1])
        )
        self.wait(1)
        
        self.play(
            Create(edges[2:]),
            Create(l2_ll),
            Create(l2_lr),
            Create(l2_rl),
            Create(l2_rr),
            FadeIn(depth_labels[2])
        )
        self.wait(1)
        
        self.play(
            Create(potential_edges),
            FadeIn(l3_lll),
            FadeIn(l3_llr),
            FadeIn(depth_labels[3])
        )
        self.wait(2)

