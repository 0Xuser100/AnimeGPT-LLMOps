# Anime Recommender

An intelligent anime recommendation system that uses natural language processing and machine learning to suggest anime based on user preferences and synopsis analysis.

## Project Overview

This project leverages advanced NLP techniques including:
- **LangChain** for building language model applications
- **ChromaDB** for vector database storage and similarity search
- **Sentence Transformers** for semantic text embeddings
- **Streamlit** for creating an interactive web interface
- **Groq** and **Hugging Face** integrations for enhanced language model capabilities

The system analyzes anime synopses and user preferences to provide personalized recommendations using semantic similarity matching.

## Features

- 🎯 Personalized anime recommendations based on user preferences
- 📊 Synopsis-based similarity matching using advanced embeddings
- 🚀 Interactive web interface built with Streamlit
- 🔍 Vector-based search using ChromaDB
- 🤖 Integration with modern language models (Groq, Hugging Face)

## Prerequisites

- Python 3.12 or higher
- Git (for cloning the repository)

## Installation and Setup

### Step 1: Download Python 3.12

1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download Python 3.12 or the latest version
3. Run the installer and make sure to check "Add Python to PATH" during installation
4. Verify installation by opening Command Prompt and running:
   ```cmd
   python --version
   ```

### Step 2: Clone or Download the Project

If you haven't already, download or clone this project to your local machine.

### Step 3: Create Virtual Environment

Navigate to the project directory and create a virtual environment:

```cmd
cd d:\LLMOPS\AnimeRecommender
python -m venv venv
```

### Step 4: Activate Virtual Environment

Activate the virtual environment:

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### Step 5: Install Project Dependencies

Install the project in development mode along with all required libraries:

```cmd
pip install -e .
```

This command will:
- Install the project package in editable mode
- Automatically install all dependencies listed in `requirements.txt`
- Set up the project for development

## Project Structure

```
AnimeRecommender/
├── app/
│   ├── __init__.py
│   └── app.py                     # Streamlit web application
├── config/
│   ├── __init__.py
│   └── config.py                  # Configuration and environment variables
├── data/
│   └── anime_with_synopsis.csv    # Anime dataset with synopses
├── pipeline/
│   ├── __init__.py
│   └── pipeline.py                # Main recommendation pipeline
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # CSV data loading and processing
│   ├── prompt_template.py         # LLM prompt templates
│   ├── recommender.py             # Core recommendation logic
│   └── vector_store.py            # Vector database operations
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py        # Custom exception handling
│   └── logger.py                  # Logging configuration
├── Anime_Recommend.egg-info/      # Package metadata
├── requirements.txt               # Project dependencies
├── setup.py                      # Package setup configuration
├── .env                          # Environment variables (API keys)
└── README.md                     # This file
```

## Configuration

1. Create or update the `.env` file in the project root directory
2. Add your API keys for external services:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   ```

## Code Architecture & Detailed Explanation

### Core Components

#### 1. Configuration Management (`config/config.py`)
```python
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME="llama-3.1-8b-instant"
```
- **Purpose**: Centralized configuration management
- **Functionality**: Loads environment variables from `.env` file and provides API key and model configuration
- **Dependencies**: `python-dotenv` for environment variable loading

#### 2. Data Processing (`src/data_loader.py`)
```python
class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv , encoding='utf-8' , on_bad_lines='skip').dropna()
        # Validates required columns: Name, Genres, sypnopsis
        # Creates combined_info field for vector embedding
```
- **Purpose**: Handles CSV data loading, cleaning, and preprocessing
- **Key Features**:
  - Validates required columns (`Name`, `Genres`, `sypnopsis`)
  - Combines anime information into a single text field for embedding
  - Handles encoding issues and bad lines gracefully
  - Outputs processed data ready for vector store creation

#### 3. Vector Store Management (`src/vector_store.py`)
```python
class VectorStoreBuilder:
    def __init__(self,csv_path:str,persist_dir:str="chroma_db"):
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

    def build_and_save_vectorestore(self):
        # Creates vector embeddings from CSV data
        # Stores in ChromaDB for similarity search
        
    def load_vector_store(self):
        # Loads existing vector store from disk
```
- **Purpose**: Creates and manages vector embeddings for semantic search
- **Key Technologies**:
  - **HuggingFace Embeddings**: Uses `all-MiniLM-L6-v2` model for text embeddings
  - **ChromaDB**: Vector database for storing and querying embeddings
  - **LangChain**: Document loading and text splitting
- **Workflow**:
  1. Loads CSV data using LangChain's CSVLoader
  2. Splits text into chunks for better embeddings
  3. Creates vector embeddings using sentence transformers
  4. Stores vectors in ChromaDB with persistence

#### 4. Recommendation Engine (`src/recommender.py`)
```python
class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            chain_type = "stuff",
            retriever = retriever,
            return_source_documents = True,
            chain_type_kwargs = {"prompt":self.prompt}
        )
```
- **Purpose**: Core recommendation logic using RAG (Retrieval-Augmented Generation)
- **Architecture**:
  - **LLM Integration**: Uses Groq's Llama-3.1-8b-instant model
  - **RAG Pipeline**: Combines vector similarity search with LLM generation
  - **Chain Type**: "stuff" chain type for document-based Q&A
- **Process**:
  1. Retriever finds similar anime based on user query
  2. LLM generates personalized recommendations using retrieved context
  3. Returns structured recommendations with explanations

#### 5. Prompt Engineering (`src/prompt_template.py`)
```python
def get_anime_prompt():
    template = """
You are an expert anime recommender...
For each question, suggest exactly three anime titles. For each recommendation, include:
1. The anime title.
2. A concise plot summary (2-3 sentences).
3. A clear explanation of why this anime matches the user's preferences.
"""
```
- **Purpose**: Defines structured prompts for consistent LLM responses
- **Features**:
  - Expert persona establishment
  - Structured output format (exactly 3 recommendations)
  - Required information per recommendation
  - Context and question variables for dynamic content

#### 6. Pipeline Integration (`pipeline/pipeline.py`)
```python
class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        vectore_builder=VectorStoreBuilder(csv_path="",persist_dir=persist_dir)
        retriever=vectore_builder.load_vector_store().as_retriever()
        self.recommender=AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)
```
- **Purpose**: Orchestrates the entire recommendation workflow
- **Integration Points**:
  - Loads vector store and creates retriever
  - Initializes recommender with LLM configuration
  - Provides single interface for recommendation queries
- **Error Handling**: Comprehensive logging and custom exception handling

#### 7. Web Application (`app/app.py`)
```python
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

st.title("Anime Recommender System")
query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
```
- **Purpose**: Streamlit-based user interface
- **Features**:
  - Pipeline caching with `@st.cache_resource` for performance
  - Interactive text input for user preferences
  - Loading spinner for user experience
  - Markdown rendering for formatted recommendations

#### 8. Utilities

##### Logging (`utils/logger.py`)
- **Daily log files**: Creates date-based log files in `logs/` directory
- **Structured logging**: Timestamp, level, and message formatting
- **Application-wide**: Used across all components for debugging and monitoring

##### Exception Handling (`utils/custom_exception.py`)
- **Detailed error tracking**: Captures file, line number, and error details
- **Consistent error format**: Standardized error messages across the application
- **Debug information**: Helps with troubleshooting and maintenance

## Usage

### Running the Application

After completing the installation steps, you can run the anime recommender:

```cmd
# Make sure your virtual environment is activated
# Run the Streamlit application
streamlit run app/app.py

# For auto-reload during development
streamlit run app/app.py --server.runOnSave true
```

### Using the Recommender

1. **Input Preferences**: Describe your anime preferences in natural language
   - Example: "light hearted anime with school settings"
   - Example: "dark fantasy anime with complex storylines"
   - Example: "romantic comedy anime similar to Your Name"

2. **Get Recommendations**: The system will:
   - Search the vector database for similar anime
   - Use LLM to generate personalized recommendations
   - Return exactly 3 recommendations with detailed explanations

3. **Explore Results**: Each recommendation includes:
   - Anime title
   - Plot summary (2-3 sentences)
   - Why it matches your preferences

## Dependencies

The project uses the following main libraries:

- **langchain**: Framework for building LLM applications
- **langchain_community**: Community extensions for LangChain
- **langchain_groq**: Groq integration for LangChain
- **langchain_huggingface**: Hugging Face integration for LangChain
- **chromadb**: Vector database for similarity search
- **streamlit**: Web app framework for ML applications
- **pandas**: Data manipulation and analysis
- **python-dotenv**: Environment variable management
- **sentence-transformers**: Sentence and text embeddings

## Technical Workflow

### 1. Data Flow Architecture
```
User Query → Vector Search → Context Retrieval → LLM Processing → Structured Response
     ↓              ↓              ↓               ↓                ↓
Text Input → Embeddings → Similar Anime → RAG Chain → 3 Recommendations
```

### 2. System Initialization Process
1. **Environment Setup**: Load API keys and configuration from `.env`
2. **Vector Store Loading**: Initialize ChromaDB with pre-computed embeddings
3. **LLM Initialization**: Set up Groq LLM with specified model and parameters
4. **Pipeline Assembly**: Connect retriever, LLM, and prompt template
5. **Web Interface**: Launch Streamlit app with cached pipeline

### 3. Recommendation Generation Process
1. **Query Processing**: User input is processed and embedded
2. **Similarity Search**: Vector database returns most similar anime
3. **Context Assembly**: Retrieved documents are formatted for LLM
4. **LLM Generation**: Groq model generates structured recommendations
5. **Response Formatting**: Output is formatted and displayed to user

### 4. Key Design Patterns
- **Dependency Injection**: Components receive dependencies through constructors
- **Factory Pattern**: Pipeline class orchestrates component creation
- **Template Method**: Prompt templates define consistent LLM behavior
- **Caching Strategy**: Streamlit caching for expensive operations
- **Error Handling**: Custom exceptions with detailed logging

## Development

### Development Workflow

1. **Environment Setup**:
   ```cmd
   # Activate virtual environment
   venv\Scripts\activate
   
   # Install in development mode
   pip install -e .
   ```

2. **Code Changes**: 
   - Make your changes to source files
   - Changes are reflected immediately (editable install)

3. **Testing**: 
   ```cmd
   # Run the application
   streamlit run app/app.py --server.runOnSave true
   ```

4. **Debugging**:
   - Check logs in the `logs/` directory
   - Use custom exception details for error tracking
   - Enable Streamlit debug mode if needed

### Code Quality Guidelines
- Follow existing naming conventions
- Add proper error handling and logging
- Update documentation for new features
- Ensure proper type hints where applicable

## Troubleshooting

### Common Issues

1. **Python not found**: Make sure Python 3.12 is installed and added to PATH
2. **Virtual environment activation fails**: Ensure you're in the correct directory
3. **Package installation errors**: Try upgrading pip first: `python -m pip install --upgrade pip`
4. **Missing API keys**: Check your `.env` file configuration

### Getting Help

If you encounter issues:
1. Check that all installation steps were completed
2. Verify your Python version: `python --version`
3. Ensure virtual environment is activated (you should see `(venv)` in prompt)
4. Try reinstalling dependencies: `pip install -e . --force-reinstall`

## Author

**Mahmoud Abdulhamid**

## License

This project is open source. Please check the license file for more details.

---

*Happy anime discovering! 🎌*
