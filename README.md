Gemini generated readme.txt

# Local Text2SQL with Ollama, DuckDB, and DVD Rental Database

This project demonstrates a local Text-to-SQL system, allowing you to query a PostgreSQL database (specifically the publicly available DVD Rental database) using natural language. It leverages:

* **Ollama hosting duckdb-nsql:** For locally hosted Large Language Models (LLMs) to translate natural language into SQL queries.
* **Streamlit:** For a user-friendly web interface.
* **PostgreSQL for hosting dvdrental database

## Features

* Natural language querying of the DVD Rental PostgreSQL database.
* Locally hosted LLM for privacy and control.
* Fast query execution with DuckDB.
* Simple and intuitive Streamlit web interface.

## Prerequisites

1.  **Ollama:**
    * Install Ollama from [ollama.ai](https://ollama.ai/).
    * Pull your desired LLM model (e.g., `ollama pull llama2`).
2.  **Python 3.x:**
    * Ensure Python 3.x is installed.
3.  **Required Python Libraries:**
    * Install the necessary libraries using pip:


    pip install streamlit langchain duckdb duckdb-nsql psycopg2-binary
  

4.  **DVD Rental Database:**
    * Download the DVD Rental database dump. You can find this database online by searching for "PostgreSQL DVD Rental Database".
    * Restore the database to a local postgres instance, or convert it to a duckDB database. You can convert the database to a DuckDB database by using the following code.
 

## Setup and Usage

1.  **Clone the Repository:**
    * Clone this repository to your local machine.
2.  **Place your DuckDB database:**
    * Place your `dvdrental.duckdb` file in the same directory as the python scripts.
3.  **Run the Streamlit Application:**
    * Execute the Streamlit application:
 
    streamlit run text2sql.py


4.  **Interact with the Application:**
    * Open the Streamlit application in your web browser.
    * Enter your natural language query in the input field.e.g. "Get a list of films title and description longer than 120 minutes."
    * The application will generate the SQL query, execute it using DuckDB locally hosted on PostgreSQL server DVD Rental database schema, and display the results.

## Code Overview

* **`text2sql.py`:**
    * Contains the Streamlit application logic.
    * Sets up the LangChain integration with Ollama.
    * Defines the prompt for the LLM to generate SQL queries.
    * Connects to the DuckDB database.
    * Executes the generated SQL queries and displays the results.

* **DuckDB:**
    * Uses DuckDB with the `nsql` extension to execute the generated SQL queries.
    * Provides efficient in-memory query execution.

## Example Usage

1.  Open the Streamlit app.
2.  Enter a query like: "What are the names of all the actors?"
3.  The app will display the results from the database.

## Customization

* **LLM Model:**
    * Change the llama 3.2 model by modifying the `model`
* **Database Schema:**
    * Adapt the prompt and potentially the code to work with different database schemas, defined in schema.txt
* **Streamlit UI:**
    * Customize the Streamlit interface to enhance the user experience.

## Limitations

* The accuracy of SQL query generation depends on the LLM's capabilities and the prompt engineering.
* Complex queries may require more advanced prompt engineering or LLM capabilities.
* Local LLM performance is dependant on local hardware.
  
