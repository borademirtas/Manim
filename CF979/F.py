from manim import *
from manim_data_structures import * 

import itertools



class F(Scene):

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
            color = fill_color[v]

        list[idx]=v

        self.play(
            arr.animate_elem_square(idx).set_fill(color),
        )


    def construct(self):
        
        b = MArray(self,hide_index=True)
        a = MArray(self,hide_index=True)
        imp = MArray(self,hide_index=True)
        one = MArray(self,hide_index=True)
        two = MArray(self,hide_index=True)
        three = MArray(self,hide_index=True)
        example = MArray(self, hide_index=True)
        counter = MArray(self, hide_index=True)

        self.construct_array(b, [2,1,1,3,3,1,1,2], {}, {}, {})
        self.construct_array(one, [1,2,5,6], {}, {}, {})
        self.construct_array(two, [0,7], {}, {}, {})
        self.construct_array(three, [3,4], {}, {}, {})
        self.construct_array(a, [2,3,1,2,3,5], {}, {}, {})
        self.construct_array(imp, [1,2,1,2], {},{},{})
        self.construct_array(example, [1,2,3,2,1,3,2,3], {},{},{})
        self.construct_array(counter, [1,2,2,1], {},{},{})

         
        text = MathTex(r"S = \{ 1, 2, 3 \}")
        text2 = MathTex(r"S = \{ 1, 2 \}")
        text3 = MathTex(r"S = \{ 2 \}")
        text.shift(DOWN*1.5)
        text2.shift(DOWN*1.5)
        text3.shift(DOWN*1.5)

        question = Text("Can we make B empty?", font_size=32, color = GOLD)
        question.shift(UP*1.5)

        self.play(Create(b))
        self.wait(2)
        self.play(Write(question))
        self.wait(2)
        self.play(Create(text))
        self.wait(2)

        self.play(Transform(text,text2))
        b.remove_elem(3)
        self.play(b.animate.move_to(ORIGIN))
        b.remove_elem(3)
        self.play(b.animate.move_to(ORIGIN))
        self.play(Transform(text,text3))
        b.remove_elem(1)
        self.play(b.animate.move_to(ORIGIN))
        b.remove_elem(1)
        self.play(b.animate.move_to(ORIGIN))
        b.remove_elem(1)
        self.play(b.animate.move_to(ORIGIN))
        b.remove_elem(1)
        self.play(b.animate.move_to(ORIGIN))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        
        self.play(Create(a))
        window = MArraySlidingWindow(self, a, 1, 3, 'Query')
        self.play(Create(window))
        window.shift_to_elem(3)
        window.resize_window(2)
        window.shift_to_elem(0)
        window.resize_window(6)
        self.wait(1)
        self.play(FadeOut(window))
        
        hint = Text("Try to draw some impossible cases", font_size=32, color = GOLD)
        hint2 = Text("Each operation V has to erase all occurences of V", font_size=32, color = GOLD)
        hint3 = Text("All elements of V must form a subarray when operation V is used", font_size=32, color = GOLD)
        hint4 = Text("Can we find the smallest value of t, for any fixed i?", font_size=32, color = GOLD)

        hint.shift(UP*1.5)
        hint2.shift(UP*1.5)
        hint3.shift(UP*1.5)
        hint4.shift(UP*1.5)

        self.play(Write(hint))
        self.wait(5)
        self.play(FadeOut(a))
        self.play(Create(imp))
        sets = MathTex(r"S = \{ 1, 2\}")
        sets.shift(DOWN*1.5)
        self.play(Write(sets))
        self.wait(3)
        self.play(Transform(hint,hint2))
        self.wait(5)
        self.play(Transform(hint,hint3))
        self.wait(5)
        condition = MathTex(
            r"Impossible \ condition:",
            r"i < j < k < t",
            r"a[i] = a[k] \quad \text{and} \quad a[j] = a[t] \quad \text{and} \quad a[i] \neq a[j]"
        ).arrange(DOWN)
        condition.shift(DOWN*3)
        self.play(Write(condition))
        self.wait(3)
        self.play(Transform(hint,hint4))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        hint5 = Text("left[i] = last occurence of a[i] before i", color = GOLD)
        self.play(Write(hint5))
        question2 = Text("How do we compute left?", font_size =32, color = GOLD)
        question2.shift(UP*1.5)
        self.play(Write(question2))
        self.wait(2) 
        self.play(FadeOut(hint5))
        self.play(Create(b))

        one.scale(0.75)
        two.scale(0.75)
        three.scale(0.75)

        one.shift(DOWN*3)
        two.shift(DOWN*2)
        three.shift(DOWN)

        self.play(Create(three))
        three.update_mob_arr_label('3')

        self.play(Create(two))
        two.update_mob_arr_label('2')

        self.play(Create(one))
        one.update_mob_arr_label('1')

        self.wait(10)

        self.play(FadeOut(*self.mobjects))

        hint6 = Text("right[i] = first occurence of a[i] after i", color = GOLD)
        self.play(Write(hint6))
        question3 = Text("How do we compute right?", font_size =32, color = GOLD)
        question3.shift(UP*1.5)
        self.play(Write(question3))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        hint7 = Text("Fix some of the values in the condition", color = GOLD, font_size = 32)
        hint7.shift(UP*1.5)
        hint8 = Text("What happens when we fix k and set i to left[k]?", color = GOLD, font_size = 32)
        hint8.shift(UP*1.5)

        condition.shift(UP*3)
        self.play(Write(condition))
        self.wait(3)
        self.play(Write(hint7))
        self.wait(3)
        self.play(Transform(hint7,hint8))
        self.wait(3)
        self.play(FadeOut(condition))
        self.play(Create(example))
        self.wait(3)
        
        pointer1 = MArrayPointer(self, example, 2)
        pointer2 = MArrayPointer(self, example, 5)
        self.play(Create(pointer1), Create(pointer2))
        self.wait(3)
        window2 = MArraySlidingWindow(self, example, 3,2,'')
        window3 = MArraySlidingWindow(self, example, 6,2,'')
        self.play(Create(window2), Create(window3))
        self.wait(3)

        hint9 = Text("How can we find smallest index in (k, n) that appears in (left[k], k)?", color = GOLD, font_size = 32)
        hint9.shift(UP*1.5)
        self.play(Transform(hint7,hint9))
        self.wait(5)
        self.play(FadeOut(window2), FadeOut(window3), FadeOut(pointer1), FadeOut(pointer2))
        
        segtree = Paragraph(
            "Minimum Segment Tree",
            "set(i,x): sets the ith element to x",
            "get_min(l,r): gets the minimum value in the range [l,r)",
            alignment="center",
        )
        segtree.scale(0.75)
        segtree.shift(DOWN*1.5)
        self.play(Write(segtree))
        self.wait(7)
        self.play(FadeOut(example), FadeOut(hint7))

        hint10 = Text("What is the issue with our approach?", color = GOLD, font_size = 32)
        hint11 = Text("get_min(0,3) returns 2 which is less than 3")
        hint10.shift(UP*1.5)
        hint11.shift(UP*1.5)
        self.play(Create(hint10), Create(counter))
        self.wait(4)
        self.play(Transform(hint10,hint11))
        self.wait(4)
        self.play(FadeOut(*self.mobjects))

        hint6 = Text("killed[i] = the first index k where [i,k] is bad", color = GOLD)
        self.play(Write(hint6))
        question3 = Text("How do we answer the queries?", font_size =32, color = GOLD)
        question3.shift(UP*1.5)
        self.play(Write(question3))
        self.wait(3)
        self.play(FadeOut(*self.mobjects))

        cpp_code1 = """
        ll n,q; cin >> n >> q;
        vll a(n); for(ll i = 0; i < n; i++){cin >> a[i];}
        min_segment_tree<ll> right(n+5), killed(n+5);
        vector<vll> pos(n+1);

        vll left(n,-1);

        for(ll i = 0; i < n; i++){pos[a[i]].pb(i);}

        for(ll i = 1; i <= n; i++){
            for(ll j = 1; j < pos[i].size(); j++){
                left[pos[i][j]]=pos[i][j-1];
                right.set(pos[i][j-1], pos[i][j]);
            }
        }
        """


        code1 = Code(
            code=cpp_code1,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code1.move_to(ORIGIN)
        self.play(FadeIn(code1))
        self.wait(15)
        self.play(FadeOut(code1))

        cpp_code2 = """
        for(ll i = 0; i < n; i++){
            if(left[i]!=-1){
                right.set(left[i],1e18);
            }
            if(left[i]!=-1){
                killed.set(left[i], right.get_min(left[i],i));
            }
        }

        for(ll i = 0; i < q; i++){
            ll l,r; cin >> l >> r; l--; r--;
            if(killed.get_min(l,r+1)<=r){
                cout << "NO" << endl;
            }
            else{
                cout << "YES" << endl;
            }
        }
        """

        code2 = Code(
            code=cpp_code2,
            tab_width=4,
            background="window",
            language="C++",
            font="Monospace",
            font_size=24,
        )
        code2.move_to(ORIGIN)
        self.play(FadeIn(code2))
        self.wait(25)
        self.play(FadeOut(code2))
