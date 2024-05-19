# Recipe Generation API with RAG Model
![Project Logo](media/menu.png)
## Explanation
This project is a Recipe Generation API that utilizes a Retrieval-Augmented Generation (RAG) model to generate detailed recipes based on user input. The API allows users to input a desired recipe idea (e.g., "pancakes recipe") and returns a complete recipe by querying a vector database (faiss), retrieving relevant information, and processing it through a BART model.

## What does the API include?

### Recipe Generation Process
1. **Query Encoding**: The user's recipe idea is encoded into a query vector.
2. **Top-K Retrieval**: The encoded query is used to find the top-k relevant entries from the vector database.
3. **Context Encoding**: The retrieved top-k entries are decoded and then re-encoded into the BART model vector format.
4. **Recipe Generation**: The BART model processes the encoded context to generate a detailed recipe.
5. **Result Decoding**: The final generated recipe is decoded and returned to the user.

## Dataset and Vector Database Preparation
To avoid building the vector database each time the API runs, a Jupyter notebook is provided. This notebook performs all necessary preprocessing steps, including:
- Preparing the dataset.
- Building and saving the vector database (faiss).

The API reads the pre-built vector database and dataset from files, ensuring efficient and quick responses.

## Running the API

### Prerequisites
- Ensure you have Python and necessary libraries installed.

### Steps to Run

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/recipe-generation-api.git
    cd recipe-generation-api
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the Dataset and Vector Database**:
    - Open the provided Jupyter notebook (`prepare_data.ipynb`).
    - Follow the instructions to preprocess the dataset and build the vector database.
    - Save the generated files in the appropriate directory.

4. **Run the API**:
    ```bash
    python run.py
    ```
5. **Open Swagger UI**\
The API will be accessible at `http://127.0.0.1:5000/apidocs/` by default


## Demo

![Demo GIF](media/demo.gif)
