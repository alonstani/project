import praw
from flask import Flask, render_template

app = Flask(__name__)

# Set up the Reddit API client
reddit = praw.Reddit(
    client_id='XtxgfTlCXsPnr9edfZdACw',
    client_secret='XENXG6j9mW9INr7qZmlgXskrr2ZV4A',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/requests'
)

@app.route('/')
def index():
    memes = get_memes_from_reddit()
    return render_template('index.html', memes=memes)

def get_memes_from_reddit():
    memes = []
    subreddit = reddit.subreddit('memes')
    for submission in subreddit.top(limit=10): 
        print(f"Title: {submission.title}, URL: {submission.url}")
        if submission.url.endswith(('jpg', 'jpeg', 'png')):
             print(f"Meme found")
             memes.append(submission.url)
    return memes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
