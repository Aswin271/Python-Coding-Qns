def isValid(s: str) -> bool:
    stack = []
    
    # Mapping of closing brackets to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'  # Pop from stack or assign a placeholder
            if bracket_map[char] != top_element:
                return False
        else:  # If it's an opening bracket, push to stack
            stack.append(char)
    
    # If the stack is empty, all brackets matched; otherwise, unbalanced
    return not stack
