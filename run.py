from flask import Flask, jsonify, request
from flasgger import Swagger
from src.initializer import Initializer


app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
Swagger(app, template={
    "info": {
        "title": "Recipe Recommendation API",
        "description": "A simple API that recommends you any recipe you want.",
        "version": "1.0.0"
    }
})
initializer = Initializer()
pipeline = initializer.initialize()


@app.route('/api/recommend_recipe', methods=['GET'])
def recommend_recipe():
    """
        A simple recipe recommendation endpoint that accepts a recipe argument.
        ---
        tags:
          - Recipe
        parameters:
          - name: recipe
            in: query
            type: string
            required: true
            description: The name of the recipe
            example: "Pancakes"
        responses:
          200:
            description: A successful response
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: "Hello, World!"
                    recipe:
                      type: string
                      example: "Pancakes"
          400:
            description: Missing recipe parameter
    """
    recipe = request.args.get('recipe')
    if not recipe:
        return jsonify(error="Missing recipe parameter"), 400

    recommended_recipe = pipeline.run(f"{recipe} recipe")
    return jsonify(recommended_recipe=recommended_recipe)


if __name__ == '__main__':
    app.run(debug=True)
