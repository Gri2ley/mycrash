from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Генерация длинного URL
    long_url = 'http://example.com/' + 'a' * 10000  # 10,000 символов 'a'
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
