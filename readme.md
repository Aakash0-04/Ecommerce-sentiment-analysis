# E-commerce Review Sentiment Analysis (Flipkart – Samsung S24 & iPhone 15)

End-to-end NLP project to analyse Flipkart reviews for **Samsung Galaxy S24** and **iPhone 15**, generate **business insights**, and deploy a **sentiment prediction API** using FastAPI.

---

## 🧱 Project Structure

```bash
ECOM-- SENTIMENT/
│
├── App/
│   └── main.py                  # FastAPI app (loads model & serves /predict)
│
├── Data/
│   ├── Raw/                     # Raw CSVs (manually exported from Flipkart)
│   └── Processed/
│       ├── flipkart_cleaned.csv # Cleaned dataset
│       └── EDA_Charts/          # Saved EDA plots
│
├── Notebooks/
│   ├── EDA.ipynb                # Exploratory data analysis & insights
│   ├── Preprocessing.ipynb      # Cleaning, feature engineering, balancing
│   └── Model_Training.ipynb     # Model training & evaluation
│
├── Src/
│   ├── preprocess_flipkart.ipynb# Early experiments / scratch work
│   └── model.pkl                # Trained Logistic Regression model (TF-IDF)
│
├── Reports/
│   └── Insight_Report.pdf       # Business-facing insight report
│
├── Dockerfile                   # Container definition (not runnable on my HW)
├── requirements.txt             # Python dependencies
└── README.md

📊 Dataset & Labelling

Reviews manually collected from Flipkart using a browser extension
Products: Samsung Galaxy S24 and iPhone 15
Initial dataset was heavily positive, so:
Added extra negative reviews manually
Then balanced using oversampling / undersampling

Sentiment rules (rating-based):

rating >= 4 → positive
rating <= 2 → negative
rating == 3 → neutral (used for EDA, removed for model training)

🔍 Key Insights (from EDA)

Some highlights (full details in Reports/Insight_Report.pdf):

1. Strong Positive Bias

Majority of reviews are positive; negative reviews are much fewer.

2. Top Complaints

Heating + battery drain are common for both phones.

A few users complain about lag / performance in heavy usage.

3. Top Praises

Camera and display are the most appreciated aspects.

4. Review Length vs Sentiment

Negative reviews tend to be slightly longer, users explain problems.

5. Verified Buyers

Verified purchase reviews are more detailed and carry more negative signals (more honest feedback).

EDA charts are saved in: Data/Processed/EDA_Charts.

🤖 Model

Vectorizer: TfidfVectorizer
Classifier: LogisticRegression
Training done on the balanced dataset (positive vs negative).

On the balanced test set:

Accuracy ≈ 84%
Similar precision/recall for both classes
Confusion matrix image saved as:
Data/Processed/EDA_Charts/confusion_matrix_balanced.png

png

🚀 FastAPI Inference Service

The API is implemented in App/main.py.

1. Install dependencies
pip install -r requirements.txt

2. Activate virtual environment (if not already)
.\venv\Scripts\activate

3. Run the API
From the project root:
uvicorn App.main:app --reload
API root: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

4. Example request (Swagger sample)
{
  "review_text": "The phone heats up too quickly and the battery drains very fast. Worst experience ever."
}
Response:
{
  "review_text": "...",
  "clean_text": "phone heat quickly battery drain fast worst experience ever",
  "predicted_sentiment": "negative"
}
More tested examples are shown in the screenshots in the Insight report

⚠️ Limitations

Data is limited to Flipkart reviews for two specific phones.

Negative reviews are partly manually curated, not purely scraped.

No aspect-wise sentiment (battery, camera, delivery, etc.) yet.

API is running locally, not deployed to cloud.

Dockerfile is present but not tested due to hardware constraints.

🔮 Future Work

Host FastAPI app on Render / Railway / AWS.

Replace Logistic Regression with BERT-based transformer model.

Do aspect-based sentiment (battery vs camera vs delivery).

Add a simple Streamlit / React dashboard that calls the API.

👤 Author

Aakash Jaiswal

GitHub: Aakash0-04

Email: aakash041111@gmail.com

