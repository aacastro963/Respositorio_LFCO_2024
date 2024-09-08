
def balanceo_parentesis(cadena):
    valor_stack = []
    parentesis = {'(': ')'}

    for c in cadena:
        if c in parentesis:
            valor_stack.append(c)
        elif len(valor_stack) == 0 or c != parentesis[valor_stack.pop()]:
            return False
    return len(valor_stack) == 0


if __name__ == '__main__':
    print(balanceo_parentesis('(())()(())'))
    #print(balanceo_parentesis(''))
    #print(balanceo_parentesis(''))
