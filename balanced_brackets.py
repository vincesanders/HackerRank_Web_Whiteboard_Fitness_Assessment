def balancedBrackets(string):
    # Write your code here
    bracket_dict = {
        '[': ']',
        '(': ')',
        '{': '}',
        '|': '|'
    }
    possible_matches = {'[',']','(',')','{', '}', '|'}
    stack = []
    for char in string:
        if char not in possible_matches:
            continue
        if len(stack) is 0:
            stack.append(char)
        else:
            # compare the new bracket to bracket at top of stack
            if stack[len(stack) - 1] in bracket_dict and bracket_dict[stack[len(stack) - 1]] is char:
                # if match pop bracket off stack
                print('we are here')
                stack.pop()
            # if not match, add bracket to stack
            else:
                stack.append(char)
    if len(stack) > 0:
        return False
    else:
        return True