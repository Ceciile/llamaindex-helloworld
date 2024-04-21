from dotenv import load_dotenv
import os
load_dotenv()

if __name__ == '__main__' :
    print("Going to ingest pinecode doc...")
    print(f"{os.environ['P_KEY']}")