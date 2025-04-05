%%manim -qm MinimumSamplesTreeScene
class MinimumSamplesTreeScene(Scene):
    def construct(self):
        # Create root node
        tree_root = Circle(radius=0.6, color=WHITE)
        tree_root.shift(UP * 2.5)
        
        # Create level 1 nodes
        l1_left = Circle(radius=0.6, color=WHITE)
        l1_left.shift(UP * 1 + LEFT * 2)
        l1_right = Circle(radius=0.6, color=WHITE)
        l1_right.shift(UP * 1 + RIGHT * 2)
        
        # Create level 2 nodes
        l2_ll = Circle(radius=0.6, color=RED, stroke_width=3)
        l2_ll.shift(DOWN * 0.5 + LEFT * 3)
        l2_lr = Circle(radius=0.6, color=RED, stroke_width=3)
        l2_lr.shift(DOWN * 0.5 + LEFT * 1)
        
        # Add connections
        edges = VGroup(
            Line(tree_root.get_bottom(), l1_left.get_top()),
            Line(tree_root.get_bottom(), l1_right.get_top()),
            Line(l1_left.get_bottom(), l2_ll.get_top()),
            Line(l1_left.get_bottom(), l2_lr.get_top()),
        )
        
        # Add data points to nodes
        l2_ll_data = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3
            radius = 0.3
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point=l2_ll.get_center() + pos, color=BLUE, radius=0.05)
            l2_ll_data.add(dot)
            
        l2_lr_data = VGroup()
        for i in range(2):
            angle = i * PI
            radius = 0.3
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot = Dot(point=l2_lr.get_center() + pos, color=BLUE, radius=0.05)
            l2_lr_data.add(dot)
        
        # Animate tree structure
        self.play(Create(tree_root))
        self.wait(0.5)
        
        self.play(Create(edges[0:2]))
        self.play(
            Create(l1_left),
            Create(l1_right),
        )
        self.wait(0.5)
        
        self.play(Create(edges[2:]))
        self.play(
            Create(l2_ll),
            Create(l2_lr),
        )
        self.wait(0.5)
        
        # Add data points
        self.play(
            FadeIn(l2_ll_data),
            FadeIn(l2_lr_data),
        )
        self.wait(1)
        
        # Add sample counters
        l2_ll_counter = Integer(0).next_to(l2_ll, UP * 0.2)
        l2_ll_counter.scale(0.6)
        l2_lr_counter = Integer(0).next_to(l2_lr, UP * 0.2)
        l2_lr_counter.scale(0.6)
        
        self.play(
            FadeIn(l2_ll_counter),
            FadeIn(l2_lr_counter)
        )
        
        # Animate counters
        for i in range(1, 4):
            self.play(l2_ll_counter.animate.set_value(i), run_time=0.3)
        
        for i in range(1, 3):
            self.play(l2_lr_counter.animate.set_value(i), run_time=0.3)
        
        self.wait(0.5)
        self.wait(2)