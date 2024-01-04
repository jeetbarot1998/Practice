def checkBalance(expr):  
    stack = []  
    for char in expr:  
        if char in ["(", "{", "["]:  
            stack.append(char)  
        else:  
  
            # Here we check if the current character is not opening  
            # bracket, then it must be closing.  
            # So stack cannot be empty at this point.  
            if not stack:  
                return False  
            curr_char = stack.pop()  
            if curr_char == '(':  
                if char != ")":  
                    return False  
            if curr_char == '{':  
                if char != "}":  
                    return False  
            if curr_char == '[':  
                if char != "]":  
                    return False  
  
    # Here we check empty stack  
    if stack:  
        return False  
    return True  
  
  
expr = "{[]{()}}"  
  
if checkBalance(expr):  
    print("The given string is balanced")  
else:  
    print("The given string is not balanced") 
