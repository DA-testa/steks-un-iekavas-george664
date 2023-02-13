
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
        pass

        if next in ")]}":
            if (len(opening_brackets_stack)==0):
                return i+1
            elif not are_matching(opening_brackets_stack[-1].char,next):
                return i+1
            opening_brackets_stack.pop()

    return len(opening_brackets_stack)
        


def main():
    text = input()
    print(text)
    mismatch = find_mismatch(text.replace(text[:5],""))
    if mismatch==0:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
