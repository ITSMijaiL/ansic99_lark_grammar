import lark

lp = None

with open("ansi_c99_grammar.lark") as f:
    lp = lark.Lark(f.read())

t_hello_world = None
t_maths = None

with open("c_test_files/hello_world.c") as cf:
    t_hello_world = lp.parse(cf.read())

with open("c_test_files/maths.c") as cf:
    t_maths = lp.parse(cf.read())

print(t_hello_world)
print(t_maths)
