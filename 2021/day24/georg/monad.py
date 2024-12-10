x, y, z = 0, 0, 0

# max model number
# w14, w13, w12, w11, w10, w9, w8, w7, w6, w5, w4, w3, w2, w1 = 5, 9, 9, 9, 6, 9, 1, 2, 9, 8, 1, 9, 3, 9

# min model number
w14, w13, w12, w11, w10, w9, w8, w7, w6, w5, w4, w3, w2, w1 = 1, 7, 2, 4, 1, 9, 1, 1, 8, 1, 1, 9, 1, 5

print(f'{w14}{w13}{w12}{w11}{w10}{w9}{w8}{w7}{w6}{w5}{w4}{w3}{w2}{w1}')


"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
"""
z = w14 + 16

"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
"""
z = z * 26 + w13 + 3 

"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
"""
z = z * 26 + w12 + 2

"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
"""
z = z * 26 + w11 + 7

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
"""
if w10 == (z % 26) - 10:
    z = z // 26
else:
    z = z + w10 + 13 

"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
"""
z = z * 26 + w9 + 6

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
"""
if w8 == (z % 26) - 14:
    z = z // 26
else:
    z = z + w8 + 10

"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
"""
z = z * 26 + w7 + 11

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
"""
if w6 == (z % 26) - 4:
    z = z // 26
else:
    z = z + w6 + 6

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
"""
if w5 == (z % 26) - 3:
    z = z // 26
else:
    z = z + w5 + 5
z = z

"""
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
"""
z = z * 26 + w4 + 11

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
"""
if w3 == (z % 26) - 3:
    z = z // 26
else:
    z = z + w3 + 4

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
"""
if w2 == (z % 26) - 9:
    z = z // 26
else:
    z = z + w2 + 4


"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x -12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
"""
if w1 == (z % 26) - 12:
    z = z // 26
else:
    z = z + w1 + 6

print(z)
