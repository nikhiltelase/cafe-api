# Cafe API

Welcome to the Cafe API! This API allows you to manage a database of cafes, including retrieving details about cafes, searching for cafes by location, adding new cafes, updating cafe details, and deleting cafes.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [Get Random Cafe](#1-get-random-cafe)
  - [Get All Cafes](#2-get-all-cafes)
  - [Search Cafe by Location](#3-search-cafe-by-location)
  - [Add New Cafe](#4-add-new-cafe)
  - [Update Coffee Price](#5-update-coffee-price)
  - [Delete Cafe](#6-delete-cafe)
- [Data Model](#data-model)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Fetch a random cafe from the database
- Retrieve a list of all cafes
- Search for cafes by location
- Add a new cafe to the database
- Update the coffee price of a specified cafe
- Delete a specified cafe from the database

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML/CSS for documentation

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nikhiltelase/cafe-api.git
   cd cafe-api
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python main.py
   ```

4. **Access the API documentation:**
   Open your web browser and go to `https://cafe-api-five.vercel.app/`

## API Endpoints

### 1. Get Random Cafe

- **URL:** `/random`
- **Method:** GET
- **Description:** Fetches a random cafe from the database.

#### Python Example:
```python
import requests

response = requests.get('https://cafe-api-five.vercel.app/random')
print(response.json())
```

#### Expected Response:
```json
{
    "cafe": {
        "id": 1,
        "name": "Cafe Latte",
        "map_url": "https://example.com",
        "img_url": "https://example.com/image.jpg",
        "location": "Downtown",
        "seats": "50",
        "has_toilet": true,
        "has_wifi": true,
        "has_sockets": true,
        "can_take_calls": true,
        "coffee_price": "$4.00"
    }
}
```

### 2. Get All Cafes

- **URL:** `/all-cafe`
- **Method:** GET
- **Description:** Fetches all cafes from the database.

#### Python Example:
```python
import requests

response = requests.get('https://cafe-api-five.vercel.app/all-cafe')
print(response.json())
```

#### Expected Response:
```json
{
    "cafes": [
        {
            "id": 1,
            "name": "Cafe Latte",
            "map_url": "https://example.com",
            "img_url": "https://example.com/image.jpg",
            "location": "Downtown",
            "seats": "50",
            "has_toilet": true,
            "has_wifi": true,
            "has_sockets": true,
            "can_take_calls": true,
            "coffee_price": "$4.00"
        },
        {
            "id": 2,
            "name": "Cafe Mocha",
            "map_url": "https://example.com",
            "img_url": "https://example.com/image2.jpg",
            "location": "Uptown",
            "seats": "30",
            "has_toilet": true,
            "has_wifi": true,
            "has_sockets": true,
            "can_take_calls": true,
            "coffee_price": "$5.00"
        }
    ]
}
```

### 3. Search Cafe by Location

- **URL:** `/search`
- **Method:** GET
- **Description:** Searches for cafes by location.
- **Query Parameter:** `loc` (location of the cafe)

#### Python Example:
```python
import requests

params = {'loc': 'Downtown'}
response = requests.get('https://cafe-api-five.vercel.app/search', params=params)
print(response.json())
```

#### Expected Response:
```json
{
    "cafes": [
        {
            "id": 1,
            "name": "Cafe Latte",
            "map_url": "https://example.com",
            "img_url": "https://example.com/image.jpg",
            "location": "Downtown",
            "seats": "50",
            "has_toilet": true,
            "has_wifi": true,
            "has_sockets": true,
            "can_take_calls": true,
            "coffee_price": "$4.00"
        }
    ]
}
```

#### Error Response:
```json
{
    "error": "No cafes found at the specified location"
}
```

### 4. Add New Cafe

- **URL:** `/add`
- **Method:** POST
- **Description:** Adds a new cafe to the database.

#### Python Example:
```python
import requests

data = {
    'name': 'Cafe Mocha',
    'map_url': 'https://example.com',
    'img_url': 'https://example.com/image.jpg',
    'location': 'Uptown',
    'seats': '30',
    'has_toilet': True,
    'has_wifi': True,
    'has_sockets': True,
    'can_take_calls': True,
    'coffee_price': '$5.00'
}

response = requests.post('https://cafe-api-five.vercel.app/add', data=data)
print(response.json())
```

#### Expected Response:
```json
{
    "response": "success"
}
```

#### Error Response:
```json
{
    "response": "error: this cafe already exists."
}
```

### 5. Update Coffee Price

- **URL:** `/update-price/<cafe_id>`
- **Method:** PATCH
- **Description:** Updates the coffee price of a specified cafe.

#### Python Example:
```python
import requests

data = {'coffee_price': '$4.50'}
response = requests.patch('https://cafe-api-five.vercel.app/update-price/1', data=data)
print(response.json())
```

#### Expected Response:
```json
{
    "response": {
        "success": "Successfully updated the price."
    }
}
```

#### Error Response:
```json
{
    "error": {
        "Not Found": "Sorry, a cafe with that id was not found in the database."
    }
}
```

#### Missing Field Response:
```json
{
    "error": {
        "Missing field": "coffee_price is required"
    }
}
```

### 6. Delete Cafe

- **URL:** `/delete-cafe/<cafe_id>`
- **Method:** DELETE
- **Description:** Deletes a specified cafe from the database. Requires an API key.
- **Query Parameter:** `api-key` (API key for authentication)

#### Python Example:
```python
import requests

params = {'api-key': 'ram'}
response = requests.delete('https://cafe-api-five.vercel.app/delete-cafe/1', params=params)
print(response.json())
```

#### Expected Response:
```json
{
    "response": {
        "success": "Successfully deleted cafe."
    }
}
```

#### Error Response:
```json
{
    "error": {
        "Not Found": "Cafe not found"
    }
}
```

#### Invalid API Key Response:
```json
{
    "error": {
        "Invalid API Key": "API key is invalid"
    }
}
```

## Data Model

The cafe data model consists of the following fields:

- **id:** Integer, primary key, auto-incremented
- **name:** String, unique, required
- **map_url:** String, required
- **img_url:** String, required
- **location:** String, required
- **seats:** String, required
- **has_toilet:** Boolean, required
- **has_wifi:** Boolean, required
- **has_sockets:** Boolean, required
- **can_take_calls:** Boolean, required
- **coffee_price:** String, optional

## Contributing

We welcome contributions to improve the Cafe API. Please follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch for your feature:**
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature-name
   ```
5. **Create a pull request.**

## Contact

If you have any questions or need further assistance, feel free to contact us at .
- [Linkedin](https://www.linkedin.com/in/nikhiltelase/)