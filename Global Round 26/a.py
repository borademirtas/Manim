from manim import *
from manim_data_structures import * 

class A(Scene):
    def construct(self):
        arr = MArray(
            self,
            arr = [1,1,2,3,4],
            hide_index=True,
        )
        arr.center()

        empty = MArray(
            self,
            arr = [1,1,1,1,1],
            hide_index=True,
        )
        empty.center()

        self.play(Create(arr))

        pointer1 = MArrayPointer(self, arr, 1, '')
        pointer2 = MArrayPointer(self, arr, 3, '')

        self.play(
            arr.animate_elem_square(1).set_fill("#D74D4D"),
            arr.animate_elem_square(3).set_fill("#D74D4D"),
            Create(pointer1),
            Create(pointer2)
            )
        self.wait(1)
        rr = Text("Red range: 3 - 1 = 2", color = RED, font_size=40)
        rr.shift(UP)
        br = Text("Blue range: 4 - 1 = 3", color = BLUE_C, font_size=40)
        self.play(arr.animate.shift(DOWN), FadeOut(pointer1), FadeOut(pointer2))
        self.play(Create(rr), Create(br))
        self.wait(1)
        self.play(FadeOut(rr), FadeOut(br),)
        

        hint1 = Text("Hint 1: How do we minimize a range?", font_size = 36)
        hint1.shift(UP*0.5)
        pointer1 = MArrayPointer(self, arr, 1, '')
        self.play(Create(hint1))
        self.wait(1)
        self.play( arr.animate_elem_square(3).set_fill(BLUE_D), Create(pointer1))
        self.wait(1)
        self.play(FadeOut(pointer1), FadeOut(arr), FadeOut(hint1))

        hint2 = Text("Hint 2: When is it impossible?")
        hint1.shift(UP*0.5)
        empty.shift(DOWN)
        self.play(Create(hint2))
        self.wait(1)
        self.play(Create(empty))
        self.wait(1)
        self.play(FadeOut(empty), FadeOut(hint2))
        self.wait(1)

        cpp_code = """
            int n; cin >> n;
            vector<int> a(n);
            for(int i = 0; i < n; i++){cin >> a[i];}
            if(a[0]==a[n-1]){cout << "NO" << endl;}
            else{
            
                cout << "YES" << endl;
            
                for(int i = 0; i < n; i++){
                    if(i==1){cout << 'R';}
                    else{cout << 'B';}
                }   
                
                cout << endl;
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
        self.play(FadeOut(code))
