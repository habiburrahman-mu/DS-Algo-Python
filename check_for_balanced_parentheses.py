open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check(string_):
    stack = []
    for i in string_:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "Unbalanced"

    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


assert check("{[]{()}}") == "Balanced"
assert check("[{}{})(]") == "Unbalanced"
assert check("((()") == "Unbalanced"
