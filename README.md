===========================
Django POI API Documentation
===========================

This project is a Django-based RESTful API for managing Points of Interest (POI). The API supports creating, retrieving, updating, and deleting POIs, with optional filtering by category.

Features
========
- Manage Points of Interest (POI) with fields like name, description, category, and geolocation.
- RESTful API endpoints for CRUD operations.
- PostgreSQL database for data persistence.
- Dockerized for easy setup and deployment.
- Support for bulk generation of random POI data.

Setup Instructions
==================
Follow these steps to set up and run the project locally or in a Docker environment.

Local Setup
-----------
1. **Clone the Repository**:
   .. code-block:: bash

      git clone <repository-url>
      cd <repository-folder>

2. **Create a Virtual Environment**:
   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

3. **Install Dependencies**:
   .. code-block:: bash

      pip install -r requirements/base.txt

4. **Run Database Migrations**:
   .. code-block:: bash

      python backend/manage.py migrate

5. **Start the Development Server**:
   .. code-block:: bash

      python backend/manage.py runserver

6. **Access the API**:
   Open your browser or API client at `http://127.0.0.1:8000`.

Docker Setup
------------
1. **Build and Start Containers**:
   .. code-block:: bash

      docker-compose up --build

2. **Run Migrations**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py migrate

3. **Seed Database with Random Data (Optional)**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py populate_pois

4. **Access the API**:
   Visit `http://127.0.0.1:8000`.

Environment Variables
=====================
The project uses environment variables for configuration. Create a `.env` file in the root directory with the following content:

.. code-block:: text

   DEBUG=True
   DJANGO_SECRET_KEY=your_secret_key
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_database_user
   POSTGRES_PASSWORD=your_database_password
   POSTGRES_HOST=db

Key Commands
============
Below are the key commands to manage the project:

1. **Run the Development Server**:
   .. code-block:: bash

      python backend/manage.py runserver

2. **Run Migrations**:
   .. code-block:: bash

      python backend/manage.py migrate

3. **Create a Superuser**:
   .. code-block:: bash

      python backend/manage.py createsuperuser

4. **Populate Database with Random Data**:
   .. code-block:: bash

      python backend/manage.py populate_pois

API Endpoints
=============
- **POST /api/poi/**: Create a new POI.
- **GET /api/poi/**: Retrieve a list of all POIs (optional filtering by category).
- **GET /api/poi/<id>/**: Retrieve a specific POI by ID.
- **PUT /api/poi/<id>/**: Update a POI by ID.
- **DELETE /api/poi/<id>/**: Delete a POI by ID.

Project Structure
=================
- **backend/**: Contains the main Django project files.
- **backend/points/**: Contains the POI app, including models, serializers, and views.
- **requirements/**: Requirements files for Python dependencies.
- **Dockerfile**: Docker configuration for the web service.
- **docker-compose.yml**: Docker Compose configuration for the entire project.

Testing
=======
Run tests to ensure the project works correctly:

.. code-block:: bash

   python backend/manage.py test
