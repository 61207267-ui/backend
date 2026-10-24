from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración con Autenticación de Windows
# Reemplaza 'NOMBRE_DE_TU_BD' por el nombre real de tu base de datos en SQL Server
SERVER = "(localdb)\MSSQLLocalDB"  # O el nombre de tu servidor/instancia, ej: "localhost\\SQLEXPRESS"
DATABASE = "veterinaria_db"

DATABASE_URL = f"mssql+pyodbc://{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inyección de dependencia para usar la sesión en tus APIs
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()