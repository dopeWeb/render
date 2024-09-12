from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


categories =[
    {"catid":1,"desc":"meat"},
    {"catid":2,"desc":"dairyyyyyyyyy"},
    {"catid":3,"desc":"bakery"},]


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/categories')
def get_categories():
    return categories



@app.route('/dis_cat/<int:id>')
def dis_cat(id):
    # Find the category with the given ID
    category = next((cat for cat in categories if cat["catid"] == id), None)
    if category:
        return (category)  # Return the category details as JSON
    else:
        return ({"error": "Category not found"}), 404  # Return 404 if not found
 


if __name__ == '__main__':
    app.run(debug=True)
