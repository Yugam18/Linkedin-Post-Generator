import streamlit as st
import requests
import json

API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'
API_KEY = ''
HEADERS = {
    'Content-Type': 'application/json',
    'X-goog-api-key': API_KEY
}
PROMPT_TEMPLATE = (
    "Generate a LinkedIn post summarizing the key insights from the article provided in the URL below. The post should: "
    "\n\n1. Focus on the core problem the article addresses."
    "\n2. Highlight the elegance or simplicity of the solution presented."
    "\n3. Emphasize practical applications in relevant  technology."
    "\n4. Include a call-to-action that encourages discussion or sharing of experiences among professionals in the field."
    "\n5. Add 3-5 relevant hashtags to increase engagement."
    "\n\nThe tone should be professional, insightful, and concise, within the 600-character limit before hashtags. Do not include the article link or author's name in the post."
    "Article URL: {url}"
)

def generate_linkedin_post(url):
    prompt = PROMPT_TEMPLATE.format(url=url)
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "tools": [
            {"url_context": {}}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    result = response.json()
    try:
        post = result["candidates"][0]["content"]["parts"][0]["text"]
        # Remove any summary or extra info before hashtags (if present)
        # The prompt already asks for only the LinkedIn post, but just in case, we can trim if needed
        return post.strip()
    except (KeyError, IndexError):
        return "Failed to extract LinkedIn post from response."

st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼", layout="centered")
st.markdown("""
    <style>
    .main {
        background-color: #f3f6fb;
    }
    .stTextInput>div>div>input {
        font-size: 1.1rem;
        padding: 0.75rem;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #0077b5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 1.1rem;
    }
    .post-box {
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        padding: 2rem;
        margin-top: 2rem;
        font-size: 1.15rem;
        min-height: 120px;
        color: #222;
    }
    .placeholder {
        color: #888;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💼 LinkedIn Post Generator")
st.write("Generate a professional LinkedIn post from any article URL using AI.")

url = st.text_input("Enter the article URL", placeholder="https://example.com/article")

post_placeholder = st.empty()

if st.button("Generate LinkedIn Post", use_container_width=True):
    if url.strip():
        with st.spinner("Generating post..."):
            post = generate_linkedin_post(url.strip())
        post_placeholder.markdown(f'<div class="post-box">{post}</div>', unsafe_allow_html=True)
    else:
        post_placeholder.markdown('<div class="post-box placeholder">Please enter a valid article URL above.</div>', unsafe_allow_html=True)
else:
    post_placeholder.markdown('<div class="post-box placeholder">Your generated LinkedIn post will appear here.</div>', unsafe_allow_html=True) 