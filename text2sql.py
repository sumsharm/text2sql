import ollama
import streamlit as st
from PIL import Image
import psycopg2
import pandas as pd


class Database:
    def __init__(self,query):
        self.query = query

    def execute_query(self):
        conn = None
        cur = None
        try:
            # 1. Connection Parameters
            db_params = {
                "host": "localhost",  # Or your PostgreSQL server's hostname/IP
                "port": 5432,  # Default PostgreSQL port
                "database": "dvdrental",
                "user": "postgres",
                "password": "password",
            }
            # 2. Establish Connection
            conn = psycopg2.connect(**db_params)
            # 3. Create a Cursor
            cur = conn.cursor()
            # 4. Execute a Query (Example: SELECT)
            cur.execute(self.query)
            # 5. Fetch Results
            results = cur.fetchall()  # Fetch all rows
            columns = [desc[0] for desc in cur.description]  # Get column names
            df = pd.DataFrame(results, columns=columns)
            st.dataframe(df)

        except psycopg2.Error as e:
            print(f"Database error: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
                print("Database connection closed.")

class StreamlitApp:
    def __init__(self):
        self.db_metadata = None
        self.text = None
        self.query = None
        with open("./Data/schema.txt",'r') as file:
            self.db_metadata = file.read()
        # st.title("AI")
        image = Image.open("./resource/urban-outfitter.png")
        st.markdown("<div style='text-align: right;'></div>", unsafe_allow_html=True)
        st.image(image, use_container_width=False, width=200)
        text2sql = st.text_input("How Can I Help?")
        self.query = self.get_query(text2sql)
        if st.button("Execute Query"):
            Database(self.query).execute_query()


    def get_query(self,text2sql):
        responses = ollama.generate(
            model="duckdb-nsql:latest",
            system=self.db_metadata,
            prompt=text2sql
        )
        llm_query = responses["response"]
        st.write(llm_query)
        return llm_query

StreamlitApp()

# print(responses["response"])
# st.stop()
