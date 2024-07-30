'''Para diseñar un DFA que acepte cadenas que contienen un número par de ceros, podemos seguir estos pasos:

Definir los estados: Necesitamos dos estados: uno para las cadenas con un número par de ceros (q0) y otro para las cadenas con un número impar de ceros (q1).
Definir el alfabeto: El alfabeto será {0, 1}.
Definir la función de transición: Las transiciones cambiarán entre los estados dependiendo del número de ceros leídos.
Definir el estado inicial: El estado inicial será q0 (número par de ceros).
Definir los estados de aceptación: El estado de aceptación será q0.
Aquí tienes el código para implementar este DFA en Python:'''

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state

    def reset(self):
        self.current_state = self.start_state

    def transition(self, input_symbol):
        if input_symbol in self.alphabet:
            self.current_state = self.transition_function[self.current_state][input_symbol]
        else:
            raise ValueError(f"Input symbol {input_symbol} is not in the alphabet")

    def accepts(self, input_string):
        self.reset()
        try:
            for symbol in input_string:
                self.transition(symbol)
            return self.current_state in self.accept_states
        except KeyError:
            return False

# Definición del DFA
states = {'q0', 'q1'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': 'q1', '1': 'q0'},  # Transición desde el estado q0
    'q1': {'0': 'q0', '1': 'q1'},  # Transición desde el estado q1
}
start_state = 'q0'
accept_states = {'q0'}

# Crear el DFA
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Probar el DFA con varias cadenas de entrada
test_strings = ["", "0", "1", "10", "101", "1010", "1001", "1100", "000", "111"]

for string in test_strings:
    result = dfa.accepts(string)
    print(f"La cadena '{string}' es aceptada por el DFA: {result}")


'''Explicación:
Clase DFA:

__init__: Inicializa el DFA con sus estados, alfabeto, función de transición, estado inicial y estados de aceptación.
reset: Reinicia el DFA al estado inicial.
transition: Realiza la transición del estado actual al siguiente estado según el símbolo de entrada.
accepts: Comprueba si una cadena de entrada es aceptada por el DFA.
Definición del DFA:

states: Conjunto de estados (q0, q1).
alphabet: Alfabeto del DFA (0, 1).
transition_function: Función de transición que define las transiciones entre estados para cada símbolo del alfabeto.
start_state: Estado inicial (q0).
accept_states: Conjunto de estados de aceptación (q0).
Probar el DFA:

Se prueban varias cadenas de entrada para verificar si son aceptadas por el DFA.
Este DFA acepta cadenas que contienen un número par de ceros, cambiando de estado cada vez que lee un cero.'''
