import ollama
import streamlit as st
import pandas as pd
import psycopg2



class Database:
    def __init__(self,query):
        self.query = query

    def execute_query(self):
        conn = None
        cur = None
        try:

            db_params = {
                "host": "localhost",
                "port": 5432,
                "database": "dvdrental",
                "user": "postgres",
                "password": "password",
            }

            conn = psycopg2.connect(**db_params)

            cur = conn.cursor()
            cur.execute(self.query)
            results = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
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
                print("Database connection is closed.")

class StreamlitApp:
    def __init__(self):
        self.db_metadata = None
        self.text = None
        self.query = None
        with open("./Data/schema.txt",'r') as file:
            self.db_metadata = file.read()
        # st.title("AI")
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
