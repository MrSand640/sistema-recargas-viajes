DEPLOYMENT.md - Guía de Despliegue de la API REST
1. Requisitos Previos
Antes de comenzar, asegúrate de tener disponible lo siguiente:
•	Python 3.10+ instalado en tu entorno Linux.
•	Acceso a la máquina virtual s-viloria-api, donde se ejecutará la API.
•	Acceso de red a la base de datos PostgreSQL desplegada en s-viloria-db.
•	Git para clonar el repositorio.
________________________________________
2. Instalación del Proyecto
a. Clonar el Repositorio
Primero, clona el repositorio desde GitHub en la máquina s-viloria-api:
bash
CopiarEditar
git clone https://github.com/tu-usuario/sistema-recargas-api.git
cd sistema-recargas-api
b. Crear y activar un entorno virtual
bash
CopiarEditar
python3 -m venv venv
source venv/bin/activate
c. Instalar dependencias
bash
CopiarEditar
pip install fastapi uvicorn psycopg2
________________________________________

3. Configuración de Conexión a la Base de Datos
La API está preconfigurada para conectarse a la base de datos con los siguientes valores:
yaml
CopiarEditar
HOST:     149.130.169.172
PORT:     33333
DB NAME:  sistema_recargas_viajes
USER:     admin
PASS:     Pass!__2025!
________________________________________
4. Ejecución del Servidor API
Desde el directorio raíz del proyecto (donde está el archivo main.py), ejecuta:
bash
CopiarEditar
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Asegúrate de tener habilitado el reenvío de puertos (por ejemplo, 8000) si vas a acceder desde fuera de la VM.
________________________________________
5. Acceder a la API
puedes acceder a la documentación interactiva en:
bash
CopiarEditar
http://localhost:8000/docs
O si estás accediendo remotamente (por ejemplo, desde tu host físico o navegador externo):
arduino
CopiarEditar
http://[IP_PUBLICA_VM_API]:8000/docs
________________________________________
6. Endpoints disponibles
Endpoint	Descripción
/users/count	Retorna el total de usuarios registrados
/users/active/count	Usuarios con al menos una tarjeta activa
/users/latest	Último usuario registrado (nombre completo e ID)
/trips/total	Cantidad total de viajes realizados
/finance/revenue	Total de ingresos recaudados por los viajes
