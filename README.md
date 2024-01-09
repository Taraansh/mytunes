# MyTunes Django Project

MyTunes is a simple Django web application for tracking and managing songs and artists.

## Features

- View a list of songs.
- View a list of artists along with the total number of songs each artist has.
- Add new artists and songs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django (install using `pip install django`)

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/Taraansh/MyTunes.git

   ```

2. Navigate to the project directory:

   cd MyTunes

3. Install dependencies:

   pip install -r requirements.txt

4. Apply database migrations:

   python manage.py makemigrations
   python manage.py migrate

### Running the Application

Start the Django development server:

    python manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser to access the application.

### Usage

    1. Navigate to the home page to view a list of songs.
    2. Navigate to the artists page to view a list of artists along with the total number of songs each artist has.
    3. Use the "Add Artist" and "Add Song" pages to add new artists and songs, respectively.

### Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Submit a pull request with a clear description of your changes.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
