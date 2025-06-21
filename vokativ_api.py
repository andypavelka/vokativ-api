
from flask import Flask, request, jsonify

app = Flask(__name__)

vokativ_dict = {"Jan": "Jane", "Petr": "Petře", "Lucie": "Lucie", "Tomáš": "Tomáši", "Ondřej": "Ondřeji", "Vratislav": "Vratislave", "Eva": "Evo", "Filip": "Filipe", "Tereza": "Terezo", "Radek": "Radku", "Dominik": "Dominiku", "Daniel": "Daniele", "Kateřina": "Kateřino", "Lenka": "Lenko", "David": "Davide", "Veronika": "Veroniko", "Matěj": "Matěji", "Barbora": "Barboro", "Karel": "Karle"}

@app.route('/api/vokativ')
def get_vokativ():
    name = request.args.get('name', '').strip()
    vokativ = vokativ_dict.get(name, name + 'e') if name else ''
    return jsonify({"name": name, "vokativ": vokativ})

if __name__ == '__main__':
    app.run()
