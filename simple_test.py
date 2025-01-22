from sympy import symbols, solve

E = 12
r = 0.3
R = symbols('R')

# Power dissipation formula: P = (E**2) / (R + r)**2
power_dissipation = (E**2) / ((R + r)**2)
dP_dR = power_dissipation.diff(R)

# Solve for maximum power dissipation
R_max = solve(dP_dR, R)
print(f"Maximum power dissipation occurs at R = {R_max}")