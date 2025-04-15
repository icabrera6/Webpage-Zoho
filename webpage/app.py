from flask import Flask, request, render_template, jsonify
import re

app = Flask(__name__)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email')
    if not is_valid_email(email):
        return jsonify({'success': False, 'message': 'Email inválido'}), 400
    # ...additional validation logic if needed...
    return jsonify({'success': True, 'message': 'Formulario enviado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
