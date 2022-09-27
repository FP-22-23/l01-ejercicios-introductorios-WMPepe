import calificaciones


a = calificaciones.SolicitudAET()
print(calificaciones.CalcularNota(a[0],a[1],a[2]))
print(calificaciones.calcula_nota_evaluacion_continua(calificaciones.SolicitarCuestionario(),calificaciones.SolicitarParciales(),calificaciones.SolicitarProyectos()))



