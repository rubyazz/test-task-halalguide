
Django POINT API Documentation
===========================

This project is a Django-based RESTful API for managing Points of Interest (POI). The API supports creating, retrieving, updating, and deleting POIs, with optional filtering by category.

Features
========
- Manage Points of Interest (POI) with fields like name, description, category, and geolocation.
- RESTful API endpoints for CRUD operations.
- PostgreSQL database for data persistence.
- Dockerized for easy setup and deployment.
- Support for bulk generation of random POI data.
- **Sphinx Documentation** to generate and serve detailed API documentation.

Setup Instructions
==================
Follow these steps to set up and run the project using Docker Compose.

Docker Setup
------------
1. **Clone the Repository**:
   .. code-block:: bash

      git clone <repository-url>
      cd <repository-folder>

2. **Create a `.env` File**:
   Add the following environment variables in the `.env` file:

   .. code-block:: text

      DEBUG=True
      DJANGO_SECRET_KEY=your_secret_key
      POSTGRES_DB=your_database_name
      POSTGRES_USER=your_database_user
      POSTGRES_PASSWORD=your_database_password
      POSTGRES_HOST=db

3. **Build and Start Containers**:
   .. code-block:: bash

      docker-compose up --build

4. **Run Database Migrations**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py migrate

5. **Seed Database with Random Data (Optional)**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py populate_pois

6. **Access the API**:
   Visit `http://127.0.0.1:8000/swagger` in your browser or API client.

Sphinx Documentation
====================
This project uses **Sphinx** to generate detailed HTML documentation for the API.

1. **Install Documentation Dependencies**:
   To generate the documentation, ensure that `sphinx` is included in your environment (it is in `requirements/base.txt`).

2. **Build Documentation**:
   To build the documentation using Docker Compose, run the following:

   .. code-block:: bash

      docker-compose run docs

   This command will generate the documentation in the `docs/build` directory.

3. **Serve Documentation Locally**:
   After building the documentation, you can serve it locally:

   .. code-block:: bash

      python -m http.server --directory docs/build 8080

   Then, visit `http://127.0.0.1:8080` to view the generated documentation.

4. **Access the Documentation through the API**:
   The generated documentation is also available directly through the Django application. To access it, visit:

   .. code-block:: bash

      http://127.0.0.1:8000/swagger/

   This will serve the Sphinx-generated docs through the Django web server.

Key Commands
============
Below are the key Docker Compose commands to manage the project:

1. **Start the Application**:
   .. code-block:: bash

      docker-compose up

2. **Run Migrations**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py migrate

3. **Create a Superuser**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py createsuperuser

4. **Seed Database with Random Data**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py populate_pois

5. **Run Tests**:
   .. code-block:: bash

      docker-compose run web python backend/manage.py test

6. **Stop Containers**:
   .. code-block:: bash

      docker-compose down

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
- **Dockerfile.docs**: Docker configuration for generating and serving Sphinx documentation.
- **docker-compose.yml**: Docker Compose configuration for the entire project.
- **.env**: Environment configuration file for the project.

Testing
=======
Run tests to ensure the project works correctly:

.. code-block:: bash

   docker-compose run web python backend/manage.py test

License
=======
This project is licensed under the MIT License.
