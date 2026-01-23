# Herramienta de Ciberseguridad: Analizador y Generador de Passwords
# Creado por: Samuel Martinez
# Versión: 1.0

import random
import string

def analizar_fuerza(password):
    """
    Analiza qué tan segura es una contraseña basándose en reglas de complejidad.
    Retorna un puntaje y un mensaje.
    """
    puntaje = 0
    feedback = []

    # 1. Regla de Longitud (Mínimo 8, ideal 12+)
    if len(password) < 8:
        feedback.append("❌ Muy corta (Mínimo 8 caracteres)")
    elif len(password) >= 12:
        puntaje += 2
        feedback.append("✅ Buen tamaño")
    else:
        puntaje += 1
        feedback.append("⚠️ Tamaño aceptable")

    # 2. Regla de Variedad (Mayúsculas, Minúsculas, Números, Símbolos)
    tiene_mayus = any(c.isupper() for c in password)
    tiene_minus = any(c.islower() for c in password)
    tiene_nums  = any(c.isdigit() for c in password)
    tiene_simb  = any(c in string.punctuation for c in password)

    if tiene_mayus: puntaje += 1
    else: feedback.append("💡 Agrega MAYÚSCULAS")
    
    if tiene_minus: puntaje += 1
    else: feedback.append("💡 Agrega minúsculas")
    
    if tiene_nums:  puntaje += 1
    else: feedback.append("💡 Agrega números")
    
    if tiene_simb:  puntaje += 1
    else: feedback.append("💡 Agrega símbolos (!@#$)")

    return puntaje, feedback

def generar_password(longitud=12):
    """Genera una contraseña fuerte aleatoria."""
    # Combinamos todas las letras, números y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Creamos la contraseña eligiendo caracteres al azar
    password = "".join(random.choice(caracteres) for i in range(longitud))
    return password

def main():
    print("========================================")
    print("🔐 SISTEMA DE SEGURIDAD DE CONTRASEÑAS")
    print("========================================")
    
    while True:
        print("\nSelecciona una opción:")
        print("1. Analizar una contraseña")
        print("2. Generar una contraseña segura")
        print("3. Salir")
        
        opcion = input(">>> ")

        if opcion == "1":
            user_pass = input("\nIngresa la contraseña a analizar: ")
            score, mensajes = analizar_fuerza(user_pass)
            
            print(f"\n--- RESULTADO (Puntaje: {score}/6) ---")
            for msg in mensajes:
                print(msg)
                
            if score < 4:
                print("\n⚠️ CONCLUSIÓN: Esta contraseña es DÉBIL y hackeable.")
            elif score < 6:
                print("\n👍 CONCLUSIÓN: Es una contraseña DECENTE.")
            else:
                print("\n🔥 CONCLUSIÓN: ¡EXCELENTE! Es una contraseña MUY FUERTE.")

        elif opcion == "2":
            try:
                largo = int(input("\n¿De cuántos caracteres la quieres? (Recomendado 12): "))
                nueva_pass = generar_password(largo)
                print(f"\n✅ Tu nueva contraseña segura es:  {nueva_pass}")
                print("¡Cópiala y guárdala en un lugar seguro!")
            except ValueError:
                print("❌ Error: Ingresa solo números para la longitud.")

        elif opcion == "3":
            print("Cerrando sistema... Mantente seguro. 👋")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
main()

# Módulo principal de criptografía y validación de contraseñas 