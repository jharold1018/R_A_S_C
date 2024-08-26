from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados de las especies de serpientes y sus detalles
species_data = {
    "zona1": {
        "especie": "Serpiente1",
        "detalles": "Descripción de Serpiente1"
    },
    "zona2": {
        "especie": "Serpiente2",
        "detalles": "Descripción de Serpiente2"
    },
    # Agrega más datos para otras zonas
}

@app.route('/species', methods=['GET'])
def get_species():
    zona = request.args.get('zona')
    if zona in species_data:
        return jsonify(species_data[zona])
    else:
        return jsonify({"error": "Zona no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
