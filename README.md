# Aim_AI_Native_First
A simple sentiment analysis bot - Learn working with AI model APIs and Streamlit for UX
Idea: Create a sentiment analyzer or chatbot using OpenAI’s GPT API or Google's Gemini API
Example app: A web-based text sentiment analysis tool where users input text and get a sentiment score (positive/negative/neutral).

Step 1: Set Up Your Environment
Install Python 3.8+ if not installed.

Create a project folder, and inside it, set up a virtual environment:

bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install required libraries:

bash
pip install openai streamlit
Step 2: Get OpenAI API Access
Sign up at OpenAI if you haven’t.

Generate an API key from your OpenAI dashboard.

Store your API key securely (e.g., environment variable):

bash
export OPENAI_API_KEY="your_api_key_here"    # Mac/Linux
set OPENAI_API_KEY="your_api_key_here"       # Windows
Step 3: Create the Streamlit App File
Create a app.py file

Step 4: Run and Test Locally
Run the app locally:

bash
streamlit run app.py
The app opens in your browser.

Enter text and press “Analyze” to see the sentiment result.

Step 5: Deploy Your App
Sign up at Streamlit Cloud for free deployment.
Connect your GitHub repo with the app code.
Deploy and share the link to your simple AI-powered app.

