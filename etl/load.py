import psycopg2
import numpy as np

def load_data_to_db(images, stats, db_config):
    conn = psycopg2.connect(
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        image BYTEA
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stats (
        id SERIAL PRIMARY KEY,
        mean FLOAT,
        median FLOAT,
        std FLOAT
    );
    """)

    for img in images:
        cursor.execute("INSERT INTO images (image) VALUES (%s)", (psycopg2.Binary(img.tobytes()),))

    # Convert numpy data types to native Python data types
    mean, median, std = stats
    cursor.execute("INSERT INTO stats (mean, median, std) VALUES (%s, %s, %s)", (float(mean), float(median), float(std)))
    
    conn.commit()
    cursor.close()
    conn.close()
