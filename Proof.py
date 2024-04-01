from manim import *

class Proof(Scene):
    
    def replay(self, arrow):
        self.play(FadeOut(arrow))
        self.play(Create(arrow))

    def construct(self):
        
        flip = VGroup(
            Circle(stroke_color=WHITE, stroke_width=8, fill_color=BLACK, fill_opacity=1),
            Text("Roll Again", font_size=30, color = WHITE)
        )
        flip.move_to(LEFT*2.5)

        win = VGroup(
            Circle(stroke_color=WHITE, stroke_width=8, fill_color=BLACK, fill_opacity=1),
            Text("End Game", font_size=30, color = WHITE)
        )
        win.move_to(RIGHT*2.5)

        uptxt = MathTex(r"1-p", color = YELLOW)
        uptxt.next_to(flip, UP), uptxt.shift(LEFT*1.2)



        self.play(GrowFromCenter(flip), GrowFromCenter(win))
        arrow_down = CurvedArrow(flip.get_bottom()+DOWN*0.1, win.get_bottom(), color = "#40E0D0",stroke_width=10)
        arrow_up =  ArcBetweenPoints(flip.get_top()+RIGHT*0.1, flip.get_top()+UP+LEFT*0.05, stroke_color="#40E0D0", angle = PI/2,stroke_width=10) 
        arrow_up2 =  CurvedArrow(flip.get_top()+UP, flip.get_top()+LEFT*0.1, stroke_color="#40E0D0", angle = PI/2,stroke_width=10)  

        downtxt = MathTex(r"\frac{1}{p}", color = YELLOW)
        downtxt.next_to(arrow_down, DOWN)

        arrows_up = VGroup(arrow_up, arrow_up2, uptxt)
        arrows_down = VGroup(arrow_down, downtxt)

        
       

        self.play(Create(arrows_up), Create(arrows_down))
        self.wait(3)

        

        equation = MathTex(r"E[x] =  ", "p" ," + ", "(1-p)" , "(1+E[x])")
        equation[1].set_color(RED)
        equation[3].set_color(YELLOW)
        equation[4].set_color(BLUE)
        equation_2 = MathTex(r'E[x] =  p +  1 - p  + E[x] - pE[x]')
        equation_3 = MathTex(r'E[x] =  1  + E[x] - pE[x]')
        equation_4 = MathTex(r'E[x] + pE[x] =  1  + E[x]')
        equation_5 = MathTex(r'E[x] + pE[x] =  1  + E[x]')
        equation_6 = MathTex(r'pE[x] =  1')
        equation_7 = MathTex(r'E[x] = \frac{1}{p}')
        equation_8 = MathTex(r'E[x] = \frac{1}{p} = \sum_{n=1}^{\infty} (1-p)^{n-1} \times p \times x')

        equation.shift(UP*3)
        equation_2.shift(UP*3)
        equation_3.shift(UP*3)
        equation_4.shift(UP*3)
        equation_5.shift(UP*3)
        equation_6.shift(UP*3)
        equation_7.shift(UP*3)
        self.wait(10)
        self.play(Create(equation))
        self.wait(17)
        self.play(Transform(equation, equation_2, run_time = 3))
        self.play(Transform(equation,equation_3,run_time = 3))
        self.play(Transform(equation, equation_4,run_time = 3))
        self.play(Transform(equation, equation_5,run_time = 3))
        self.play(Transform(equation, equation_6,run_time = 3))
        self.play(Transform(equation, equation_7,run_time = 3))
        self.play(FadeOut(flip), FadeOut(win), FadeOut(arrows_up), FadeOut(arrows_down), FadeOut(uptxt), FadeOut(downtxt))
        self.play(equation.animate.scale(3).move_to(ORIGIN))
        self.play(Circumscribe(equation, color = DARK_BLUE, stroke_width = 10))
        self.wait(1)
        self.play(Transform(equation, equation_8))
        self.wait(10)
        self.play(FadeOut(equation))

        

        