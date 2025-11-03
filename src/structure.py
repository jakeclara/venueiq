'''
hospitality_dashboard/
│--.venv                        # python virtual environment for dependencies
|--.env                         # environment variables 
|--.gitignore           
|--README.md
|--src                          # main source code
|  |--assets                    # static assets 
|  |  |--logos/
|  |  |--css/
|  |  |--images/
|  |--callbacks                 # dash callback functions for interactivity
|  |  |--__init__.py
|  |  |--banquet_callbacks.py
|  |  |--combined_callbacks.py
|  |  |--restaurant_callbacks.py
|  |--models                    # data models for DB collections
|  |  |--__init__.py
|  |  |--menu_item.py
|  |  |--banquet_event.py
|  |  |--budget.py
|  |  |--sale.py
|  |--pages                     # individual dash pages for navigation
|  |  |--__init__.py
|  |  |--home.py
|  |  |--banquet/
|  |  |  |--snapshot.py
|  |  |  |--statement.py
|  |  |--restaurant/
|  |  |  |--snapshot.py
|  |  |  |--statement.py
|  |--partials                  # reusable UI layouts
|  |  |--__init__.py
|  |  |--footer.py
|  |  |--navbar.py
|  |--services                  # database access and business logic
|  |  |--__init__.py
|  |  |--banquet_service.py
|  |  |--budget_service.py
|  |  |--restaurant_service.py
|  |  |--database_service.py
|  |--app.py                    # main app entry point
'''