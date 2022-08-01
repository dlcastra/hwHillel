#first task

comparison_nuber: bool = 3 != 5

print(comparison_nuber)

#second task

comparison_nuber1: bool = 5 == 5
comparison_nuber2: bool = 5 >= 5
comparison_nuber3: bool = 5 <= 5
comparison_nuber4: bool = not 5 < 5
comparison_nuber5: bool = not 5 > 5
comparison_nuber6: bool = not 5 != 5
comparison_nuber7: bool = not 5 == (not 5)
comparison_nuber8 = bool(5) or bool(5)
comparison_nuber9 = bool(5) or not bool(5)
comparison_nuber10 = bool(5) and bool(5)

print(comparison_nuber1)
print(comparison_nuber2)
print(comparison_nuber3)
print(comparison_nuber4)
print(comparison_nuber5)
print(comparison_nuber6)
print(comparison_nuber7)
print(comparison_nuber8)
print(comparison_nuber9)
print(comparison_nuber10)

# #third task

lg_oper = True or True and False
lg_oper1 = not True and not True or not False
lg_oper2 = not False or (not True and True)
lg_oper3 = True and True or not False
lg_oper4 = True or not True and not False

print(lg_oper)
print(lg_oper1)
print(lg_oper2)
print(lg_oper3)
print(lg_oper4)

# four task

comp_nb_with_oper = None != 7

print(comp_nb_with_oper)

# fifth task

comp_str_with_exp = bool("") < 10 - 1
comp_str_with_exp2 = bool("") != 10 - 1

print(comp_str_with_exp)
print(comp_str_with_exp2)

