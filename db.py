import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="web_scraping_db",
        user="postgres",
        password="Kv@9063321",
        host="localhost",
        port="5432"
    )
