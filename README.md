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
├── data/
│   └── anime_with_synopsis.csv    # Anime dataset with synopses
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

## Usage

### Running the Application

After completing the installation steps, you can run the anime recommender:

```cmd
# Make sure your virtual environment is activated
# Run the Streamlit application (if available)
streamlit run app.py
```

### Using the Recommender

1. **Input Preferences**: Describe your anime preferences in natural language
2. **Get Recommendations**: The system will analyze your input and suggest similar anime
3. **Explore Results**: Browse through recommended anime with their synopses and ratings

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

## Development

To contribute to this project:

1. Ensure your virtual environment is activated
2. Make your changes
3. Test thoroughly
4. The project is installed in editable mode, so changes are reflected immediately

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
