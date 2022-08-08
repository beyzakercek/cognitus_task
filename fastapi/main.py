from fastapi import FastAPI
from celery import Celery

from algorithm import *
from database import *


app = FastAPI()
celery_app = Celery('celery_app', broker_url = "redis://127.0.0.1:6379/0")

@celery_app.task
def train_celery():
    connection = SessionLocal()
    data = connection.execute("SELECT * FROM app_data")

    text, label = [], []
    for obj in data:
        text.append(obj.text)
        label.append(obj.label)

    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    connection.close()

 
@app.post("/train")
async def train():
    train_celery.delay()
    return {"message":"success"}

@app.post("/predict")
async def predict(text: str):
    model = load_model('model.pickle')
    vectorizer = load_model('vectorizer.pickle')
    tdifd = vectorizer.transform([text])
    result = model.predict_proba(tdifd)
    return {'response': result}


