from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the user-item matrix and model
user_item_matrix = pd.read_csv('user_item_matrix.csv', index_col='User_ID')
U, sigma, Vt = np.linalg.svd(user_item_matrix, full_matrices=False)
k = 5
user_factors = U[:, :k]
item_factors = Vt[:k, :]

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id'))
    top_n = int(request.args.get('top_n', 5))

    # Predict ratings for the user
    user_ratings = np.dot(user_factors[user_id - 1], item_factors)

    # Sort items by predicted rating
    recommended_items = user_item_matrix.columns[np.argsort(-user_ratings)[:top_n]].tolist()

    return jsonify({
        'user_id': user_id,
        'recommendations': recommended_items
    })

if __name__ == '__main__':
    app.run(debug=True)