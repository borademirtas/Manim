from manim import *
from manim_data_structures import * 



class B(Scene):


    def construct(self):

        vars = Text("x = 13, y = 3, k = 5", color = GOLD)
        box = SurroundingRectangle(vars, color=BLUE, buff=0.5)
        var = VGroup(vars,box)

        self.play(Create(var))
        self.wait(10)
        self.play(var.animate.shift(DOWN*3))

        instructions = Text("1. Increase x by 1\n2. While the number x is divisible by y,\n divide it by y")
        self.play(Create(instructions)) 
        self.wait(8)
        self.play(FadeOut(instructions))

        step1 = MathTex("13")
        step2 = MathTex("13 \Rightarrow 14")
        step3 = MathTex("13 \Rightarrow 14 \Rightarrow 15 \Rightarrow 5")
        step4 = MathTex("13 \Rightarrow 14 \Rightarrow 15 \Rightarrow 5 \Rightarrow 6 \Rightarrow 2")
        step5 = MathTex("13 \Rightarrow 14 \Rightarrow 15 \Rightarrow 5 \Rightarrow 6 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1")
        step6 = MathTex("13 \Rightarrow 14 \Rightarrow 15 \Rightarrow 5 \Rightarrow 6 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1 \Rightarrow 2")

        self.play(Create(step1))
        self.wait(2)
        self.play(Transform(step1,step2))
        self.wait(5)
        self.play(Transform(step1,step3))
        self.wait(5)
        self.play(Transform(step1,step4))
        self.wait(5)
        self.play(Transform(step1,step5))
        self.wait(5)
        self.play(Transform(step1,step6))
        self.wait(8)
        self.play(FadeOut(var), FadeOut(step1))


        hint1 = Text("Hint 1: when do we do the division operation?")
        self.play(Create(hint1))
        self.play(hint1.animate.shift(UP*2))
        self.wait(5)

        vars = Text("x = 13, y = 19", color = GOLD)
        box = SurroundingRectangle(vars, color=BLUE, buff=0.5)
        var = VGroup(vars,box)
        var.shift(DOWN*3)
        self.play(Create(var))
        self.wait(2)

        show = MathTex("13 \Rightarrow 14 \Rightarrow 15 \Rightarrow 16 \Rightarrow 17 \Rightarrow 18 \Rightarrow 19 \Rightarrow 1")
        self.play(Create(show))
        self.wait(6)

        hint2 = Text("Hint 2: We don't need many division operations to each one", font_size=36)  
        hint2.shift(UP*2)      
        self.play(Transform(hint1, hint2))
        self.wait(4)

        hint3 = Text("Hint 3: Look at what happens when we reach one", font_size=36)  
        hint3.shift(UP*2)   
        self.play(Transform(hint1, hint3))
        self.wait(3)

        vars2 = Text("x = 1, y = 4", color = GOLD)
        box2 = SurroundingRectangle(vars2, color=BLUE, buff=0.5)
        var2 = VGroup(vars2,box2)
        var2.shift(DOWN*3)
        show2 = MathTex("1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1 \Rightarrow 2 \Rightarrow 3")
        self.play(Transform(var,var2))
        self.wait(1)
        self.play(Transform(show,show2))
        self.wait(10)
        self.play(FadeOut(var), FadeOut(hint1), FadeOut(show))

        cpp_code = """
        int x,y,k; cin >> x >> y >> k;
 
        while(x != 1){
            int dif = (y - x%y);
            if(dif<=k){k -= dif; x += dif;}
            else{
            cout << x + k << endl; return;
            }
            while(x%y==0){x/=y;}
        }
 
        cout << k%(y-1)+1 << endl;
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
        self.wait(20)
        self.play(FadeOut(code))