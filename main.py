import os
from etl.extract import extract_data
from etl.transform import convert_to_grayscale, resize_images, calculate_statistics
from etl.load import load_data_to_db

# File paths
data_path = r'C:\Users\mior\Downloads\full_archive\data.npz'

# DB configuration
db_config = {
    'dbname': 'ct_scan',
    'user': 'user',
    'password': 'password',
    'host': 'localhost',
    'port': 5432
}

# Verify the file path
if not os.path.exists(data_path):
    print(f"File not found: {data_path}")
else:
    print(f"Loading data from: {data_path}")
    # Run ETL process
    data = extract_data(data_path)
    images = convert_to_grayscale(data['image'])
    resized_images = resize_images(images)
    stats = calculate_statistics(resized_images)
    load_data_to_db(resized_images, stats, db_config)
