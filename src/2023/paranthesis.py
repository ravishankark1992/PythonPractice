class Paranthesis:
    def validity_check(self, input_str: str) -> bool:
        if len(input_str)%2==1:
            return False
        open_list=["{", "[", "("]
        lookup = {'}': '{',
                ')': '(',
                ']': '['
                  }
        stack = []
        for c in input_str:
            if c in open_list:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False

                elif lookup[c] != stack.pop():
                    return False

        return False


def main():
    input_str = "()"
    paran_call = Paranthesis()
    paran_call.validity_check(input_str)
