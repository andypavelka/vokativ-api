
from flask import Flask, request, jsonify

app = Flask(__name__)

vokativ_dict = {
    # Mužská jména
    "Jan": "Jane", "Petr": "Petře", "Pavel": "Pavle", "Tomáš": "Tomáši",
    "Jiří": "Jiří", "Martin": "Martine", "Miroslav": "Miroslave", "Jaroslav": "Jaroslave",
    "František": "Františku", "Josef": "Josefe", "David": "Davide", "Michal": "Michale",
    "Lukáš": "Lukáši", "Jakub": "Jakube", "Milan": "Milane", "Václav": "Václave",
    "Daniel": "Daniele", "Adam": "Adame", "Ondřej": "Ondřeji", "Radek": "Radku",
    "Marek": "Marku", "Roman": "Romane", "Aleš": "Aleši", "Zdeněk": "Zdeňku",
    "Stanislav": "Stanislave", "Robert": "Roberte", "Richard": "Richarde",
    "Filip": "Filipe", "Vlastimil": "Vlastimile", "Ladislav": "Ladislave",
    "Antonín": "Antoníne", "Libor": "Libore", "Vojtěch": "Vojtěchu",
    "Karel": "Karle", "Jindřich": "Jindřichu", "Bohuslav": "Bohuslave",
    "Rostislav": "Rostislave", "Bohumil": "Bohumile", "Oldřich": "Oldřichu",

    # Ženská jména
    "Jana": "Jano", "Marie": "Marie", "Eva": "Evo", "Anna": "Anno",
    "Hana": "Hano", "Lenka": "Lenko", "Kateřina": "Kateřino", "Věra": "Věro",
    "Alena": "Aleno", "Petra": "Petro", "Veronika": "Veroniko", "Tereza": "Terezo",
    "Martina": "Martino", "Michaela": "Michaelo", "Jiřina": "Jiřino", "Božena": "Boženo",
    "Helena": "Heleno", "Zuzana": "Zuzano", "Barbora": "Barbaro", "Kristýna": "Kristýno",
    "Monika": "Moniko", "Pavla": "Pavlo", "Lucie": "Lucie", "Ivana": "Ivano",
    "Dagmar": "Dagmar", "Jitka": "Jitko", "Andrea": "Andreo", "Radka": "Radko",
    "Markéta": "Markéto", "Simona": "Simono", "Klára": "Kláro", "Nikola": "Nikolo",
    "Irena": "Ireno", "Milada": "Milado", "Růžena": "Růženo", "Vlasta": "Vlasto"
}
@app.route('/api/vokativ')
def get_vokativ():
    name = request.args.get('name', '').strip()
    vokativ = vokativ_dict.get(name, name + 'e') if name else ''
    return jsonify({"name": name, "vokativ": vokativ})

if __name__ == '__main__':
    pass  # nebo nic
