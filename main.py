import os
from dotenv import load_dotenv
import time

from etl.extraction import read_user_ids_from_csv
from etl.enrichment import fetch_user_profile
from etl.transform import generate_marketing_message
from etl.load import send_marketing_message

load_dotenv()

def main():
    df = read_user_ids_from_csv(os.getenv("INPUT_CSV"))
    print("Iniciando pipeline...\n")

    for _, row in df.iterrows():
        user_id = int(row["user_id"])
        print(f"Processando usuário {user_id}...")

        profile = fetch_user_profile(user_id)
        message = generate_marketing_message(profile)
        response = send_marketing_message(user_id, message)

        print("Mensagem enviada:", response)
        time.sleep(1)

    print("\nPipeline finalizado!")

if __name__ == "__main__":
    main()
