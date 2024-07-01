
## Grazioso Salvare Dashboard

### Purpose
Grazioso Salvare is an innovative international rescue-animal training company. This project involves creating a web application dashboard to help Grazioso Salvare identify dogs from animal shelters around Austin, Texas, that are suitable for search-and-rescue training. The dashboard allows users to filter the data based on various rescue types and provides a dynamic view of the filtered data.

### Tools Used
- **Python:** The primary programming language used for development.
- **MongoDB:** Used as the database to store and retrieve animal data.
- **Dash:** A Python framework used to build the web application dashboard.
- **Pandas:** Used for data manipulation and analysis.

### Rationale for Tools
- **MongoDB:** Chosen for its flexibility in handling large datasets with varying structures. It allows for easy storage and retrieval of JSON-like documents, which is ideal for the animal shelter data.
- **Dash:** Provides a powerful framework for building interactive web applications with minimal effort. It integrates seamlessly with Plotly for creating dynamic charts and maps.
- **Pandas:** Offers robust data manipulation capabilities, making it easy to transform and filter the data as needed for the dashboard.

### Steps to Reproduce the Project

#### Prerequisites
- Install Python 3.x
- Install MongoDB and set up a database with the animal shelter data

Install required Python packages:
```bash
pip install dash
pip install jupyter_dash
pip install dash-leaflet
pip install pandas
pip install pymongo
```

#### Instructions

1. **Set Up the MongoDB Database:**
   Import the animal shelter data into MongoDB:
   ```bash
   mongoimport --username="${MONGO_USER}" --password="${MONGO_PASS}" --port=${MONGO_PORT} --host=${MONGO_HOST} --db AAC --collection animals --authenticationDatabase admin --type csv --headerline ./aac_shelter_outcomes.csv
   ```

2. **Clone the Repository:**
   - Clone the project repository to your local machine.

3. **Run the Dashboard:**
   - Open the `ProjectTwoDashboard.ipynb` file in Jupyter Notebook or JupyterLab.
   - Ensure the `Grazioso_Salvare_Logo.png` file is in the same directory as the notebook file.
   - Execute all cells in the notebook to start the Dash server.
   - Open the provided URL (usually `http://127.0.0.1:8050/`) in your web browser to view the dashboard.

### Explanation of the Code

- **MongoDB as the Model Component:**
  - MongoDB is used to store and manage the animal shelter data. It allows for flexible and scalable data storage, making it easy to retrieve and filter the data using Python's PyMongo library.

- **Dash Framework:**
  - Dash provides the view and controller structure for the web application. It allows for the creation of interactive and dynamic web applications using Python. The framework integrates well with Plotly for data visualization and offers a wide range of UI components.

### Functionality
The dashboard provides the following functionalities:
- **Display an Unfiltered Data Table:** Shows all available data from the animal shelters.
- **Interactive Filters:** Users can filter the data based on:
  - Water Rescue
  - Mountain or Wilderness Rescue
  - Disaster or Individual Tracking
  - Reset (to return to the original, unfiltered state)
- **Dynamic Data Table:** The data table updates based on the selected filter.
- **Geolocation Chart:** Displays the location of the selected animal on a map.
- **Unique Identifier:** The dashboard includes the Grazioso Salvare logo and the developer's name.



Water Rescue
 
![Screenshot 2024-06-24 030711](https://github.com/Besker1/Client_server_dev/assets/53057190/9a9e91f8-9bd3-4268-8000-5c7a22f77b7e)


Mountain or Wilderness Rescue
 ![Screenshot 2024-06-24 030629](https://github.com/Besker1/Client_server_dev/assets/53057190/b26b879b-2289-4b3e-b7f7-8022b6556558)


Disaster or Individual Tracking

 ![Screenshot 2024-06-24 030528](https://github.com/Besker1/Client_server_dev/assets/53057190/7e0556f8-a7fb-4ece-8be9-caf86cf1769b)

Reset:
 ![Screenshot 2024-06-24 030142](https://github.com/Besker1/Client_server_dev/assets/53057190/e1940306-6a6a-4b35-b5eb-c38eab7756bd)


**How do you write programs that are maintainable, readable, and adaptable?**

There are several best practices when it comes to writing our programs maintainable, readable and adaptable. Namespaces need to be easy to understand and use through clear naming conventions, well-commented documentation on how the code provided in a namespace works with specific variable names that are useful only within their module. For instance, we encapsulated database operations in Project One module CRUD Python code within functions and classes which makes it readable as well as easy to modify. This modular approach made it a lot easier to connect the dashboard widgets with the database layer in Project Two without requiring much modifications on either end. The advantage of this CRUD module is that it can be used in future projects with similar data operations, which fulfillment purpose of code reusability and redundancy for the application.

**How do you approach a problem as a computer scientist?**

As a computer scientist, you will often take problems and tasks approaching them by chopping that problem into smaller, manageable chunks of work as well understanding the requirements to solving it. RequirementsFor the Grazioso Salvare project, I needed to work on a dashboard where data could be dynamically filtered and shown. This set it apart from earlier requisites that demanded a combo of database management and dynamic front end development. Things like creating the ERD diagrams for how your database would look, writing pseudocode and iterative testing really came in handy. I will use this strategies in the future also, to get good user feedback and finally I met client requirement.

**What do computer scientists do, and why does it matter?**

Computer scientists create software to address real-world problems. That is important, because it also allows companies like Grazioso Salvare to run much more efficiently and effectively. We gave Grazioso Salvare a way to find and train the best dogs for search-and-rescue by developing this dashboard, helping them on their journey of saving lives. Projects of this kind are significant in showcasing how computer science can actively engage with societal welfare, thereby enhancing processes as well as outcomes across multiple domains.


