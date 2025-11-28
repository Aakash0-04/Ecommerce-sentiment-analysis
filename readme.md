📦 End-to-End Sentiment Analysis Pipeline (Flipkart E-Commerce Reviews)
Author: Aakash Jaiswal
Tech Stack: Python, FastAPI, Scikit-Learn, NLTK, Pandas, Matplotlib, Imbalanced-Learn

🚀 Project Overview

This project is an end-to-end sentiment analysis pipeline built using real Flipkart reviews of:

1) Samsung S24
2) iPhone 15

The pipeline covers:

✔ Web-scraped dataset
✔ Preprocessing & cleaning
✔ Exploratory Data Analysis (EDA)
✔ Sentiment labelling (based on rating)
✔ Data balancing using undersampling
✔ Model training & evaluation
✔ Visualization dashboards
✔ FastAPI endpoint for real-time predictions

-------------------------------------------------------------------------------------------------------------------------------------

📁 Folder Structure

ECOM-- SENTIMENT/
│
├── App/
│   ├── main.py               # FastAPI sentiment prediction API
│   └── model.pkl             # Trained ML model
│
├── Data/
│   ├── Raw/                             # Raw scraped CSV files (positive + negative)
│   ├── Processed/
│   │      └── flipkart_model_ready.csv  # Processed dataset
│   │
│   └── EDA Charts/                      # Saved visualizations (.png)
│
├── Notebooks/
│   ├── EDA.ipynb             # Exploratory Data Analysis + insights
│   ├── Preprocessing.ipynb   # Cleaning, feature engineering, balancing
│   └── Model_Training.ipynb  # ML model building & evaluation
│
├── Src/
│   └── preprocess_flipkart.ipynb   # Initial version of preprocessing
│
├── venv/                     # Virtual environment
│
├── requirements.txt          # Python dependencies
│
└── README.md                 # Project documentation (this file)


-------------------------------------------------------------------------------------------------------------------------------------

📊 Dataset Summary

| Product     | Count        |
| ----------- | ------------ |
| Samsung S24 | ~700 reviews |
| iPhone 15   | ~650 reviews |

Sentiment Rules

Positive: rating ≥ 4
Negative: rating ≤ 2
Neutral: rating = 3

Imbalance Issue

Raw data was heavily positive biased, so the following were applied:
✔ Undersampling (RandomUnderSampler)

-------------------------------------------------------------------------------------------------------------------------------------

📈 Key Insights (Business-Focused)

⭐ 1. Overall Sentiment

Majority reviews are positive, indicating strong customer satisfaction.
Negative reviews mainly highlight:
Heating issues
Battery drain
Delivery or quality problems

⭐ 2. Battery & Camera Drive Reviews

WordCloud shows camera, battery, display, performance dominate both positive & negative reviews.
Battery drain is the top negative complaint.

⭐ 3. Review Length vs Sentiment

Neutral reviews have the longest average word count.
Negative reviews are more direct and short

⭐ 4. Helpful Upvotes

Positive reviews get significantly more helpful upvotes, meaning people trust them more.

⭐ 5. Samsung S24 vs iPhone 15

Both products have strong positive sentiment.
iPhone reviews include more mentions of:
camera quality
premium feel
Samsung reviews emphasize:
display
battery performance

-------------------------------------------------------------------------------------------------------------------------------------

🤖 Model Training

Final Metrics (Balanced Dataset)

Accuracy: ~87%
Precision: 0.84 – 0.86
Recall: 0.84 – 0.85
F1-Score: ~0.85

Confusion Matrix (Balanced)

You can include your saved image

![](Data/Processed/confusion_matrix_balanced.png)

-------------------------------------------------------------------------------------------------------------------------------------

🧪 API Endpoint (FastAPI)

Start the server:
uvicorn App.main:app --reload
Open:
http://127.0.0.1:8000/docs

Example Request
POST /predict
{
  "review_text": "The camera heats too much and battery drains fast."
}

Example Response
{
  "review_text": "...",
  "clean_text": "...",
  "predicted_sentiment": "negative"
}

-------------------------------------------------------------------------------------------------------------------------------------

🛠 Installation Instructions

1️⃣ Create virtual environment
python -m venv venv

2️⃣ Activate venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run FastAPI
uvicorn App.main:app --reload

-------------------------------------------------------------------------------------------------------------------------------------

📄 Included Visualizations

The project contains:

Sentiment distribution
Rating distribution
WordCloud
Verified vs not-verified sentiment
Product-wise sentiment comparison
Helpful upvotes box-plot
Review length vs sentiment

Confusion matrix
Data/Processed/

-------------------------------------------------------------------------------------------------------------------------------------

📝 Final Deliverables

✔ Raw scraped dataset
✔ Cleaned & processed dataset
✔ EDA notebook
✔ ML training notebook
✔ Metrics + confusion matrix
✔ Insight report (this README)
✔ FastAPI working endpoin

-------------------------------------------------------------------------------------------------------------------------------------

Limitations & Future Work

Limited number of negative reviews → used SMOTE + undersampling to balance.
Data only from Flipkart (Samsung S24 & iPhone 15) → model biased to high-end phones.
Could try transformer models (BERT) in the future.