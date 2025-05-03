# User Recommendation System 🛍️🤖

Welcome to the **User Recommendation System**! This is a simple collaborative filtering-based recommendation engine built with **Flask** and **Singular Value Decomposition (SVD)**. It predicts the most relevant product recommendations for users based on their previous interactions with items, especially for products in their **locality**. 🌍

## Features 🌟

* **Flask Web App**: Lightweight web app to serve product recommendations 🚀
* **Collaborative Filtering**: Uses **SVD** to predict ratings for unseen items 🔮
* **Locality-based Recommendations**: Personalized recommendations based on **user locality** 🌍
* **Real-time API**: Get product recommendations instantly 📡

## Setup Instructions ⚙️

### Prerequisites 🔧

* Python 3.x 🐍
* `pip` (Python package installer) 🛒

### Installation 🚀

1. Clone the repository:

   ```bash
   git clone https://github.com/Soham-droid-pixel/UserEndRecommendations.git
   cd UserEndRecommendations
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Files in the Project 📂

* **`app.py`**: The core Flask app serving recommendations 🌟
* **`user_item_matrix.csv`**: User-item interaction matrix used for training the model 📊
* **`recommendation_model.ipynb`**: Jupyter notebook for building the recommendation system using **SVD** 💻
* **`data/user_data.csv`**: Dummy user interaction data generated using **Faker** 🔮
* **`requirements.txt`**: Python dependencies list 📋

### Running the App 🏃‍♂️

1. Make sure all dependencies are installed 📦.
2. Start the Flask app by running:

   ```bash
   python app.py
   ```

   The app will run at `http://127.0.0.1:5000/` 🌐

### API Endpoint 📡

#### `GET /recommend` 🎯

* **Description**: Get product recommendations for a specific user 🎁
* **Query Parameters**:

  * `user_id`: The ID of the user for whom recommendations are to be generated 👤
  * `top_n`: (Optional) The number of recommendations to return (default is 5) 📈

**Example Request**:

```bash
http://127.0.0.1:5000/recommend?user_id=1&top_n=5
```

**Example Response**:

```json
{
    "user_id": 1,
    "recommendations": ["Product A", "Product B", "Product C", "Product D", "Product E"]
}
```

### How it Works 💡

1. **Data Collection**:

   * We start with dummy user-item interaction data created using **Faker**. Each user has a list of products they've interacted with (rated, purchased, etc.) 🛒.

2. **Matrix Factorization**:

   * We apply **Singular Value Decomposition (SVD)** to the user-item matrix to find **latent factors** for users and items 🔍.

3. **Recommendation Generation**:

   * For each user, the system predicts the ratings for all items they haven't interacted with and recommends the top **N** items 📦.

### Model Training (Jupyter Notebook 📓)

The model training happens in the **`recommendation_model.ipynb`** notebook. It demonstrates how we can use **SVD** for collaborative filtering to build the recommendation system based on the user-item interaction matrix 🔄.

### Data Description 📑

* **`user_item_matrix.csv`**: This is the **user-item interaction matrix** where rows represent users, columns represent items, and the values represent interactions (ratings, purchases, etc.) 💬.

* **`user_data.csv`**: A dummy dataset of users and their interactions with products generated using **Faker** 🔮.

## Dependencies 🧳

This project uses the following Python libraries:

* **Flask**: For building the web app 🖥️
* **NumPy**: For numerical operations 🔢
* **Pandas**: For data manipulation 📊

Install these dependencies by running:

```bash
pip install -r requirements.txt
```

## Contributing 🤝

Feel free to fork the repository, make improvements, and submit **pull requests**. If you have any questions or suggestions, open an **issue** 📬.



