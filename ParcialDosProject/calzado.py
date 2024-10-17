sala=int
nuevosalario=int
#funcion para calcular el cargo
def calcularempleado(empleado,salario,desempeno,nuevosalario,sala):
    if empleado=='directivo':
        desempeno=='alto'
        sala==salario*0.20
        nuevosalario==sala+salario
    elif empleado=='directivo':
        desempeno=='medio'
        sala==salario*0.10
        nuevosalario==sala+salario
    elif empleado == 'directivo':
        sala==0
        desempeno == 'bajo'
        nuevosalario == salario
    elif empleado=='operativo':
        desempeno=='alto'
        sala==salario*0.15
        nuevosalario==sala+salario
    elif empleado=='operativo':
        desempeno=='medio'
        sala==salario*0.05
        nuevosalario==sala+salario
    elif empleado == 'operativo':
        sala==0
        desempeno == 'bajo'
        nuevosalario == salario
    elif empleado=='auxiliar':
        sala==0
        desempeno=='bajo'
        nuevosalario==salario
    else:
        return None

def generar_mensaje(empleado, desempeno, salario, sala, nuevosalario):
        return (f"----Resumen de pago-------"
                f"Cargo:{empleado}\n"
                f"Nivel de Desempeño: ${desempeno}\n"
                f"Salario: {salario}\n"
                f"bonificacion: ${sala}\n"
                f"Total a recibir: ${nuevosalario}\n"
                f"-----------------------------------")


#Entradas
empleado=(input("Cargo empleado: "))
desempeno=(input("Nivel desempeño: "))
salario=int(input("Salario base Mensual $: "))



