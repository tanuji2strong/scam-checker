import os
import mysql.connector
import json
from dotenv import load_dotenv


load_dotenv()

def save_check(message,result):
    try:
        conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        )
        cursor=conn.cursor()

        sql = "INSERT INTO checks (message, risk, scam_type, red_flags, judge) VALUES (%s, %s, %s, %s, %s)"
        values = (message, result["risk"], result["scam_type"], json.dumps(result["red_flags"],ensure_ascii=False), result["judge"])
        cursor.execute(sql,values)
        conn.commit()
        new_id=cursor.lastrowid
        conn.close()
        return new_id
    except Exception as e:
        print("save failed:", e)
        return None
if __name__ == "__main__":
    fake = {"risk": "low", "scam_type": "none", "red_flags": [], "judge": "keyword"}
    print(save_check("test message", fake))
