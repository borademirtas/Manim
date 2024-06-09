from manim import *

colors = [YELLOW, BLUE, BLUE, RED]

class CodeforcesGlobalRound26(Scene):
    def construct(self):
        
        
        words = VGroup(
            Text("Codeforces", font_size=72),
            Text("Global", font_size=72),
            Text("Round 26", font_size=72),
            Text("Video Editorial", font_size=72)

        )
        
        words.arrange(DOWN, buff=0.5)
        
        for word, color in zip(words, colors):
            word.set_color(color)

        self.play(Write(words))
        self.play(AnimationGroup(*[word.animate.scale(1.5) for word in words], lag_ratio=0.3))
        self.play(words.animate.set_color_by_gradient(*colors), run_time=2)
        self.play(ApplyWave(words))
        self.play(Rotate(words, angle=-PI / 4), FadeOut(words))
