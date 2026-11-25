from fractions import Fraction

h_lo, h_hi = map(int, input().split())
s_lo, s_hi = map(int, input().split())
v_lo, v_hi = map(int, input().split())
r, g, b = map(int, input().split())

V = max(r, g, b)
m = min(r, g, b)
S = Fraction(255 * (V - m), V)
if V == r:
	H = Fraction(60 * (g - b), V - m)
elif V == g:
	H = 120 + Fraction(60 * (b - r), V - m)
else:
	H = 240 + Fraction(60 * (r - g), V - m)
if H < 0:
	H += 360

if h_lo <= H <= h_hi and s_lo <= S <= s_hi and v_lo <= V <= v_hi:
	print('Lumi will like it.')
else:
	print('Lumi will not like it.')
