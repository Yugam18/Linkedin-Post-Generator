# LinkedIn Post Generator

Generate professional LinkedIn posts from any article URL using Gemini AI, with a beautiful Streamlit interface.

## Features
- Enter any article URL and generate a concise, professional LinkedIn post.
- Modern, user-friendly UI with clear input and output areas.
- Posts are tailored for engagement, including hashtags and a call-to-action.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd linkedin-post-generator
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:
```bash
pip install -r requirements.txt
```
Or, if `requirements.txt` is not present:
```bash
pip install streamlit requests
```

### 3. Set Your Gemini API Key
Open `app.py` and set your Gemini API key:
```python
API_KEY = 'your-gemini-api-key-here'
```
> **Note:** Never commit your API key to public repositories.

### 4. Run the App
```bash
streamlit run app.py
```

The app will open in your browser. Enter an article URL and click "Generate LinkedIn Post" to get your post!

## Example Usage
```
$ streamlit run app.py
# In the browser, enter: https://example.com/article
# Click 'Generate LinkedIn Post' to see your result.
```

## Security Note
- Keep your API key private. Do not share or commit it to public repositories.
- This app uses the Gemini API and may incur costs depending on your usage and API plan.

---

Enjoy generating LinkedIn posts effortlessly! 