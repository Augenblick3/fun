from sympy import symbols, diff, integrate, sin, cos, exp

x = symbols('x')

f = x**2 +2*x +1

f_prime = diff(f,x)
print(f"f(x)={f}")
print(f"f'(x)={f_prime}")

g = sin(x) + cos(x) +exp(x)

g_integral = integrate(g,x)
print(f"g(x)={g}")
print(f"integral = {g_integral}")

from sympy import pi
g_integral_definite = integrate(g,(x, 0, pi))
print(f"{g_integral_definite}")
