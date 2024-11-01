# CSV_analyzer_web2

# CSV Analysis Web Application

This web application allows users to upload and analyze CSV files through an intuitive interface. The application provides detailed analysis and visualization of the uploaded data.

## Installation

1. Download the project zip file
2. Extract the zip file to your desired location
3. Navigate to the project directory

   ![image](https://github.com/user-attachments/assets/5b6dce45-7fce-4362-86dd-7b883a2ac0b4)


### Run the requirements.txt file

```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the application:
```bash
python -m streamlit run app.py
```
2. Open your web browser and navigate to:
```
http://localhost:8501
```

## Usage Flow

### 1. Initial Screen
- Upon accessing the application, you'll see the main upload interface
- The interface features a "Browse Files" button centered on the page

  ![image](https://github.com/user-attachments/assets/aedd3b43-ec29-4572-b2f9-7fafa44c110b)


### 2. File Upload
- Click on the "Browse Files" button
- Select your CSV file from your local system
- The file will be uploaded and processed automatically

  ![image](https://github.com/user-attachments/assets/1cdb3021-d7ba-498b-99fe-53024f75d691)


### 3. Analysis Dashboard
After successful upload, the analysis dashboard will appear showing:
- Data overview and statistics
- Visualizations and charts
- Detailed analysis of the CSV content

### 4. Data Analysis
  ![image](https://github.com/user-attachments/assets/1e2b0f9d-bc2f-46d3-aed0-257fa901b44b)
  
-  Displays basic statistics of the uploaded CSV (Name of the file (PINN-scopus_new.csv),Size of the file  (5.3MB))
-  Shows data shape (4440 rows, 14 columns) and data types (12 object, 2 int64)
-  Can view raw data view with the checkbox and explore basic dataset statistics
  
  ![image](https://github.com/user-attachments/assets/7439c4b9-690b-431c-98d8-7c0da9485543)
  
- Shows missing value counts across different columns 
- Displays numeric column analysis with descriptive statistics
- Can be used to identify data quality issues and gaps in the dataset
  
  ![image](https://github.com/user-attachments/assets/4e426ec3-8f00-4df5-a6c4-08a08578cc14)

-Presents three visualization types: Distribution, Boxplot, and Line Plot for selected columns
-Currently showing Year-based visualizations with trends from 2016-2024
-Can select different columns from the dropdown for alternative visualization views

  ![image](https://github.com/user-attachments/assets/5075bc68-6de2-440d-a0b0-b999a61698bc)

-Shows value counts for categorical columns (currently displaying Author full names)
-Presents data in a horizontal bar chart format
-Can select different categorical columns from the dropdown for different analyses

## Features

- Simple and intuitive user interface
- Secure file upload system
- Comprehensive data analysis
- Interactive visualizations

## System Requirements

- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Safari)
- Internet connection for initial setup

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed
2. Check if the correct Python version is being used
3. Verify that the CSV file is properly formatted
4. Make sure no other application is using on the port hosting the localhost
