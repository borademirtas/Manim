from manim import *
from manim_data_structures import * 



class A(Scene):


    def construct(self):

        scoretxt = Text("3:5", color = GOLD)
        box = SurroundingRectangle(scoretxt, color=BLUE, buff=0.5)
        score1 = VGroup(scoretxt, box)

        scoretxt2 = Text("4:7", color = GOLD)
        box2 = SurroundingRectangle(scoretxt2, color=BLUE, buff=0.5)
        score2 = VGroup(scoretxt2, box2)

        steps = MathTex("3:5 \Rightarrow 3:6 \Rightarrow 4:6 \Rightarrow 4:7")


        self.play(Create(score1))
        self.play(score1.animate.shift(UP*2))
        score2.shift(DOWN*2)
        self.play(Create(score2))
        self.wait(25)
        self.play(Create(steps))
        self.wait(5)

        scoretxt3 = Text("3:5", color = "#D74D4D")
        scoretxt3.shift(UP*2)
        scoretxt4 = Text("6:5", color = "#D74D4D")
        scoretxt4.shift(DOWN*2)
        self.play(FadeOut(steps), Transform(scoretxt, scoretxt3), Transform(scoretxt2, scoretxt4))
        self.wait(9)

        claim = Text("Claim: The game has to have a tie if the winning team changes", color = GOLD,font_size=36)
        question = Text("Why is it possible for the game to not have a tie if the lead never changes?",color = GOLD,font_size=30 )

        self.play(Write(claim))
        self.wait(9)
        self.play(Transform(claim,question))
        self.wait(9)

        scoretxt4 = Text("4:3", color = GOLD)
        scoretxt4.shift(UP*2)
        scoretxt5 = Text("7:5", color = GOLD)
        scoretxt5.shift(DOWN*2)
        steps2 = MathTex("4:3 \Rightarrow 5:3 \Rightarrow 6:3 \Rightarrow 7:3 \Rightarrow 7:4 \Rightarrow 7:5")
        self.play(FadeOut(claim), Transform(scoretxt, scoretxt4), Transform(scoretxt2, scoretxt5))
        self.wait(1)
        self.play(Create(steps2))
        self.wait(20)
        self.play(FadeOut(steps2), FadeOut(score1), FadeOut(score2))
        self.wait(0.5)

        cpp_code = """
        int x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
    
        if(x1 > y1 && x2 > y2){cout << "YES" << endl;}
        else if(x1 < y1 && x2 < y2){cout << "YES" << endl;}
        else{cout << "NO" << endl;}
        """

        code = Code(
            code=cpp_code,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code.move_to(ORIGIN)
        self.play(FadeIn(code))
        self.wait(15)
        self.play(FadeOut(code))
