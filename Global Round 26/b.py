from manim import *
from manim_data_structures import * 

class B(Scene):
    def construct(self):
        
        green_string = Text("5  6  7  8  9", color=GREEN, font_size = 60)
        red_string = Text("0  1  2  3  4", color=RED, font_size = 60)

        
        green_rect = SurroundingRectangle(green_string, color=GREEN, buff=0.5)
        red_rect = SurroundingRectangle(red_string, color=RED, buff=0.5)

       
        green_label = Text("large digit", color=GREEN, font_size=40)
        red_label = Text("not large digit", color=RED, font_size=40)
        
        green_label.center().move_to(DOWN*1.3)
        red_label.center().move_to(DOWN*1.3)
       
        green_group = VGroup(green_string, green_rect, green_label)
        red_group = VGroup(red_string, red_rect, red_label)

        green_group.center().move_to(RIGHT * 3)
        red_group.center().move_to(LEFT * 3)
        
        self.play(Write(green_group))
        self.play(Write(red_group))

        
        self.wait(10)
        self.play(FadeOut(green_group), FadeOut(red_group))

        good1 = Text("5675", color=GREEN,font_size = 75)
        good2 = Text("99999", color=GREEN,font_size = 75)
        bad1 = Text("120304", color=RED,font_size = 75)
        bad2 = MathTex("5","6","7","4","5",font_size = 100)

        bad2.set_color(GREEN)
        bad2[3].set_color(RED)

        examples = VGroup(good1, good2, bad1, bad2).arrange(DOWN, buff=0.5)

        self.play(Create(good1))
        self.play(Create(good2))
        self.wait(3)
        self.play(Create(bad1))
        self.wait(3)
        self.play(Create(bad2))
        self.wait(5)
        self.play(FadeOut(examples))
        
        problem1 = Text("You are given an integer x.", font_size = 30)
        problem2 = Text("Can it be the sum of two large integers with the same number of digits?", font_size=30)

        
        problem = VGroup(problem1, problem2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(Write(problem))
        self.wait(5)
        self.play(problem.animate.shift(UP*2))
        ok = Text("135 = 67 + 68", color = GREEN)
        self.play(Write(ok))
        self.wait(2)
        not_ok = Text("233 = NO SOLUTION", color=RED)
        not_ok.move_to(DOWN)
        self.play(Write(not_ok))
        self.wait(2)
        self.play(FadeOut(not_ok),FadeOut(ok), FadeOut(problem))
        

        hint1 = Text("Hint 1: Try to look at what happens when we add two large digits", font_size=30)
        hint1.move_to(UP*2.5)
        self.play(Write(hint1))
        self.wait(2)
        add1 = Text("5 + 5 = 10")
        add2 = Text("9 + 9 = 18")
        adders = VGroup(add1, add2).arrange(DOWN, buff=1).move_to(ORIGIN)
        self.play(Write(adders))
        self.wait(2)
        self.play(FadeOut(hint1), FadeOut(adders))
        
        hint2 = Text("Hint 2: Think about how carrying digits affects the problem", font_size=30)
        hint2.move_to(UP*2.5)
        self.play(Write(hint2))

        val1 = Text("597")
        val2 = Text("998")
        val3 = MathTex("1","5","9","5", font_size=75, )
        vals = VGroup(val1, val2).arrange(DOWN*0.2, buff=1).move_to(ORIGIN)
        
        line = Line(LEFT, RIGHT*0.1).scale(2)  
        line.next_to(vals, DOWN, buff=0.1)  
        line.shift(LEFT*0.2)
        
        plus_sign = Text("+")
        plus_sign.next_to(line, UP, buff=0.1)
        plus_sign.shift(LEFT)
        add = VGroup(vals, line, plus_sign)
        val3.next_to(line, DOWN, buff=0.1)
        
        self.play(Create(add))
        self.play(Create(val3[3]))
        self.wait(1)
        self.play(Create(val3[2]))
        self.wait(1)
        self.play(Create(val3[1]))
        self.wait(1)
        self.play(Create(val3[0]))
        self.wait(2)
        self.play(FadeOut(add), FadeOut(val3), FadeOut(hint2))
        
        claim1top = Text("Claim 1:", font_size = 36)
        claim1bottom = Text("The last digit cannot be nine.", font_size = 36)
        claim1 = VGroup(claim1top, claim1bottom).arrange(DOWN*0.2, buff=1).move_to(ORIGIN)
        claim1.shift(UP*2)
        self.play(Create(claim1))
        self.wait(2)

        claim2top = Text("Claim 2:", font_size = 36)
        claim2bottom = Text("The first digit is always one.", font_size = 36)
        claim2 = VGroup(claim2top, claim2bottom).arrange(DOWN*0.2, buff=1).move_to(ORIGIN)
        self.play(Create(claim2))
        self.wait(2)

        claim3top = Text("Claim 3:", font_size = 36)
        claim3bottom = Text("The middle digits cannot be zero.", font_size = 36)
        claim3 = VGroup(claim3top, claim3bottom).arrange(DOWN*0.2, buff=1).move_to(ORIGIN)
        claim3.shift(DOWN*2)
        self.play(Create(claim3))
        self.wait(2)
        

        cpp_code = """
            string s;
            cin >> s;
            bool ok = true;
            if(s[0]=='1'){
             ok=false;
            }
            if(s.back()=='9'){
                ok=false;
            }
            for(int i = 1; i < s.size()-1; i++){
                if(s[i]=='0'){
                    ok=false;
                }
            }
            if(ok==true){
                cout << "YES";
            }
            else{
            cout << "NO";
            }
        """

        code = Code(
            code=cpp_code,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        ).scale(0.8)

        code.move_to(ORIGIN)
        self.play(FadeIn(code))
        self.wait(2)
