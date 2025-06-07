
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    while eleccion not in opciones:
        print(f"Opción no valida, vuelve a intentarlo. Las opciones son:  {opciones}"  )
        eleccion = input("""Ingresa una opción valida 
        >""" )
   
    return eleccion
        ##########################################################################


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
