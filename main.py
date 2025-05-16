from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Función para conectar a la base de datos
def get_connection():
    try:
        connection = psycopg2.connect(
            dbname="sistema_recargas_viajes",
            user="admin",
            password="Pass!__2025!",
            host="149.130.169.172",
            port="33333"
        )
        return connection
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None

# 1. Total de usuarios
@app.get("/users/count")
def get_total_users():
    conn = get_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuarios;")
        total = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return {"total_users": total}
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        return {"error": "Error al ejecutar la consulta SQL"}

# 2. Usuarios con tarjeta activa
@app.get("/users/active/count")
def get_active_users():
    conn = get_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(DISTINCT u.usuario_id)
            FROM usuarios u
            INNER JOIN tarjetas t ON u.usuario_id = t.usuario_id
            WHERE t.estado = 'Activa';
        """)
        total = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return {"total_users_active": total}
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        return {"error": "Error al ejecutar la consulta SQL"}

# 3. Último usuario registrado
@app.get("/users/latest")
def get_latest_user():
    conn = get_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT usuario_id, nombres || ' ' || apellidos AS nombre_completo
            FROM usuarios
            ORDER BY fecha_registro DESC
            LIMIT 1;
        """)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return {"usuario_id": result[0], "nombre_completo": result[1]}
        else:
            return {"message": "No hay usuarios registrados"}
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        return {"error": "Error al ejecutar la consulta SQL"}

# 4. Total de viajes
@app.get("/trips/total")
def get_total_trips():
    conn = get_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM viajes;")
        total = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return {"total_trips": total}
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        return {"error": "Error al ejecutar la consulta SQL"}

# 5. Ingresos totales
@app.get("/finance/revenue")
def get_total_revenue():
    conn = get_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(monto) FROM viajes;")
        total = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return {"total_revenue": total}
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        return {"error": "Error al ejecutar la consulta SQL"}

