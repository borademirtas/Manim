from manim import *

class DiceTree(Scene):
    
    def construct(self):
        
        
        vertices = {
            "1": UP * 2,
            "2": UP + LEFT,
            "3": LEFT * 2,
            "4": LEFT * 3 + DOWN,
            r"\$1": UP + RIGHT,
            r"\$2": LEFT-LEFT,
            r"\$3": LEFT + DOWN,
            r"\$4": LEFT*2 + DOWN*2
        }

        edges = [
            ("1", "2"), ("1", r"\$1"),
            ("2", "3"), ("2", r"\$2"),
            ("3", "4"), ("3", r"\$3"),
            ("4", r"\$4")
        ]

        graph = Graph(list(vertices.keys()), edges, layout=vertices, labels=True, label_fill_color = BLACK)
        graph.scale(1.5)
        graph.center()
        graph.shift(RIGHT*2.5)

        text = MathTex(r"P(\$1) = \frac{1}{6}", 
               r"\\ \approx 0.166")
        text2 = MathTex(r"E(\$1) = \frac{1}{6} \times \times 1", 
               r"\\ \approx 0.166")
        text.to_edge(UP+LEFT, buff = 1)
        text2.next_to(text, DOWN)

        self.play(Create(graph), run_time = 5)

        self.play(Create(text), Create(text2))
        self.play(
        Circumscribe(graph["1"], time_width =5, run_time = 5 ), 
        Circumscribe(graph[r"\$1"], time_width = 5, run_time = 5)
        )
        self.play(FadeOut(text), FadeOut(text2))

        text = MathTex(r"P(\$2) = \frac{1}{6} \times \left(\frac{5}{6}\right)", 
               r"\\ = \frac{5}{36}", 
               r"\\ \approx 0.138")
        text2 = MathTex(r"E(\$2) = \frac{1}{6} \times \left(\frac{5}{6}\right) \times 2", 
               r"\\ = \frac{5}{18}", 
               r"\\ \approx 0.277")
        text.to_edge(UP+LEFT, buff = 1)
        text2.next_to(text, DOWN)

        self.play(Create(text), Create(text2))
        self.play(
        Circumscribe(graph["2"], time_width =5, run_time = 5 ), 
        Circumscribe(graph[r"\$2"], time_width = 5, run_time = 5)
        )
        self.play(FadeOut(text), FadeOut(text2))

        text = MathTex(r"P(\$3) = \frac{1}{6} \times \left(\frac{5}{6}\right)^{2}", 
               r"\\ = \frac{25}{216}", 
               r"\\ \approx 0.115")
        text2 = MathTex(r"E(\$3) = \frac{1}{6} \times \left(\frac{5}{6}\right)^{2} \times 3", 
               r"\\ = \frac{25}{72}", 
               r"\\ \approx 0.347")
        text.to_edge(UP+LEFT, buff = 1)
        text2.next_to(text, DOWN)

        self.play(Create(text), Create(text2))
        self.play(
        Circumscribe(graph["3"], time_width =5, run_time = 5 ), 
        Circumscribe(graph[r"\$3"], time_width = 5, run_time = 5)
        )
        self.play(FadeOut(text), FadeOut(text2))


        text = MathTex(r"P(\$4) = \frac{1}{6} \times \left(\frac{5}{6}\right)^{3}", 
               r"\\ = \frac{125}{1296}", 
               r"\\ \approx 0.096")
        text2 = MathTex(r"E(\$4) = \frac{1}{6} \times \left(\frac{5}{6}\right)^{3} \times 4", 
               r"\\ = \frac{125}{324}", 
               r"\\ \approx 0.385")
        text.to_edge(UP+LEFT, buff = 1)
        text2.next_to(text, DOWN)

        self.play(Create(text), Create(text2))
        self.play(
        Circumscribe(graph["4"], time_width =5, run_time = 5 ), 
        Circumscribe(graph[r"\$4"], time_width = 5, run_time = 5)
        )
        self.play(FadeOut(text), FadeOut(text2))

        self.play(FadeOut(graph))
        text = MathTex(r"P(x) = (\frac{5}{6})^{\# \text{ of left moves}} \times (\frac{1}{6})^{\# \text{ of right moves}}")
        text2 = MathTex(r"E(x) = (\frac{5}{6})^{\# \text{ of left moves}} \times (\frac{1}{6})^{\# \text{ of right moves}} \times x")
        text.center()
        text.shift(UP*0.25)
        text2.next_to(text, DOWN)
        self.play(Create(text, run_time = 5))
        self.wait(2)
        self.play(Create(text2, run_time = 5))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        text = MathTex(r"P(x) = (\frac{5}{6})^{x-1} \times \frac{1}{6}")
        text2 = MathTex(r"E(x) = (\frac{5}{6})^{x-1} \times \frac{1}{6} \times x")
        text.center()
        text.shift(UP*0.25)
        text2.next_to(text, DOWN)
        self.play(Create(text, run_time = 5))
        self.wait(2)
        self.play(Create(text2, run_time = 5))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text2))
        text = MathTex(r"E(x) = \sum_{n=1}^{\infty} \left(\frac{5}{6}\right)^{n-1} \times \frac{1}{6} \times n")
        text2 = MathTex(r"E(x) = \sum_{n=1}^{\infty} (1-p)^{n-1} \times p \times n")
        text.shift(UP*0.7)
        text2.next_to(text, DOWN*0.7)
        self.play(Create(text,run_time = 5))
        self.play(Create(text2,run_time = 5))
        self.wait(5)

        
