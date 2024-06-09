from manim import *
from manim_data_structures import * 

class C(Scene):
    def construct(self):
         arr = MArray(
            self,
            arr = [2,-5,2,-3,4],
            hide_index=True,
        )
         arr.center()
         self.play(Create(arr))
         
         operation1 = MathTex(r"Option\ 1: set\ c\ to\ c + a_i", font_size = 60)
         operation2 = MathTex(r"Option\ 2: set\ c\ to\ |c + a_i|", font_size = 60)

         operation1.shift(UP)
         label = Text("c = 0 ", color=WHITE).center().shift(DOWN*3)
         

         self.play(Write(label))
         self.play(arr.animate.shift(DOWN*1.5))
         self.play(Write(operation1))
         self.play(Write(operation2))
         pointer = MArrayPointer(self, arr, 0, '')
         self.play(Create(pointer))


         label2 = Text("c = 0 + 2", color=YELLOW).center().shift(DOWN*3)
         label3 = Text("c = |0 + 2|", color=YELLOW).center().shift(DOWN*3)
         self.play(Transform(label,label2))
         self.wait(2)
         self.play(Transform(label,label3))
         self.wait(2)
         label4 = Text("c = 2", color=WHITE).center().shift(DOWN*3)
         self.play(Transform(label,label4))
         pointer.shift_to_elem(1)
         label5 = Text("c = 2 - 5", color=YELLOW).center().shift(DOWN*3)
         label6 = Text("c = |2-5|", color=YELLOW).center().shift(DOWN*3)
         self.play(Transform(label,label5))
         self.wait(2)
         self.play(Transform(label,label6))
         self.wait(2)
         label7 = Text("c = -3", color=WHITE).center().shift(DOWN*3)
         self.play(Transform(label,label7))
         pointer.shift_to_elem(2)
         label8 = Text("c = -3+2", color=YELLOW).center().shift(DOWN*3)
         label9 = Text("c = -1", color=WHITE).center().shift(DOWN*3)
         self.play(Transform(label,label8))
         self.play(Transform(label,label9))
         pointer.shift_to_elem(3)
         label10 = Text("c = |-1-3|", color=YELLOW).center().shift(DOWN*3)
         label11 = Text("c = 4", color=WHITE).center().shift(DOWN*3)
         self.play(Transform(label,label10))
         self.play(Transform(label,label11))
         pointer.shift_to_elem(4)
         label12 = Text("c = 4+4", color=YELLOW).center().shift(DOWN*3)
         label13 = Text("c = 8", color=WHITE).center().shift(DOWN*3)
         self.play(Transform(label,label12))
         self.play(Transform(label,label13))
         self.wait(1)
         self.play(FadeOut(operation1), FadeOut(operation2), FadeOut(pointer))
         question = Text("What is the maximum value of c we can obtain after all operations?", font_size=30)
         question.shift(UP)
         self.play(Write(question))
         self.wait(1)
         self.play(FadeOut(question), FadeOut(label))
         
         hint1 = Text("Hint 1: When should we choose option 2?")
         hint1.shift(UP)
         self.play(Write(hint1))
         claim = Text("Claim: Choose option 2 at prefix minimum", font_size=42)
         claim.shift(UP)
         self.play(Transform(hint1,claim))
         self.play(FadeOut(hint1))
         self.play(arr.animate.shift(UP*1.5))
         pointer2 = MArrayPointer(self, arr, 1, '')
         self.play(Create(pointer2))
         label = Text("c = |2-5|")
         label.shift(DOWN*2)
         self.play(Write(label))
         label14 = Text("c=3")
         label14.shift(DOWN*2)
         self.play(Transform(label,label14))
         pointer2.shift_to_elem(2)
         label15 = Text("c=3+2")
         label15.shift(DOWN*2)
         label16 = Text("c=5")
         label16.shift(DOWN*2)
         label17 = Text("c=5-3")
         label17.shift(DOWN*2)
         label18 = Text("c=2")
         label18.shift(DOWN*2)
         self.play(Transform(label,label15))
         self.play(Transform(label,label16))
         pointer2.shift_to_elem(3)
         self.play(Transform(label,label17))
         self.play(Transform(label,label18))

         pointer2.shift_to_elem(1)
         self.play(FadeOut(label))

         label = Text("c = 2-5")
         label.shift(DOWN*2)
         self.play(Write(label))
         label14 = Text("c=-3")
         label14.shift(DOWN*2)
         self.play(Transform(label,label14))
         pointer2.shift_to_elem(2)
         label15 = Text("c=-3+2")
         label15.shift(DOWN*2)
         label16 = Text("c=-1")
         label16.shift(DOWN*2)
         label17 = Text("c=|-1-3|")
         label17.shift(DOWN*2)
         label18 = Text("c=4")
         label18.shift(DOWN*2)
         self.play(Transform(label,label15))
         self.play(Transform(label,label16))
         pointer2.shift_to_elem(3)
         self.play(Transform(label,label17))
         self.play(Transform(label,label18))
        
         self.play(FadeOut(arr), FadeOut(pointer2), FadeOut(label))

         cpp_code = """
            ll n; cin >> n;
            vll a(n); for(ll i = 0; i < n; i++){cin >> a[i];}
            ll mn = a[0], prefix_cur = 0, min_pos = 0;
            for(ll i = 0; i < n; i++){
                prefix_cur+=a[i];
                if(prefix_cur<mn){mn=prefix_cur; min_pos = i;}
            }
            ll ans = 0;
            for(ll i = 0; i < n; i++){
                ans += a[i];
                if(i==min_pos){ans=abs(ans);}
            }
            cout << ans << endl;
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
         self.play(FadeOut(code))
         


