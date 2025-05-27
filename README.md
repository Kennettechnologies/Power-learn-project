# Inventory Management System

A comprehensive inventory management system built with Python and MySQL that helps businesses track, manage, and optimize their inventory operations.

## Features

- Product management (add, update, delete products)
- Stock tracking and management
- Sales and purchase tracking
- Supplier management
- User authentication and authorization
- Reports and analytics
- Low stock alerts
- Barcode/QR code support

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages (install using `pip install -r requirements.txt`):
  - mysql-connector-python
  - tkinter
  - pillow
  - qrcode
  - reportlab

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Kennettechnologies/Power-learn-project.git
cd Power-learn-project
```

2. Set up the MySQL database:
   - Install MySQL Server if you haven't already
   - Create a new database named `inventory_db`
   - Import the database schema using the provided SQL file:
```bash
mysql -u your_username -p inventory_db < database/schema.sql
```

3. Configure the database connection:
   - Open `config.py`
   - Update the database credentials with your MySQL settings:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'inventory_db'
}
```

4. Install required Python packages:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python main.py
```

## Project Structure

```
inventory-management-system/
├── database/
│   └── schema.sql
├── src/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── views/
│   └── controllers/
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 