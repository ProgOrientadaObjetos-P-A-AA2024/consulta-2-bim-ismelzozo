class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad):
        self._nombres = nombres
        self._apellidos = apellidos
        self._identificacion = identificacion
        self._edad = edad

    def establecer_nombres_estudiante(self, nombres):
        self._nombres = nombres

    def establecer_apellido_estudiante(self, apellidos):
        self._apellidos = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self._identificacion = identificacion

    def establecer_edad_estudiante(self, edad):
        self._edad = edad

    def obtener_nombres_estudiante(self):
        return self._nombres

    def obtener_apellido_estudiante(self):
        return self._apellidos

    def obtener_identificacion_estudiante(self):
        return self._identificacion

    def obtener_edad_estudiante(self):
        return self._edad


class EstudianteDistancia(Estudiante):
    pass
    def __init__(self, nombres, apellidos, identificacion, edad, numero_asignaturas=0, costo_asignatura=0.0):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_asignaturas = numero_asignaturas
        self._costo_asignatura = costo_asignatura
        self._matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self._costo_asignatura = valor

    def calcular_matricula_distancia(self):
        self._matricula_distancia = self._numero_asignaturas * self._costo_asignatura

    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura

    def obtener_matricula_distancia(self):
        return self._matricula_distancia


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad, numero_asignaturas=0, costo_asignatura=0.0):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_asignaturas = numero_asignaturas
        self._costo_asignatura = costo_asignatura
        self._matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self._costo_asignatura = valor

    def calcular_matricula_distancia(self):
        self._matricula_distancia = self._numero_asignaturas * self._costo_asignatura

    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura

    def obtener_matricula_distancia(self):
        return self._matricula_distancia

    class EstudiantePresencial(Estudiante):
        def __init__(self, nombres, apellidos, identificacion, edad, numero_creditos=0, costo_credito=0.0):
            super().__init__(nombres, apellidos, identificacion, edad)
            self._numero_creditos = numero_creditos
            self._costo_credito = costo_credito
            self._matricula_presencial = 0.0

        def establecer_numero_creditos(self, numero):
            self._numero_creditos = numero

        def establecer_costo_credito(self, valor):
            self._costo_credito = valor

        def calcular_matricula_presencial(self):
            self._matricula_presencial = self._numero_creditos * self._costo_credito

        def obtener_numero_creditos(self):
            return self._numero_creditos

        def obtener_costo_credito(self):
            return self._costo_credito

        def obtener_matricula_presencial(self):
            return self._matricula_presencial

        if __name__ == "__main__":
            est_distancia = EstudianteDistancia("Luis", "Benitez", "1100909900", 20)
            est_distancia.establecer_numero_asignaturas(5)
            est_distancia.establecer_costo_asignatura(50.5)
            est_distancia.calcular_matricula_distancia()

            print(f"Nombres: {est_distancia.obtener_nombres_estudiante()}")
            print(f"Apellidos: {est_distancia.obtener_apellido_estudiante()}")
            print(f"Identificación: {est_distancia.obtener_identificacion_estudiante()}")
            print(f"Edad: {est_distancia.obtener_edad_estudiante()}")
            print(f"Número de asignaturas: {est_distancia.obtener_numero_asignaturas()}")
            print(f"Costo asignatura: {est_distancia.obtener_costo_asignatura():.2f}")
            print(f"Costo matrícula: {est_distancia.obtener_matricula_distancia():.2f}")