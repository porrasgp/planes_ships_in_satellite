# app.py
import os
import boto3
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = "computervisionairplaneandships"
PREFIXES = ["airplanes/planesnet/planesnet", "Ships/shipsnet/shipsnet"]

def process_images():
    s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

    for prefix in PREFIXES:
        objects = s3.list_objects(Bucket=BUCKET_NAME, Prefix=f"{prefix}/")["Contents"]
        
        for obj in objects:
            key = obj["Key"]
            image_object = s3.get_object(Bucket=BUCKET_NAME, Key=key)
            image_data = image_object['Body'].read()
            image = Image.open(BytesIO(image_data))

            # Aquí puedes realizar tu lógica de machine learning con la imagen
            # Por ejemplo, podrías utilizar bibliotecas como TensorFlow o PyTorch para el procesamiento.

            # Ejemplo: Imprimir las dimensiones de la imagen
            print(f"Dimensiones de la imagen {key}: {image.size}")

if __name__ == "__main__":
    process_images()

