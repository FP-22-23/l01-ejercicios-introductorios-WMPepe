def CalcularNota(aciertos, errores, total):
    return max(((aciertos*10)/total)-((errores*10)/50-total), 0)

def calcula_nota_cuatrimestre(c1,c2,c3,p,pry):
    if pry >=5:
        return 0.1*(c1+c2+c3)+0.6*p+0.1*pry
    else:
        return 3

def NotaContinua(cuestionarios,parciales,proyectos):
    nota1 = 0.1*(cuestionarios[0]+cuestionarios[1]+cuestionarios[2]) + 0.6 * parciales[0] + 0.1*proyectos[0] 
    nota2 = 0.1*(cuestionarios[3]+cuestionarios[4]+cuestionarios[5]) + 0.6 * parciales[1] + 0.1*proyectos[1] 
    if nota1 >=4 and nota2 >=4:
        return (nota1+nota2)/2
    else: return 4

def SolicitudAET():
    aciertos = int(input("Introduce tus aciertos: "))
    errores = int(input("Introduce tus errores: "))
    total= int(input("Introduce el total: "))
    return aciertos,errores,total

def SolicitarCuestionario():
    c1 = int(input("Introduce tu nota de Cuestionario 1: "))
    c2 = int(input("Introduce tu nota de Cuestionario 2: "))
    c3 = int(input("Introduce tu nota de Cuestionario 3: "))
    c4 = int(input("Introduce tu nota de Cuestionario 4: "))
    c5 = int(input("Introduce tu nota de Cuestionario 5: "))
    c6 = int(input("Introduce tu nota de Cuestionario 6: "))
    return c1,c2,c3,c4,c5,c6

def SolicitarParciales():
    p1 = int(input("Introduce tu nota de Parcial 1: "))
    p2 = int(input("Introduce tu nota de Parcial 2: "))
    return p1,p2

def SolicitarProyectos():
    pry1 = int(input("Introduce tu nota del Proyecto 1: "))
    pry2 = int(input("Introduce tu nota del Proyecto 2: "))
    return pry1,pry2