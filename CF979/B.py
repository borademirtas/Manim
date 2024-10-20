from manim import *
from manim_data_structures import * 
import itertools


list = [1,0,1]

class B(Scene):

    def construct_array(self, arr, vals, outer_color, fill_color, value_color):
        
        fill = BLACK
        out = WHITE
        val = WHITE

        for v in vals:
            
            
            if v in fill_color:
                fill = fill_color[v]
            
            if v in outer_color:
                out = outer_color[v]
            
            if v in value_color:
                val = value_color[v]
            
            arr.append_elem(
                    value=v,
                    mob_square_args={'fill_color': fill, 'color': out},
                    mob_value_args={'color': val},
                    play_anim=False, 
                    append_anim=GrowFromCenter
                )
            arr.center()

    def updater(self, arr, idx, v, fill_color):

        arr.update_elem_value(index=idx, value=v, play_anim=True)

        color = WHITE

        if v in fill_color:
            color = fill_color

        self.play(
            arr.animate_elem_square(idx).set_fill(color),
        )


    def construct(self):

        arr = MArray(self,hide_index=True)
        subsets = [MArray(self,hide_index=True) for _ in range(10)]
        arr2 = MArray(self,hide_index=True)
        self.construct_array(arr,list, {0:WHITE, 1:WHITE}, {0:BLACK, 1:"#40E0D0"}, {0:"#40E0D0", 1:BLACK} )

        self.play(Create(arr))
        
        cnt = 0

        for subset_size in range(1, len(list) + 1):
            for indices in itertools.combinations(range(len(list)), subset_size):
                
                self.construct_array(subsets[cnt],[list[i] for i in indices], {0:WHITE, 1:WHITE}, {0:BLACK, 1:"#40E0D0"}, {0:"#40E0D0", 1:BLACK} )
            
                subsets[cnt].shift(DOWN*2)

                tmp = []
                for i in indices:
                    tmp.append(MArrayPointer(self, arr, i, ''))

                pointers = VGroup(*tmp)

                self.play(Create(pointers, run_time = 0.5))
                self.play(Create(subsets[cnt],run_time = 1))
                self.wait(0.5)

                self.play(FadeOut(pointers, run_time = 0.25),FadeOut(subsets[cnt], run_time = 0.25))
                
                cnt+=1
        
        hint_1 = Text("Hint 1: How many subsequences are there of of a string size N?", font_size = 32)
        
        hint_1.shift(UP*1.2)
        self.play(Create(hint_1), arr.animate.shift(DOWN))
        self.wait(1)

        pointer_1 = MArrayPointer(self, arr, 0, '')
        self.play(Create(pointer_1))
        pointer_1.shift_to_elem(1)
        self.wait(3)
        pointer_1.shift_to_elem(2)
        self.wait(3)

        text1 = MathTex(r"2 \times 2 \times 2 = 8", color = GOLD)
        text1.shift(DOWN*3)
        text2 = MathTex("8 - 1 = 7", color = GOLD)
        text2.shift(DOWN*3)
        text3 = MathTex(r"2^{N} - 1", color = GOLD)
        text3.shift(DOWN*3)

        box = SurroundingRectangle(text1, color=BLUE, buff=0.5)
        self.play(Create(text1), Create(box))
        self.wait(3)
        self.play(Transform(text1, text2))
        self.wait(3)
        self.play(Transform(text1, text3))
        self.wait(5)
        self.play(FadeOut(text1), FadeOut(box), FadeOut(pointer_1))


        hint_2 = Text("Hint 2: What is the lowest the oneness can be?", font_size = 32)
        hint_2.shift(UP*1.2)
        self.play(Transform(hint_1, hint_2))
        self.wait(5)
        claim = Text("Claim: We can always make the oneness equal to one", font_size = 32)
        claim.shift(UP*1.2)
        self.play(Transform(hint_1,claim))
        self.wait(5)
        self.play(FadeOut(arr))

        text4 = MathTex(r"2^{N} - 1", color = GOLD) 
        text4.scale(1.5)
        box = SurroundingRectangle(text4, color=BLUE, buff=0.5)
        text = VGroup(text4,box)
        self.play(Create(text))

        text5 = MathTex(r"\frac{2^{N}}{2}")
        text6 = MathTex(r"\frac{2^{N}}{2} - 1")
        text5.shift(DOWN*2+LEFT*2)
        text6.shift(DOWN*2+RIGHT*2)
        arrow1 = CurvedArrow(start_point=text.get_bottom()+LEFT*0.3, end_point=text5.get_top()+UP*0.1)
        arrow2 = CurvedArrow(start_point=text.get_bottom()+RIGHT*0.3, end_point=text6.get_top()+UP*0.1, angle=-PI/2)
        self.play(Create(text5), Create(text6))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(4)

        claim2= Text("Claim: A string with one 1 will have a oneness of 1", font_size = 32)
        claim2.shift(UP*1.2)    
        self.play(Transform(hint_1, claim2))

        self.construct_array(arr2,[1,0,0,0,0], {0:WHITE, 1:WHITE}, {0:BLACK, 1:"#40E0D0"}, {0:"#40E0D0", 1:BLACK} )

        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(text), FadeOut(text5), FadeOut(text6))
        self.wait(1)
        self.play(Create(arr2))
        text7 = MathTex(r"(2^{4}) - (2^{4}-1) = 1")
        text7.shift(DOWN*2.3)

        window1 = MArraySlidingWindow(self, arr2, 0, 1, 'Forced')
        window2 = MArraySlidingWindow(self, arr2, 1, 4, 'Optional')

        self.play(Create(window1))
        self.wait(3)
        self.play(FadeOut(window1), Create(window2))
        self.wait(3)

        window3 = MArraySlidingWindow(self, arr2, 0, 1, 'Banned')

        self.play(FadeOut(window2), Create(window3))
        self.wait(3)
        self.play(Create(text7))
        self.wait(3)
        self.play(FadeOut(arr2), FadeOut(text7), FadeOut(hint_1))
        cpp_code = """
        int n; cin >> n;
        cout << 1;
        for(int i = 1; i < n; i++){
            cout << 0;
        }
        cout << endl;
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
        self.wait(5)
        self.play(FadeOut(code))
