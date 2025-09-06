# 🚗 Motor Vehicle Act AI Assistant

A modern, AI-powered assistant for querying the Motor Vehicle Act of India with a beautiful neon purple dark theme UI.

## ✨ Features

- **Modern Neon Purple UI**: Beautiful dark theme with neon purple accents and animations
- **AI-Powered Responses**: Uses Ollama LLM for intelligent legal assistance
- **Vector Search**: Powered by Qdrant for semantic search through Motor Vehicle Act documents
- **Real-time Streaming**: Streaming responses for better user experience
- **Chat History**: Keeps track of your recent queries
- **Responsive Design**: Modern, mobile-friendly interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Ollama running locally on port 11434
- Qdrant cloud account with Motor Vehicle Act data uploaded

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd workshop_RAG
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
```

4. Make sure Ollama is running:
```bash
ollama serve
ollama pull llama3.2:latest
```

### Running the Application

#### Streamlit UI (Recommended)
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

#### Command Line Interface
```bash
python retrieve.py
```

## 🎨 UI Features

- **Animated Background**: Floating particles for visual appeal
- **Glowing Effects**: Text and buttons with neon glow animations
- **Gradient Animations**: Dynamic color transitions
- **Modern Typography**: Orbitron and Rajdhani fonts
- **Responsive Layout**: Works on all screen sizes
- **Dark Theme**: Easy on the eyes with neon purple accents

## 📁 Project Structure

```
workshop_RAG/
├── app.py              # Streamlit UI application
├── retrieve.py         # Command-line interface
├── upload.py           # Data upload script
├── response.py         # LLM response handler
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── data/              # PDF documents
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

- `QDRANT_URL`: Your Qdrant cloud instance URL
- `QDRANT_API_KEY`: Your Qdrant API key

### Ollama Configuration

Make sure you have the following model installed:
```bash
ollama pull llama3.2:latest
```

## 🎯 Usage

1. Launch the Streamlit app
2. Enter your question about the Motor Vehicle Act
3. Click the "🚀 ASK" button
4. View the AI-generated response based on the legal documents
5. Check your chat history for previous queries

## 🛠️ Troubleshooting

### Common Issues

1. **Ollama Connection Error**: Make sure Ollama is running on localhost:11434
2. **Qdrant Connection Error**: Check your API key and URL in the .env file
3. **Missing Dependencies**: Run `pip install -r requirements.txt`

### Support

If you encounter any issues, please check:
- Ollama is running and accessible
- Environment variables are correctly set
- All dependencies are installed

## 🎨 Customization

The UI theme can be customized by modifying the CSS in `app.py`. Key color variables:
- Primary: `#8a2be2` (Blue Violet)
- Secondary: `#ff00ff` (Magenta)
- Accent: `#da70d6` (Orchid)

## 📝 License

This project is open source and available under the MIT License.
