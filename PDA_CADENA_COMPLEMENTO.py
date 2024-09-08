class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.complement = ""

    def transition(self, char):
        if self.state == 'q0':
            if char == '0':
                self.complement += '1'
            elif char == '1':
                self.complement += '0'
            else:
                self.state = 'q2'  # Estado de rechazo si encuentra un símbolo no binario

    def process_string(self, input_string):
        for char in input_string:
            self.transition(char)
            if self.state == 'q2':  # Estado de rechazo
                return None
        return self.complement

def compute_complement(input_string):
    pda = PDA()
    return pda.process_string(input_string)

# Prueba
input_string = "101100101010"
complement = compute_complement(input_string)
if complement is not None:
    print(f"El complemento de la cadena '{input_string}' es '{complement}'.")
else:
    print("La cadena contiene caracteres no válidos.")



