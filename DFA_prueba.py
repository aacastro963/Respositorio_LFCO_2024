'''
Script ejemplopara la clase LFCO 2024 - II de Automatas determinísticos

'''

#Librerias a utilizar

#Crear las variables globales o constantes

#Definir la clase

class AUTOMATA_DFA:
    def __init__(self, estados, alfabeto, funcion_de_transicion, estado_inicial, estado_final):
        self.estado = estados
        self.alfabeto = alfabeto
        self.funcion_de_transicion = funcion_de_transicion
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.estado_actual = estado_inicial

    def reseteo (self):
        self.estado_actual = self.estado_inicial

    def transicion(self, simbolo_entrada):
        if simbolo_entrada in self.alfabeto:
            self.estado_actual = self.funcion_de_transicion[self.estado_actual][simbolo_entrada]
        else:
            raise ValueError(f'Simbolo de entrada {simbolo_entrada} no está en el alfabeto')

    #  "1010"
    def aceptacion(self, cadena_unica):
        self.reseteo()
        try:
            for simbolo in cadena_unica: # 1010
                self.transicion(simbolo)
            return self.estado_actual in self.estado_final
        except KeyError:
            return False

    

#Definición del dfa

estados = {'qo', 'q1'}
alfabeto = {'0', '1'}
funcion_de_transicion = {
    'q0' : {'0': 'q1', '1': 'q0'},
    'q1' : {'0': 'q0', '1': 'q1'}
}

estado_inicial = 'q0'
estado_final = {'q0'}

# Crear el DFA
automata_dfa = AUTOMATA_DFA(estados, alfabeto, funcion_de_transicion, estado_inicial, estado_final)

#Cadenas de prueba para el automata 
test_cadenas = ["", "0", "1", "10", "101", "1010", "1001", "1100", "000", "111"]

for cadena_unica in test_cadenas:
    resultado = automata_dfa.aceptacion(cadena_unica)
    print(f'La cadena "{cadena_unica}" es aceptada por el automata determinístico: {resultado}')