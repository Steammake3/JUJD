import re
import Tokenize

def interpret(life : list):
    f = Tokenize.Token("s", "d")
    s=0
    func_re = re.compile(r"(\S+)\((.*)\)")
    for line in life:
        real = re.search(func_re, line)
        if line == "_run:":
            s = 1
        else:
            v = real.group(1)
            if v == "print" and s:
                print(real.group(2))
        

if __name__ == "__main__":
    interpret("t")