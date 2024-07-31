'''
Script de Clase LFCO 2024

Paradigma POO
'''

#Librerias

#Definir las variables globales

#Clases-Metodos o Funciones 
class AUTOMATA_DFA:
    def __init__(self, estados, alfabeto, f_transicion, est_inicial, est_final):
        self.estado = estados
        self.alfabeto = alfabeto
        self.f_transicion = f_transicion
        self.est_inicial = est_inicial
        self.est_final = est_final
        self.est_actual = est_inicial

    def reseteo (self):
        self.est_actual = self.est_inicial

    def transicion (self, simbolo):
        if simbolo in self.alfabeto:
            self.est_actual = self.f_transicion [self.est_actual][simbolo]
        else:
            raise ValueError(f'simbolo de entrada "{simbolo}" no pertenece al alfabeto :( ')

    def aceptacion (self, cadena_unica):
        self.reseteo()
        for simbolo in cadena_unica:
            self.transicion(simbolo)
        return self.est_actual in self.est_final


#--------------------------------------------#
            #Definir el DFA
#--------------------------------------------#

if __name__ == '__main__':
    print("Inicio Script......")
    estados = {'q0', 'q1'}
    alfabeto = {'0', '1'}
    f_transicion = {
        'q0' : {'0': 'q1', '1':'q0'},
        'q1' : {'0': 'q0', '1':'q1'}
    }

    est_inicial = 'q0'
    est_final = {'q0'}

#--------------------------------------------#
            #Instanciar la clase DFA
#--------------------------------------------#

    automata_dfa = AUTOMATA_DFA(estados, alfabeto, f_transicion, est_inicial, est_final)
    test_cadena = ["", "0", "1", "10C", "1010", "1010", "1100", "000", "111"]
    for cadena_unica in test_cadena:
        resultado = automata_dfa.aceptacion(cadena_unica)
        print(f'La cadena {cadena_unica} es acptada por el DFA: {resultado}')
    print("Finalizo Script")