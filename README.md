# Data with Roots

Data with Roots is an educational web application that demonstrates how
machine learning can be applied to a practical logistics problem: estimating
delivery time from traveled distance.

The application combines a Flask web interface with a Simple Linear
Regression model trained on historical delivery records. It also includes
learning resources and visual explanations to support the understanding of
machine learning fundamentals.

<p align="center">
  <strong>Universidad de Cundinamarca · Faculty of Engineering · Semester 6 · Machine Learning</strong>
</p>

---

## Project Objective

The main objective is to estimate delivery time based on distance traveled
using a supervised learning model. In addition to making predictions, the
project presents the concepts behind the model in an accessible and
interactive way.

The application is intended for academic and demonstrative purposes. Its
predictions should not be considered a replacement for operational logistics
systems or real-world route planning.

## Main Features

- Explanations of fundamental machine learning concepts
- Overview of supervised, unsupervised, and reinforcement learning
- Four practical use cases in healthcare, finance, retail, and automotive
- Educational content about Simple Linear Regression
- Scatter plot with the fitted regression line
- Interactive prediction form for new distances
- Responsive interface built with Bootstrap
- Dataset statistics and sample records available in the application

## How It Works

1. The application loads the historical dataset from
   `data/delivery_dataset.csv`.
2. Distance in kilometers is used as the independent variable.
3. Delivery time in minutes is used as the dependent variable.
4. A `LinearRegression` model from scikit-learn is trained when the
   application starts.
5. A user enters a positive distance and receives an estimated delivery time.

## Model Summary

- **Independent variable (X):** Distance traveled (km)
- **Dependent variable (Y):** Delivery time (min)
- **Training records:** 600
- **Regression equation:** `Time = 0.4513 × Distance + 4.87`
- **Coefficient of determination (R²):** `0.9961`
- **Explained variance:** Approximately 99.6%

The model is based on a single predictor, so its results are useful for
demonstrating the relationship between distance and delivery time. Real
delivery times may also depend on traffic, weather, stops, vehicle type, and
other operational factors that are not included in this dataset.

## Technologies

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.x | Main programming language |
| Flask | 3.0.0 | Web application framework |
| scikit-learn | 1.3.2 | Model training and prediction |
| NumPy | 1.26.2 | Numerical calculations |
| Pandas | 2.1.4 | Data loading and manipulation |
| Matplotlib | 3.8.2 | Data visualization |
| Bootstrap | 5.3.2 | Responsive interface |
| Gunicorn | 21.2.0 | Production server |

## Project Structure

```text
.
├── app.py                     # Flask application and model logic
├── generate_dataset.py        # Dataset generation utility
├── requirements.txt           # Python dependencies
├── Procfile                   # Render deployment configuration
├── data/
│   └── delivery_dataset.csv   # Historical records used for training
├── static/
│   └── css/
│       └── style.css          # Application styles
├── templates/                 # HTML templates
│   ├── base.html              # Shared layout and navigation
│   ├── home.html              # Home page
│   ├── ml_concepts.html       # Machine learning concepts
│   ├── ml_types.html          # Machine learning types
│   ├── use_case_1.html        # Use case 1
│   ├── use_case_2.html        # Use case 2
│   ├── use_case_3.html        # Use case 3
│   ├── use_case_4.html        # Use case 4
│   ├── lr_concepts.html       # Linear Regression concepts
│   └── lr_application.html    # Chart and prediction form
├── README.md                  # Project documentation
└── Data_with_Roots_Proyecto_Completo.docx
```

## Local Installation

### Prerequisites

- Python 3.10 or newer
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/machinelearning-source/data-with-roots.git
cd data-with-roots

# Optional: create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open the application in a browser at:

```text
http://127.0.0.1:5000
```

To stop the development server, press `Ctrl+C` in the terminal.

## Deployment on Render

The repository includes a `Procfile` for deployment with Gunicorn.

1. Create a new Render Web Service connected to the repository.
2. Set the build command to:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the start command to:
   ```bash
   gunicorn app:app
   ```
4. Create the service and wait for the deployment to finish.

## Links

- **Repository:** https://github.com/machinelearning-source/data-with-roots
- **Live application:** https://data-with-roots-1.onrender.com

## Academic Context

This project was developed as part of the Machine Learning curriculum at the
Universidad de Cundinamarca. It brings together data analysis, predictive
modeling, visualization, and web development in a practical educational
application.

---

<p align="center">
  <strong>Universidad de Cundinamarca · Faculty of Engineering · Semester 6 · Machine Learning</strong>
</p>
