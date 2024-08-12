# Social Media Backend Clone

## Overview

The Social Media Backend Clone is a backend application developed using FastAPI that emulates a social media platform's core functionalities. This project provides a robust backend solution featuring user authentication, CRUD operations for posts, a vote/like system, and integrates with a PostgreSQL database using SQLAlchemy. It is designed to handle user interactions securely and efficiently, serving as a solid foundation for a social media application.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete posts.
- **User Authentication:** Secure user registration, login, and JWT-based authentication.
- **Vote/Like System:** Users can vote or like posts.
- **Database Integration:** PostgreSQL for data storage with SQLAlchemy ORM.
- **API Documentation:** Automatically generated documentation with FastAPI.
- **Environment Configuration:** Environment variables for secure management.

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Virtual environment (optional but recommended)

### Setup & Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/social-media-backend-clone.git
   cd social-media-backend-clone

2. **Create a Virtual Environment:**

   ```bash
    python -m venv venv
   ```

   For Windows:

   ```bash
   venv\Scripts\activate
   ```

   For MacOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   Install Dependencies:

   ```bash
    pip install -r requirements.txt
   ```

   Configure Environment Variables:

   ```bash
    DATABASE_URL=postgresql://username:password@localhost/dbname
    SECRET_KEY=your_secret_key
   ```

   Run Database Migrations:

    ```bash
    alembic upgrade head
    ```

    Start the Application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

### API Endpoints

#### User Endpoints:

- `POST /users/register`: Register a new user.
- `POST /users/login`: Login and receive a JWT token.
- `GET /users/{user_id}`: Retrieve user details.

#### Post Endpoints:

- `POST /posts`: Create a new post.
- `GET /posts`: Retrieve all posts.
- `GET /posts/{post_id}`: Retrieve a specific post.
- `PUT /posts/{post_id}`: Update a specific post.
- `DELETE /posts/{post_id}`: Delete a specific post.

#### Vote/Like Endpoints:

- `POST /posts/{post_id}/vote`: Vote on a post.
- `GET /posts/{post_id}/votes`: Retrieve votes for a specific post.


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch:**

   ```bash
   git checkout -b feature/your-feature

3. **Commit your changes:**

   ```bash
     git commit -am 'Add new feature'
   ```

4. **Push to the branch:**

   ```bash
     git push origin feature/your-feature
   ```


5. **Create a new Pull Request**

<br> 

## Contributor 

- [Krutarth Vora](https://github.com/ksv1112)

<br>
