from flask import Flask

app = Flask(__name__)

# Ana səhifə
@app.route("/")
def home():
    return """
    <h1>Ana Səhifə</h1>
    <p>Salam, xoş gəlmisən!</p>
    <a href="/haqqinda">Haqqımda</a><br>
    <a href="/elaqe">Əlaqə</a>
    """

# Haqqımda səhifəsi
@app.route("/haqqinda")
def haqqinda():
    return """
    <h1>Haqqımda</h1>
    <p>Mən Tahminayam, Flask öyrənirəm və bu mənim ilk saytiiiiiiım!</p>
    <a href="/">Geri qayıt</a>
    """

# Əlaqə səhifəsi
@app.route("/elaqe")
def elaqe():
    return """
    <h1>Əlaqə</h1>
    <p>Email: tahmina@example.com</p>
    <a href="/">Geri qayıt</a>
    """

# Serveri işə sal
if __name__ == "__main__":
    app.run(port=5013, debug=True)
