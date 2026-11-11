# SISTEMA ACADEMICO INNOVATION EDUCATION - Abraham Navarrete

estudiantes = []
matriculas = []
notas = []

while True:

    print("\n===== INNOVATION EDUCATION =====")
    print("1. Registrar estudiante")
    print("2. Registrar matricula")
    print("3. Registrar nota")
    print("4. Mostrar estudiantes")
    print("5. Mostrar matriculas")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    # REGISTRAR ESTUDIANTE
    if opcion == "1":

        nombre = input("Ingrese nombre: ").strip()
        codigo = input("Ingrese codigo: ").strip()

        #  revisamos que no dejen los campos vacios
        if nombre == "" or codigo == "":
            print("Error: los campos no pueden estar vacios.")

        # aqui compruebo que no se repita el mismo codigo
        elif any(e["codigo"] == codigo for e in estudiantes):
            print("Error: el codigo ya existe.")

        else:
            estudiantes.append({
                "nombre": nombre,
                "codigo": codigo
            })
            print("Estudiante registrado correctamente.")

    # REGISTRAR MATRICULA
    elif opcion == "2":

        codigo = input("Ingrese codigo: ").strip()
        curso = input("Ingrese curso: ").strip()

        # verifico si el estudiante ya esta registrado
        existe = any(e["codigo"] == codigo for e in estudiantes)

        if not existe:
            print("Error: estudiante no encontrado.")

        elif curso == "":
            print("Error: ingrese un curso.")

        # Evitamos que se matricule dos veces en el mismo curso
        elif any(m["codigo"] == codigo and m["curso"] == curso for m in matriculas):
            print("Error: el estudiante ya esta matriculado.")

        else:
            matriculas.append({
                "codigo": codigo,
                "curso": curso
            })
            print("Matricula registrada correctamente.")

    # REGISTRAR NOTA
    elif opcion == "3":

        codigo = input("Ingrese codigo: ").strip()
        curso = input("Ingrese curso: ").strip()

        # Antes de poner una nota, comprobamos que tenga matricula
        matriculado = any(
            m["codigo"] == codigo and m["curso"] == curso
            for m in matriculas
        )

        if not matriculado:
            print("Error: el estudiante no esta matriculado en este curso.")

        else:
            try:
                nota = float(input("Ingrese nota (0 a 20): "))

                # las notas solamente pueden estar entre 0 y 20
                if nota < 0 or nota > 20:
                    print("Error: la nota debe estar entre 0 y 20.")

                else:
                    notas.append({
                        "codigo": codigo,
                        "curso": curso,
                        "nota": nota
                    })
                    print("Nota registrada correctamente.")

            # aqui no quiereo que ingresen letras sino numeros 
            except ValueError:
                print("Error: debe ingresar un numero.")

    # MOSTRAR ESTUDIANTES
    elif opcion == "4":

        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")

        else:
            print("\nLISTA DE ESTUDIANTES")

            # recorremos la lista para mostrar a todos los estudiantes
            for estudiante in estudiantes:
                print(estudiante["codigo"], "-", estudiante["nombre"])

    # MOSTRAR MATRICULAS
    elif opcion == "5":

        if len(matriculas) == 0:
            print("No hay matriculas registradas.")

        else:
            print("\nLISTA DE MATRICULAS")

            # aqui solo busco mostrar el codigo del alumno + curso
            for matricula in matriculas:
                print(matricula["codigo"], "-", matricula["curso"])

    # SALIR
    elif opcion == "6":
        print("Gracias por utilizar Innovation Education.")
        break

    else:
        print("Error: opcion no valida.")
