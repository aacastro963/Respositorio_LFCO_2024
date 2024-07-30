'''
Script Ejemplo para la clase LFCO 2024 - II de Automatas determinísticos
Paradigma: POO
Version 1.0
Docente: Adolfo Andrés Castro Sánchez
Universidad EAFIT
Escuela de Ciencias aplicadas e Inegniería

Funcionamiento:
Se prueban varias cadenas de entrada para verificar si son aceptadas por el DFA.
Este DFA acepta cadenas que contienen un número par de ceros, cambiando de estado cada vez que lee un cero
'''

#Librerías

#Variables Globales

#Clases y métodos (Funciones) ==> Paradigma a usar POO
class AUTOMATA_DFA:
    def __init__(self, estados, alfabeto, f_transicion, est_inicial, est_final):
        self.estado = estados
        self.alfbeto = alfabeto
        self.f_transicion = f_transicion
        self.est_inicial = est_inicial
        self.est_final = est_final
        self.estado_actual = est_inicial

    def reseteo(self):
        self.estado_actual = self.est_inicial

    def transicion(self, simbolo):
        if simbolo in self.alfbeto:
            self.estado_actual = self.f_transicion[self.estado_actual][simbolo]
        else:
            raise ValueError(f'simbolo de entrada {simbolo} no pertenece al alfabeto')
            #print(f'El simbolo {simbolo} no pertenece al alfabeto')



    def aceptacion(self, cadena_unica):
        self.reseteo()
        try:            
            for simbolo in cadena_unica:
                self.transicion(simbolo)
            return self.estado_actual in self.est_final
        except KeyError:
            return False

#Código Main
if __name__ == '__main__':

#---------------------------------------------------------------------#
                            #Definir el DFA
#---------------------------------------------------------------------#

    estados = {'q0', 'q1'}
    alfabeto = {'0', '1'}
    f_transicion = {
        'q0' : {'0' : 'q1', '1': 'q0'},
        'q1' : {'0' : 'q0', '1': 'q1'}
    }

    est_inicial = 'q0'
    est_final = {'q0'}

#---------------------------------------------------------------------#
                    #INSTANCIAR LA CLASE AUTOMATA_DFA
#---------------------------------------------------------------------#

    automata_dfa = AUTOMATA_DFA(estados, alfabeto, f_transicion, est_inicial, est_final)

#*********************************************************************#
    test_cadena =["", "0", "1", "10", "1010", "1010", "1001", "1100", "000", "111"]
    for cadena_unica in test_cadena:
        resultado = automata_dfa.aceptacion(cadena_unica)
        print (f'La cadena "{cadena_unica}" es aceptada por el DFA: {resultado}')

    print ("Finalizo Script_1 DFA LFCO 2024....... ")
    