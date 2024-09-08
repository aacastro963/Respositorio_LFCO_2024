import random

class CFG:
    def __init__(self, grammar, start_symbol):
        self.grammar = grammar  # Diccionario que contiene las producciones de la gramática
        self.start_symbol = start_symbol  # Símbolo de inicio

    def generate(self, current_symbol=None):
        # Si no se proporciona un símbolo actual, empezamos con el símbolo inicial
        if current_symbol is None:
            current_symbol = self.start_symbol

        # Si el símbolo actual es un terminal, devolverlo
        if current_symbol not in self.grammar:
            return current_symbol

        # Elegir una producción aleatoria para el símbolo no terminal actual
        production = random.choice(self.grammar[current_symbol])

        # Generar la cadena recursivamente para cada símbolo en la producción
        return ''.join(self.generate(symbol) for symbol in production)

# Definir la gramática libre de contexto
grammar = {
    'S': [['a', 'S', 'b'], ['']],
    # S -> aSb | ε
}

# Crear una instancia de la CFG
cfg = CFG(grammar, 'S')

# Generar varias cadenas a partir de la gramática
for _ in range(5):
    generated_string = cfg.generate()
    print(f"Cadena generada: '{generated_string}'")