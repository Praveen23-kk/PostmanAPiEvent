---
# University Mentorship Platform

This project is a web-based application designed to facilitate mentorship connections between students and mentors at a university. Users can view available mentors, send mentorship requests, and manage their requests through a simple and intuitive interface.

## Features

- **Mentor List**: View a list of available mentors along with their areas of expertise.
- **Mentorship Requests**: Send mentorship requests to mentors and manage the status of requests (Pending, Approved).
- **User-Friendly Interface**: A responsive web application designed with a modern aesthetic.
- **Django REST API**: The backend is built using Django and Django REST Framework, providing a robust API for interaction.
- **Database Integration**: Utilizes a relational database to store and manage user and mentorship data.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (or any other relational database of your choice)
- **Libraries**: Axios (for API requests), Django Rest Framework

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- Node.js (optional, if you're using npm packages)

### Clone the Repository

```bash
git clone https://github.com/yourusername/university-mentorship-platform.git
cd university-mentorship-platform
```

### Setting Up the Backend

1. **Install Requirements**:

   Create a virtual environment and install the required packages.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

2. **Apply Migrations**:

   Run migrations to set up the database.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Run the Server**:

   Start the Django development server.

   ```bash
   python manage.py runserver
   ```

4. **Access the API**:

   Open your browser and navigate to `http://127.0.0.1:8000/api/` to test the API endpoints.

### Setting Up the Frontend

1. Open `index.html` in your preferred browser to view the application.

2. Ensure the API endpoints in the frontend JavaScript code point to the correct backend URLs.

## API Endpoints

| Method | Endpoint                     | Description                         |
|--------|------------------------------|-------------------------------------|
| GET    | /api/mentors/                | Get the list of available mentors.  |
| POST   | /api/mentorship-request/      | Create a new mentorship request.    |
| GET    | /api/my-requests/            | Get the user's mentorship requests.  |
| GET    | /api/students/               | Get the list of students.           |

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-YourFeature`
3. Commit your changes: `git commit -m 'Add your message'`
4. Push to the branch: `git push origin feature-YourFeature`
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django and Django REST Framework for the backend development.
- HTML, CSS, and JavaScript for the frontend development.
- All contributors and mentors who helped shape this project.

---
