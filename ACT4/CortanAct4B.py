A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

A_and_B = A & B
print("a. Elements in A and B:", A_and_B, "Count:", len(A_and_B))

B_not_A_C = B - (A | C)
print("b. Elements in B that are not part of A and C:", B_not_A_C, "Count:", len(B_not_A_C))

h_i_j_k = C - (A | B)
print("i. {h, i, j, k}:", h_i_j_k)

c_d_f = C & A
print("ii. {c, d, f}:", c_d_f)

b_c_h = B & C
print("iii. {b, c, h}:", b_c_h)

d_f = A & C - B
print("iv. {d, f}:", d_f)

c_only = C - (A | B)
print("v. {c}:", c_only)

l_m_o = B - (A | C)
print("vi. {l, m, o}:", l_m_o)
