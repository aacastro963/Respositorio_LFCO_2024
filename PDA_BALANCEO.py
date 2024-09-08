from nltk import CFG

# Definimos la Gramática para el balanceo de paréntesis 
grammar = CFG.fromstring("""
    S -> '(' S ')' S | ''
    """)

# Función para verificar si una cadena de paréntesis está balanceada
def check_balance(string):
    stack = []
    
    # Recorremos cada caracter en la cadena
    for char in string:
        if char == '(':
            stack.append(char)  # Añadir a la pila si es un paréntesis de apertura
        elif char == ')':
            if not stack:
                return False  # Si la pila está vacía, significa que hay un paréntesis de cierre sin su par
            stack.pop()  # Retirar el paréntesis de apertura correspondiente
    
    # Si la pila está vacía, la cadena está balanceada
    return len(stack) == 0

# Ejemplos de Cadenas 
strings = [
    "(())",
    "(()())",
    "(()))",
    "(()",
    ""
]                 

# Imprimimos el resultado
for string in strings:
    result = check_balance(string)
    print(f"'{string}': {'Balanceado' if result else 'No Balanceado'}")

#Para Palindromo
if __name__ == '__main__':
    palindromo = lambda string: string==string[::-1]
    print(palindromo('01010001111110001010'))
    
#El problema era el chatParser del NLTK porque el parser espera trabajar con cadenas tokenizadas
#y el chatParser no tokeniza bien cadenas de parentesis vacios o no vacias. Para solucionar esto
#hice una implementacion directa de verifucacion de balanceos usando una pila Si al final la pila 
# está vacía, significa que todos los paréntesis de apertura tienen un paréntesis de cierre 
# correspondiente, por lo tanto, la cadena está balanceada.
