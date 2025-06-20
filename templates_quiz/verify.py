import preguntas as p


def verificar(pregunta, eleccion):
    #devuelve el índice de elección dada
    letras = ['a', 'b', 'c', 'd']
    indice = letras.index(eleccion)    

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    alternativa_usuario = pregunta["alternativas"][indice]
    correcta = alternativa_usuario[1]

    if correcta == 1:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
    
        
    ##########################################################################################


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta, respuesta)






