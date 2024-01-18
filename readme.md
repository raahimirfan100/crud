# CRUD Project

This project implements CRUD (Create, Read, Update, Delete) operations for managing items.

## Installation

1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.

### API Endpoints

- `GET /list/`: Retrieves a list of items sorted by search count.
- `GET /search/{name}/`: Searches for items with the given name and increments their search count.
- `POST /add/`: Adds a new item.
- `DELETE /delete/{name}/`: Deletes items with names containing the given value.

## Demo

You can watch a demo of this project on [Replit](https://de920950-d519-4849-9a50-9ed1a196949a-00-3bu79qyr1ttg8.sisko.replit.dev/).
