class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge list to a hash map for O(1) lookups
        lookup = {key: val for key, val in knowledge}
        
        res = []
        is_parsing_key = False
        current_key = []
        
        for char in s:
            if char == '(':
                is_parsing_key = True
            elif char == ')':
                is_parsing_key = False
                key_str = "".join(current_key)
                # Append the value if found, otherwise append "?"
                res.append(lookup.get(key_str, "?"))
                current_key = []
            else:
                if is_parsing_key:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
