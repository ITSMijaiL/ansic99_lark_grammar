# ansic99_lark_grammar

I have been searching for an ANSI C grammar for [lark](https://github.com/lark-parser/lark/) to develop a small side project, but i haven't found any grammar yet which i found really strange.

So yeah, here's a working ANSI C99's grammar ported from lex and yacc to Lark's syntax, enjoy.

## How to use

```py
import lark
with open("ansi_c99_grammar.lark") as f:
    lp = lark.Lark(f.read())

tree = lp.parse(
"""
    int add(int a, int b){
        return a+b;
    }
""")

print(tree)
```

## Notes:
* **This grammar has been originally developed by the owner of [quut.com](https://www.quut.com/), Jutta Degener.** If it weren't because of her, this small project wouldn't even exist.
* The grammar doesn't supports preprocessor syntax, although i plan on adding it in the future.

## URLs of the original lex + yacc files:
* https://www.quut.com/c/ANSI-C-grammar-l-1999.html
* https://www.quut.com/c/ANSI-C-grammar-y-1999.html
