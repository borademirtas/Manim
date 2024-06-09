from manim import *
from manim_data_structures import * 

class C2(Scene):
    def construct(self):
        arr = MArray(
            self,
            arr = [1,-1,-3,3,-3],
            hide_index=True,
        )
        arr.center()
        self.play(Create(arr))
        
        hint1 = Text("Hint 1: When can we pick either option?")
        self.wait(1)
        self.play(arr.animate.shift(DOWN*2))
        self.play(Write(hint1))
        self.wait(1)
        hintans = MathTex("c + a_i = |c + a_i|", font_size = 60)
        self.play(Transform(hint1, hintans))
        self.wait(1)

        label = Text("Ans: ", color=WHITE).to_edge(DL, buff=0.5)
        counter = Integer(0, color=WHITE).next_to(label, RIGHT).scale(1.5)
        counter_group = VGroup(label, counter)
        counter_group.to_edge(DOWN, buff=1)
        self.play(Create(counter_group))

        hint2 = Text("Hint 2: When will c be non-negative?")
        self.play(Transform(hint1, hint2))
        self.wait(1)
        hintans2 = Text("1. Prefix sum is non-negative\n2.We are after prefix min\n")
        self.wait(1)
        self.play(Transform(hint1, hintans2))
        self.play(FadeOut(hint1))

        self.play(arr.animate.shift(UP*2))

        pointer = MArrayPointer(self, arr, 0, '')
        self.play(arr.animate_elem_square(0).set_fill("#D74D4D"))
        pointer.shift_to_elem(1)
        self.play(arr.animate_elem_square(1).set_fill("#D74D4D"))
        pointer.shift_to_elem(2)
        window = MArraySlidingWindow(self, arr, 3, 2, '')
        self.play(Create(window))
        self.wait(1)

        val = MathTex(r"2^2 \times 2^2", font_size=60)
        val2 = MathTex("16", font_size=60)
        val.shift(DOWN*2)
        val2.shift(DOWN*2)
        self.play(Create(val))
        self.wait(1)
        self.play(Transform(val,val2),counter.animate.set_value(16))
        self.play(FadeOut(val), FadeOut(window))
        self.wait(1)

        pointer.shift_to_elem(3)
        self.play(arr.animate_elem_square(3).set_fill("#D74D4D"))
        pointer.shift_to_elem(4)

        val = MathTex(r"2^3 \times 2^0", font_size=60)
        val2 = MathTex("8", font_size=60)
        val.shift(DOWN*2)
        val2.shift(DOWN*2)
        self.play(Create(val))
        self.wait(1)
        self.play(Transform(val,val2),counter.animate.set_value(24))
        self.play(FadeOut(val), FadeOut(counter_group))
        self.wait(1)

        cpp_code = """
            ll n; cin >> n;
            vector<ll> pow_2(n+1); pow_2[0] = 1;
            for(ll i = 1; i <= n; i++){pow_2[i]=pow_2[i-1]*2%mod;}
            vector<ll> a(n); for(ll i = 0; i < n; i++){cin >> a[i];}
            ll mn = a[0], cur = 0;
            for(ll i = 0; i < n; i++){
                cur += a[i];
                mn = min(cur,mn);
            }
            if(mn>=0){cout << pow_2[n] << endl; return;}
    
            cur = 0; ll pre_cnt = 0, ans = 0;
            for(ll i = 0; i < n; i++){
                if(cur+a[i]>=0){pre_cnt++;}
                cur += a[i];
                if(cur==mn){ans += pow_2[pre_cnt+(n-i-1)]; ans%=mod;}
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
