from manim import *
from manim_data_structures import * 



list = [1,0,1]

class A(Scene):

    def construct_array(self, arr, vals, outer_color , fill_color, value_color) :

        fill = "#40E0D0"
        out = WHITE
        val = BLACK

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
        shuff = MArray(self,hide_index=True)
        min = MArray(self,hide_index=True)
        max = MArray(self,hide_index=True)

        best = MArray(self,hide_index=True)
        min2 = MArray(self,hide_index=True)
        max2 = MArray(self,hide_index=True)

        best = MArray(self,hide_index=True)
        min2 = MArray(self,hide_index=True)
        max2 = MArray(self,hide_index=True)


        self.construct_array(arr,[7,6,5,4], {}, {},{})
        self.construct_array(shuff,[6,5,4,7], {}, {},{})
        self.construct_array(min,[6,5,4,4], {}, {},{})
        self.construct_array(max,[6,6,6,7], {}, {},{})

        self.construct_array(best,[7,4,5,6], {}, {},{})
        self.construct_array(min2,[7,4,4,4], {}, {},{})
        self.construct_array(max2,[7,7,7,7], {}, {},{})

        self.play(Create(arr))
        arr.update_mob_arr_label(label = 'original')
        
        self.play(FadeOut(arr))
        self.play(Create(shuff))
        shuff.update_mob_arr_label(label = 'shuffled')
        self.play(shuff.animate.shift(UP*1.5))

        self.play(Create(min))
        min.update_mob_arr_label(label = 'min')
        self.play(min.animate.shift(DOWN*1.5))
        self.play(Create(max))
        max.update_mob_arr_label(label = 'max')
        self.wait(3)

        text = Text("Score: (6-6) + (6-5) + (6-4) + (7-4)", font_size = 32)
        text1 = Text("Score: 0 + 1 + 2 + 3 = 6", font_size = 32)
        text.shift(DOWN*3)
        text1.shift(DOWN*3)
        self.play(Create(text))
        self.wait(3)
        self.play(Transform(text,text1))
        self.wait(1)

        hint = Text("Hint: What is the maximum score of one index?", font_size = 32)
        claim = Text("Claim: Max score is max element - min element of entire array", font_size = 32)
        hint_2 = Text("Hint: How can we achieve this?", font_size = 32)
        claim_2 = Text("Claim: Set first element to max and second element to min", font_size = 32)

        tmp = VGroup(hint,claim,hint_2,claim_2)
        tmp.shift(UP*3)
        self.play(Create(hint))
        self.wait(3)
        self.play(Transform(hint, claim))
        self.wait(3)
        self.play(Transform(hint,hint_2))
        self.wait(3)
        self.play(Transform(hint,claim_2))

        self.play(FadeOut(shuff), FadeOut(min), FadeOut(max), FadeOut(text))

        best.shift(UP*1.5)
        self.play(Create(best))
        best.update_mob_arr_label(label = 'best')

        min2.shift(DOWN*1.5)
        self.play(Create(min2))
        min2.update_mob_arr_label(label = 'min')

        self.play(Create(max2))
        max2.update_mob_arr_label(label = 'max')
        self.wait(3)

        text2 = Text("Score: (7-7) + (7-4) + (7-4) + (7-4)", font_size = 32)
        text3 = Text("Score: 0 + 3 + 3 + 3 = 9", font_size = 32)

        text2.shift(DOWN*3)
        text3.shift(DOWN*3)

        self.play(Create(text2))
        self.wait(3)
        self.play(Transform(text2,text3))
        self.wait(1)

        self.play(FadeOut(best), FadeOut(min2), FadeOut(max2), FadeOut(hint), FadeOut(text2))

        cpp_code = """
        int n; cin >> n;
        vector<int> a(n);
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        sort(a.begin(), a.end());

        cout << (a[n-1]-a[0])*(n-1) << endl;
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
        self.wait(10)
        self.play(FadeOut(code))
