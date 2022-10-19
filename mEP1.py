A = int(input())
B = int(input())
C = int(input())
if A <= 0 or B <= 0 or C <= 0:
  print("Valores invalidos.")
elif A >= B + C or B >= A + C or C >= A + B:
  print("Valores nao podem formar um triangulo.")
else: 
  if A == B and B == C and C == A:
    print("Triangulo equilatero.")
  elif A == B or B == C or C == A:
    print("Triangulo isosceles.")
  elif A != B and B != C and C != A:
    print("Triangulo escaleno.")
  m, n, o = A, B, C
  if B >= A and B >= C:
    m, n, o = B, A, C
  if C >= A and C >= B:
    m, n, o = C, B, A
  if m**2 < n**2 + o**2:
    print("Triangulo acutangulo.")
  elif m**2 == n**2 + o**2:
    print("Triangulo retangulo.")
  elif m**2 > n**2 + o**2:
    print("Triangulo obtusangulo.")