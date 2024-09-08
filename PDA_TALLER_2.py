class PDA:
    def __init__(self):
        # Initialize the stack, starting state, and transitions
        self.stack = []
        self.state = 'q0'  # Initial state
        self.transitions = {
            ('q0', 'a', 'Z'): ('q0', 'AZ'),  # Push 'A' when 'a' is read and 'Z' is on top of the stack
            ('q0', 'a', 'A'): ('q0', 'AA'),  # Push 'A' when 'a' is read and 'A' is on top of the stack
            ('q0', 'b', 'A'): ('q1', ''),    # Pop 'A' when 'b' is read
            ('q1', 'b', 'A'): ('q1', ''),    # Continue popping 'A' with 'b'
            ('q1', '', 'Z'): ('qf', 'Z'),    # Accept if input is empty and stack has 'Z'
        }

    def step(self, state, symbol):
        if not self.stack:
            return False
        top_stack = self.stack.pop()  # Get top of the stack

        # Find the appropriate transition
        if (state, symbol, top_stack) in self.transitions:
            new_state, stack_op = self.transitions[(state, symbol, top_stack)]
            self.state = new_state

            # Handle stack operations (push new elements)
            for char in reversed(stack_op):
                if char:
                    self.stack.append(char)
            return True
        else:
            return False

    def accepts(self, input_string):
        # Start with the initial stack symbol 'Z'
        self.stack = ['Z']
        self.state = 'q0'

        # Process the input string symbol by symbol
        for symbol in input_string:
            if not self.step(self.state, symbol):
                return False

        # Perform the empty string transition at the end
        return self.step(self.state, '')

# Test the PDA
pda = PDA()

# Strings to test
strings_to_test = ['aabb', 'aaabbb', 'abab', 'aaaabbbb', 'aabbb']

for string in strings_to_test:
    result = pda.accepts(string)
    print(f"The string '{string}' is {'accepted' if result else 'rejected'} by the PDA.")

