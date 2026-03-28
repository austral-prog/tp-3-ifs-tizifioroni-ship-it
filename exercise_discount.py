def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """
    

    precio = float(input())
    cantidad = int(input())

    p_por_q = precio * cantidad
    p_por_q_veinte = p_por_q*0.2
    p_por_q_diez = p_por_q*0.1
    p_por_q_cero = 0.0

    

    if cantidad >= 10:
        print(f"Subtotal: {p_por_q}")
        print("Descuento aplicado: 20%")
        print(f"Monto de descuento: {p_por_q_veinte}")
        print(f"Total final: {p_por_q - p_por_q_veinte}")
    elif 5 <= cantidad <= 9:
        print(f"Subtotal: {p_por_q}")
        print("Descuento aplicado: 10%")
        print(f"Monto de descuento: {p_por_q_diez}")
        print(f"Total final: {p_por_q - p_por_q_diez}")
    else:
        print(f"Subtotal: {p_por_q}")
        print("Descuento aplicado: 0%")
        print(f"Monto de descuento: {p_por_q_cero}")
        print(f"Total final: {p_por_q - p_por_q_cero}")

