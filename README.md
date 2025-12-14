# VenueIQ

A full-stack Dash application for hospitality analytics that transforms operational and financial data into actionable insights through interactive dashboards.


<br>**Live Demo:**
<br>
*The demo uses seeded sample data to simulate real-world operations.*

<br>![Home Dashboard](screenshots/home-dashboard.png)

## <br>Problem

Hospitality operators often rely on spreadsheets, manual data entry, or disconnected reports to evaluate performance across departments. This makes it difficult to quickly identify trends, cost issues, or underperforming areas.

VenueIQ centralizes these metrics into a single dashboard designed around how hospitality managers actually evaluate performance.

## <br>Key Features

- Dashboards organized by operational area (Restaurant and Banquet)
- P&L-style financial summaries and KPI breakdowns
- Menu item performance and sales mix analysis
- Year-to-date and period-based views

## <br>Technical Highlights
- Modular, multi-page Dash architecture with dedicated services and callbacks
- MongoDB data modeling using aggregation pipelines for efficient reporting
- Reusable metric builders for dynamic KPI visualizations
- Full-stack development with clear back-end data handling and front-end integration
- Responsive layout with Bootstrap for desktop and mobile compatibility
- Environment-based configuration with structured error handling and logging

## <br>Tech Stack

- **Frontend:** Python Dash, Dash Bootstrap Components, Plotly
- **Backend:** Python, MongoEngine (ODM), pandas
- **Database:** MongoDB Atlas
- **Deployment:** Render (with Gunicorn)

## <br>Project Structure

```text
src/
├── app.py
├── callbacks/
├── components/
├── metrics/
├── models/
├── pages/
├── partials/
├── services/
└── utils/
```

## <br>Setup & Installation:
### Prerequisites ###
Ensure you have the following installed:
- Python 3.8+: Download from [Python.org](https://www.python.org/)
    <br>- Ensure that **"Add Python to PATH"** is checked during installation.
- Git: Download from [git-scm.com](https://git-scm.com/install/)

### Get the Code ###
Clone the repository from GitHub and navigate into the project directory:
  ```sh
  git clone https://github.com/jakeclara/venueiq.git
  cd venueiq
  ```

### Environment Setup ###
Use a virtual environment to manage dependencies:
```sh
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
```
Install the required libraries:
```sh
pip install -r requirements.txt
```

### Database Configuration and Seeding ###
VenueIQ requires a MongoDB connection string and seeded data to function.

1. **Obtain URI:** Create a database on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and retrieve your connection string (URI).

2. **Create .env file:** Create a new file named ```.env``` in the root of the project directory.

3. **Add Configuration:** Paste your connection string information into the file:
```sh
# Environment variables used for DB connection
MONGO_USER=your_mongo_user
MONGO_PASSWORD=your_mongo_password
MONGO_HOST=your_mongo_host
MONGO_DB=your_mongo_db
```
- **Note on Permission:**

4. **Seed Sample Data:** Run the data seeding script to populate the database with the required data:
```sh
python src/seeds/run_seeds.py
```

2. Create a virtual environment (recommended):
   - Command:  
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:  
       ```sh
       venv\Scripts\activate
       ```
     - **macOS/Linux**:  
       ```sh
       source venv/bin/activate
       ```

## <br>Architecture & Design

- Refactored from a monolithic structure into a **scalable, modular architecture** with clear separation between models, services, metrics, callbacks, and layouts
- Database access and calculations are handled in service and metrics layers to keep Dash callbacks **lightweight and maintainable**
- Aggregations and filtering are performed at the **database level (MongoDB)** to reduce data transfer and repeated client-side computation
- Feature development was done on isolated branches and merged into `main` using **Pull Requests**, ensuring a clean and auditable release history

## <br>Screenshots
### Banquet Dashboard ###
![Banquet Dashboard](screenshots/banquet-dashboard.png)

### <br>Restaurant Statement ###
![Restaurant Statement](screenshots/restaurant-statement.png)

## <br>Future Enhancements ##
- User authentication and role-based access for department-specific data viewing
- Integrate automatic data retrieval from real-world operational systems
- Optimize performance for larger datasets and additional venue locations
- Develop an exportable report generator for presentations and decision-making
- Introduce a modular framework to add and customize new operational departments and KPIs easily

## <br>Author
- **Jake Clara**
- [Github](https://github.com/jakeclara)
