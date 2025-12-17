from flask import Flask, jsonify, request, abort


def create_app():
	app = Flask(__name__)
	app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

	# Datos en memoria para ejemplo simple
	items = [{"id": 1, "name": "item1"}]

	@app.route("/")
	def index():
		return jsonify({"message": "Hola desde Flask!"})

	@app.route("/items", methods=["GET"])
	def get_items():
		return jsonify(items)

	@app.route("/items", methods=["POST"])
	def create_item():
		data = request.get_json()
		if not data or "name" not in data:
			abort(400, description="Se requiere 'name' en el cuerpo JSON")
		new_item = {"id": max([i["id"] for i in items]) + 1 if items else 1, "name": data["name"]}
		items.append(new_item)
		return jsonify(new_item), 201

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host="0.0.0.0", port=5000)
