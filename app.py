from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize totals
total_weight = 0
total_price = 0
clicked_buttons = []

# Button list with name, weight, and price
buttons = [
    {"name": "Bibiki Slug", "weight": 3, "price": 5},
    {"name": "Bibiki Urchin", "weight": 6, "price": 750},
    {"name": "Broken Willow Rod", "weight": 6, "price": 0},
    {"name": "Coral Fragment", "weight": 6, "price": 1735},
    {"name": "Crab Shell", "weight": 6, "price": 392},
    {"name": "Elm Log", "weight": 6, "price": 390},
    {"name": "Fish Scales", "weight": 3, "price": 23},
    {"name": "Goblin Armor", "weight": 6, "price": 0},
    {"name": "Goblin Mail", "weight": 6, "price": 0},
    {"name": "Goblin Mask", "weight": 6, "price": 0},
    {"name": "High-Quality Crab Shell", "weight": 6, "price": 3312},
    {"name": "High-Quality Pugil Scales", "weight": 6, "price": 253},
    {"name": "Hobgoblin Bread", "weight": 6, "price": 91},
    {"name": "Hobgoblin Pie", "weight": 6, "price": 153},
    {"name": "Jacknife", "weight": 11, "price": 20},
    {"name": "Lacquer Tree Log", "weight": 6, "price": 3578},
    {"name": "Maple Log", "weight": 6, "price": 15},
    {"name": "Nebimonite", "weight": 6, "price": 53},
    {"name": "Oxblood", "weight": 6, "price": 13250},
    {"name": "Pamtam Kelp", "weight": 6, "price": 7},
    {"name": "Pebble", "weight": 7, "price": 1},
    {"name": "Petrified Log", "weight": 6, "price": 2193},
    {"name": "Pugil Scales", "weight": 3, "price": 23},
    {"name": "Seashell", "weight": 6, "price": 29},
    {"name": "Shall Shell", "weight": 6, "price": 307},
    {"name": "Titanictus Shell", "weight": 6, "price": 357},
    {"name": "Tropical Clam", "weight": 20, "price": 5100},
    {"name": "Turtle Shell", "weight": 6, "price": 1190},
    {"name": "Uragnite Shell", "weight": 6, "price": 1455},
    {"name": "Vongola Clam", "weight": 6, "price": 192},
    {"name": "White Sand", "weight": 7, "price": 250}
]

@app.route('/')
def index():
    return render_template('index.html', buttons=buttons, total_weight=total_weight, total_price=total_price, clicked_buttons=clicked_buttons)

@app.route('/add_item', methods=['POST'])
def add_item():
    global total_weight, total_price, clicked_buttons
    button_name = request.form['button_name']
    weight = next(item['weight'] for item in buttons if item['name'] == button_name)
    price = next(item['price'] for item in buttons if item['name'] == button_name)
    total_weight += weight
    total_price += price
    clicked_buttons.append(button_name)
    return render_template('index.html', buttons=buttons, total_weight=total_weight, total_price=total_price, clicked_buttons=clicked_buttons)

@app.route('/reset', methods=['POST'])
def reset():
    global total_weight, total_price, clicked_buttons
    total_weight = 0
    total_price = 0
    clicked_buttons = []
    return render_template('index.html', buttons=buttons, total_weight=total_weight, total_price=total_price, clicked_buttons=clicked_buttons)

if __name__ == '__main__':
    app.run()