from manim import *
import math
config.media_width = "100%"

%%manim -v Warning --disable_caching -qm Intro

class Intro(Scene):
    def construct(self):
        say = Text('\"Without mathematics, there\'s nothing you can do. \nEverything around you is mathematics. \nEverything around you is numbers.\"', 
        slant=ITALIC,
        font_size=32,
        )

        name = Text('- Shakuntala Devi', font_size=24, color=RED).shift(DOWN*2+RIGHT*1)


        self.play(Create(say),  run_time=4)
        self.play(Create(name))
        self.wait(duration=2)

position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]


class Geometry(Scene):
    def construct(self):

# Show pythagorean Theorem

        text = Text("Pythagorean Theorem", gradient=(RED, BLUE, GREEN), font_size=64)

# Create a grid to control the positions

        d = VGroup()
        for i in range(0,150):
            d.add(Dot())
        d.arrange_in_grid(buff=0.75).shift(DOWN*1.1)

# Create a triangle

        tri1 = VGroup()
        line1 = Line(d[15].get_center(), d[67].get_center(), color=BLUE)
        line2 = Line(d[67].get_center(), d[65].get_center(), color=GREEN)
        line3 = Line(d[15].get_center(), d[65].get_center(), color=RED)
        tri1.add(line1, line2, line3)

        right_angle = always_redraw(lambda: RightAngle(line1, line2 , quadrant=(-1, 1)))

        angle_Beta = always_redraw(lambda:  Angle(line2, line3 , quadrant=(-1, -1), radius=0.35, other_angle=False))

        angle_Alpha = always_redraw(lambda:  Angle(line1, line3 , quadrant=(1, 1), radius=0.35, other_angle=True))

        AlphaTex = always_redraw(lambda: MathTex(r"\alpha").move_to(
            Angle(
                line1, line3, radius=0.5 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        ).scale(0.8)
        )

        BetaTex = always_redraw(lambda: MathTex(r"\beta").move_to(
            Angle(
                line2, line3, radius=0.5 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        ).scale(0.8)
        )

        side_a = always_redraw(lambda: Tex("a").next_to(line2, DOWN, buff=0.15).scale(0.8))
        side_b = always_redraw(lambda: Tex("b").next_to(line1, RIGHT, buff=0.15).scale(0.8).shift(UP*0.3))
        side_c = always_redraw(lambda: Tex("c").next_to(line3, LEFT).scale(0.8).shift(RIGHT*1))

# Intro Animation
        self.play(AddTextWordByWord(text, run_time=3))
        self.play(text.animate.to_edge(UL), run_time=1.5)
        self.play(FadeTransform(text, d, stretch=False, run_time=2))
        self.play(Create(tri1))
        self.play(FadeOut(d))
        self.play(FadeIn(side_a), FadeIn(side_b), FadeIn(side_c))
        self.play(FadeIn(angle_Alpha), FadeIn(angle_Beta), FadeIn(right_angle), Create(AlphaTex), Create(BetaTex))
        self.wait()

# Copy Triangles

        tri2 = tri1.copy()
        tri3 = tri1.copy()
        tri4 = tri1.copy()

        self.play(tri2.animate.rotate(PI/2), tri3.animate.rotate(-PI/2))
        self.play(tri2.animate.next_to(tri1, DOWN, buff=0), tri3.animate.next_to(tri1, RIGHT, buff=0))
        self.play(tri2.animate.shift(RIGHT*0.9), tri3.animate.shift(UP*0.9), run_time=0.5)
        self.play(tri4.animate.rotate(PI))
        self.play(tri4.animate.next_to(tri2, RIGHT, buff=0))
        self.play(tri4.animate.shift(UP*0.9))
        self.wait()

# Complement Sides
        sq = Polygon(d[41].get_center(), d[43].get_center(), d[69].get_center(), d[67].get_center(), color=YELLOW)
        sq_line = Line(d[41].get_center(), d[43].get_center(), color=YELLOW)
        b1 = Brace(sq_line)
        b1_text = b1.get_text("b-a").scale(0.8)
        side_c2 = always_redraw(lambda: Tex("c").next_to(
          Line(d[15].get_center(), d[71].get_center(), color=RED), 
          UP).scale(0.8).shift(RIGHT*0.8+DOWN*1))

        self.play(Create(VGroup(sq, sq_line)), run_time=1.5)
        self.play(FadeIn(VGroup(b1, b1_text, side_c2)))
        self.wait()

# Text Proof
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        Proof = VGroup(
           MathTex(r"4\triangle + \square = \square", tex_template=myTemplate, font_size=50),
           MathTex(r"4(\frac{1}{2}ab) + (b-a)^2 = c^2", font_size=38),
           MathTex(r"2ab + b^2 - 2ab + a^2 = c^2", font_size=38),
           MathTex(r"a^2 + b^2 = c^2", font_size=45)
        )

        Proof.arrange(DOWN, buff=MED_LARGE_BUFF)
        index_labels(Proof[0][0])
        Proof[0][0][3].set_color(YELLOW)
        Proof[0][0][5].set_color(RED).scale(1.3)
        framebox1 = SurroundingRectangle(Proof[3], buff = 0.2).shift(RIGHT*4+DOWN*0.3)

        self.play(FadeIn(Proof[0].move_to([4, 2.8, 0])))
        self.play(
            TransformMatchingTex(Proof[0].copy(), Proof[1].shift(RIGHT*4+UP*0.8)),
            run_time=2
        )
        self.wait()
        self.play(
            TransformMatchingTex(Proof[1].copy(), Proof[2].shift(RIGHT*4+UP*0.2)),
            run_time=2
        )
        self.wait()
        self.play(
            TransformMatchingTex(Proof[2].copy(), Proof[3].shift(RIGHT*4+DOWN*0.3)),
            run_time=2
        )
        self.play(Create(framebox1))
        self.wait()