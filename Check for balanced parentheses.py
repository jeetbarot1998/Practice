def is_balanced(s: str) -> bool:
    stack = []
    # Dictionary to hold matching parentheses
    matching_parenthesis = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching_parenthesis.values():
            # If it's an opening parenthesis, push onto stack
            stack.append(char)
        elif char in matching_parenthesis.keys():
            # If it's a closing parenthesis, check if stack is not empty and top of stack is matching opening
            if stack == [] or matching_parenthesis[char] != stack.pop():
                return False

    # If stack is empty at the end, all parentheses are balanced
    return stack == []

# Example usage
test_string = "{[()()]}"
print(is_balanced(test_string))  # Output: True

test_string = "{[(])}"
print(is_balanced(test_string))  # Output: False


# ========================================================================================================
# Number of operations(Addition/Deletion) needed to balance a string(“{abc}{def{gfh{ij}}}“)

def count_unbalanced_parentheses(s: str) -> int:
    stack = []
    unbalanced_count = 0

    for char in s:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if stack:
                stack.pop()
            else:
                unbalanced_count += 1
    
    unbalanced_count += len(stack)
    return unbalanced_count

# Test cases
input_1 = "{abc}{def{gfh{ij}}}"
output_1 = count_unbalanced_parentheses(input_1)
print(f"input_1 = {input_1}\noutput_1 = {output_1}\n")

input_2 = "abc}{def{gfh{ij}}}"
output_2 = count_unbalanced_parentheses(input_2)
print(f"input_2 = {input_2}\noutput_2 = {output_2}\n")

input_3 = "abc}{def{gfh{ij}}} }"
output_3 = count_unbalanced_parentheses(input_3)
print(f"input_3 = {input_3}\noutput_3 = {output_3}\n")

input_4 = "}{"
output_4 = count_unbalanced_parentheses(input_4)
print(f"input_4 = {input_4}\noutput_4 = {output_4}\n")
