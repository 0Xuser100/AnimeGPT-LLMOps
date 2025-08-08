# Anime Recommender 🎌

An intelligent anime recommendation system that uses natural language processing and machine learning to suggest anime based on user preferences and synopsis analysis.

## Quick Start

### Clone the Repository
```bash
git clone https://github.com/0Xuser100/AnimeRecommender.git
cd AnimeRecommender
```

### Setup & Run
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -e .

# Run the application
streamlit run app/app.py
```

## Features

- 🎯 **Personalized Recommendations**: AI-powered anime suggestions based on your preferences
- 🔍 **Smart Search**: Semantic similarity matching using vector embeddings
- 🚀 **Interactive Interface**: User-friendly Streamlit web application
- 🤖 **Advanced AI**: Powered by Groq LLM and Hugging Face transformers
- 📊 **Vector Database**: ChromaDB for efficient similarity search

## How It Works

1. **Describe your preferences** in natural language (e.g., "light-hearted school anime")
2. **AI analyzes** your request against anime synopses using vector similarity
3. **Get 3 personalized recommendations** with detailed explanations

## Prerequisites

- Python 3.12+
- Git

## Configuration

Create a `.env` file in the project root and add your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
```

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

## Usage Examples

Try these sample queries:
- "light hearted anime with school settings"
- "dark fantasy anime with complex storylines"  
- "romantic comedy anime similar to Your Name"
- "action anime with supernatural powers"

## Tech Stack

- **LangChain**: LLM application framework
- **ChromaDB**: Vector database for similarity search  
- **Streamlit**: Web application interface
- **Groq**: Fast LLM inference
- **Hugging Face**: Text embeddings

## Troubleshooting

**Common Issues:**
- **Missing API key**: Add `GROQ_API_KEY` to your `.env` file
- **Import errors**: Ensure virtual environment is activated
- **Installation fails**: Upgrade pip: `python -m pip install --upgrade pip`

## Author

**Mahmoud Abdulhamid**

## License

This project is open source. Please check the license file for more details.

---

*Happy anime discovering! 🎌*
