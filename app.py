from flask import Flask, render_template

app = Flask(__name__)

def get_shoes():
    shoes = [
        {'name': 'Golf', 'image': 'images/shoes1.jpg', 'price': 49.99},
        {'name': 'Adidas-Z5', 'image': 'images/shoes2.jpg', 'price': 59.99},
        {'name': 'ُRebook', 'image': 'images/shoes3.jpg', 'price': 70},
        {'name': 'Nike -AirMax', 'image': 'images/shoes4.jpg', 'price': 300},
        {'name': 'Skechers ', 'image': 'images/shoes5.jpg', 'price': 200},
        {'name': 'Nike Dunk High', 'image': 'images/shoes6.jpg', 'price': 150},
    ]
    return shoes

@app.route('/')
def home():
    shoes = get_shoes()
    return render_template('index.html', shoes=shoes)

if __name__ == '__main__':
    app.run(debug=True)
