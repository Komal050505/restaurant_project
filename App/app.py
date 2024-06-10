from flask import Flask, jsonify, request
from db_connections.configurations import session
from user_model.table import Restaurant_table

app = Flask(__name__)


# Give all restaurants
@app.route('/get_restaurants', methods=['GET'])
def get_restaurants():
    restaurants = session.query(Restaurant_table).all()
    restaurant_list = [
        {'name': restaurant.name, 'type': restaurant.type, 'items': restaurant.items,
         'price': restaurant.price, 'location': restaurant.location} for restaurant in restaurants]
    return jsonify({'data': restaurant_list})


# Get a specific restaurant
@app.route('/get_particular_restaurants', methods=['GET'])
def get_particular_restaurant():
    data = []
    result = request.args.get('name')
    restaurants = session.query(Restaurant_table).filter(Restaurant_table.name == result).all()
    if restaurants:
        restaurant_list = [
            {'name': restaurant.name, 'type': restaurant.type, 'items': restaurant.items,
             'price': restaurant.price, 'location': restaurant.location} for restaurant in restaurants]
        return jsonify({'data': restaurant_list})
    else:
        return jsonify({'message': 'Restaurant not found'}), 404


# Insert a new restaurant
@app.route('/add_restaurants', methods=['POST'])
def add_restaurant():
    new_restaurant_data = request.get_json()
    new_restaurant = Restaurant_table(
        name=new_restaurant_data['name'],
        type=new_restaurant_data['type'],
        items=new_restaurant_data['items'],
        price=new_restaurant_data['price'],
        location=new_restaurant_data['location']
    )
    session.add(new_restaurant)
    session.commit()
    return jsonify({'message': 'Restaurant added successfully'})


# Update an existing restaurant
@app.route('/update_restaurants', methods=['PATCH'])
def update_restaurant():
    user_data = request.get_json()
    session.query(Restaurant_table).filter(Restaurant_table.name == user_data.get('name')).update(user_data)

    session.commit()
    return jsonify({'message': 'Restaurant updated successfully'})


# Delete a restaurant
@app.route('/delete_restaurants', methods=['DELETE'])
def delete_restaurant():
    data = request.get_json()
    restaurant = session.query(Restaurant_table).filter(Restaurant_table.name == data.get('name')).delete()
    session.commit()
    return jsonify({'message': 'Restaurant deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
