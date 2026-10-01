class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs(expr: str) -> set[str]:
            # groups holds sets that are separated by top-level commas (to be unioned)
            # current_group holds sets that are adjacent (to be cross-multiplied)
            groups = []
            current_group = [set([""])]
            
            i = 0
            while i < len(expr):
                if expr[i] == '{':
                    # Find the matching closing brace for this level
                    start = i + 1
                    layer = 1
                    i += 1
                    while layer > 0:
                        if expr[i] == '{': layer += 1
                        elif expr[i] == '}': layer -= 1
                        i += 1
                    
                    # Recursively solve the content inside the braces
                    inner_res = dfs(expr[start:i-1])
                    
                    # Cross-multiply the inner result with the last item in the current group
                    next_group = []
                    for s1 in current_group[-1]:
                        for s2 in inner_res:
                            next_group.append(s1 + s2)
                    current_group[-1] = set(next_group)
                    
                elif expr[i] == ',':
                    # Comma means we finish the current concatenated group and start a new one
                    groups.append(current_group)
                    current_group = [set([""])]
                    i += 1
                    
                else:
                    # Treat regular characters as a single-element set
                    next_group = []
                    for s1 in current_group[-1]:
                        next_group.append(s1 + expr[i])
                    current_group[-1] = set(next_group)
                    i += 1
            
            groups.append(current_group)
            
            # Combine all results: flat-map each group's cross-multiplication, then union them
            final_set = set()
            for group in groups:
                # Multiply all sets within the same comma-separated group
                combined = group[0]
                for next_set in group[1:]:
                    temp = set()
                    for s1 in combined:
                        for s2 in next_set:
                            temp.add(s1 + s2)
                    combined = temp
                final_set.update(combined)
                
            return final_set

        # Return sorted list of unique words
        return sorted(list(dfs(expression)))
