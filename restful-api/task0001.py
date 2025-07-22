from flask import Flask, request, render_template_string
import csv
import re

app = Flask(__name__)

html_sablon = '''
<!DOCTYPE html>
<html>
<head>
    <title>Qeydiyyat Sistemi</title>
</head>
<body>
    <h2>Qeydiyyat Formu</h2>
    {% if mesaj %}
        <p style="color: red;">{{ mesaj }}</p>
    {% endif %}
    {% if ugurlu %}
        <p style="color: green;">{{ ugurlu }}</p>
    {% endif %}
    <form method="POST">
        <label>İstifadəçi adı:</label><br>
        <input type="text" name="username" value="{{ request.form.username or '' }}"><br><br>
        
        <label>Parol:</label><br>
        <input type="password" name="password"><br><br>
        
        <label>Email:</label><br>
        <input type="text" name="email" value="{{ request.form.email or '' }}"><br><br>
        
        <input type="submit" value="Qeydiyyat">
    </form>
</body>
</html>
'''

def email_dogru_formatda(email):
    # Sadə email yoxlama regex
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def save_to_csv(username, password, email):
    with open('qeydiyyatlar.csv', mode='a', newline='', encoding='utf-8') as fayl:
        writer = csv.writer(fayl)
        writer.writerow([username, password, email])

@app.route('/', methods=['GET', 'POST'])
def qeydiyyat():
    mesaj = None
    ugurlu = None
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        email = request.form.get('email', '').strip()
        
        # Yoxlamalar
        if not username:
            mesaj = "İstifadəçi adı boş ola bilməz!"
        elif not email_dogru_formatda(email):
            mesaj = "Email düzgün formatda deyil!"
        else:
            # Hamısı düzgündür, CSV-ə yaz
            save_to_csv(username, password, email)
            ugurlu = "Qeydiyyat uğurla tamamlandı!"
    
    return render_template_string(html_sablon, mesaj=mesaj, ugurlu=ugurlu, request=request)

if __name__ == "__main__":
    app.run(port=1453, debug=True, host="0.0.0.0")
