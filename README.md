
---

## **🩺 Breast Cancer Diagnosis - Machine Learning in Production**
This project is a Machine Learning-powered Breast Cancer Diagnosis system that allows users to predict breast cancer based on input features. The system consists of:

🖥 Flask-based backend
🌐 React-based frontend
☁️ Azure MySQL database
🚢 Deployed using Docker on Koyeb
🔁 Automated CI/CD pipeline with GitHub Actions
---

## **🚀 Features**
- 🏥 **Breast Cancer Prediction** using Machine Learning (Random Forest, KNN, SVM).
- 🌐 **Frontend** built with React (deployed on Koyeb).
- 🖥️ **Backend** built with Flask (deployed on Koyeb).
- 📦 **Containerized Deployment** with Docker & Docker Compose.
- ☁️ **Cloud Database** using **Azure MySQL**.
- 🔁 **CI/CD Pipeline** with **GitHub Actions**.
- 📊 **Model Management** using **DagsHub** & **MLflow**.

---

## **🛠️ Tech Stack**
### **Frontend**
- React.js
- Axios (for API calls)
- Bootstrap / Tailwind CSS (for UI)

### **Backend**
- Flask
- Flask-SQLAlchemy
- Pandas & Scikit-learn
- MySQL (Azure Database)

### **DevOps & Deployment**
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Koyeb (Cloud deployment)
- DagsHub (Model Versioning)
- Azure MySQL (Database hosting)

---

## **📂 Project Structure**
```plaintext
finalproject/
│── frontend/                 # React frontend
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│── backend/                  # Flask backend
│   ├── app.py
│   ├── implementation.py
│   ├── predictor_mlflow.ipynb
│   ├── Dockerfile
│── mlruns/                   # MLflow experiment tracking
│── docker-compose.yml         # Multi-container setup
│── .github/workflows/         # GitHub Actions CI/CD
│── README.md
```

---

## **📝 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Sam-zzy/finalproject.git
cd finalproject
```

### **2️⃣ Setup the Environment**
- Install dependencies:
  ```bash
  pip install -r backend/requirements.txt
  cd frontend && npm install
  ```

- Set environment variables in `.env`:
  ```plaintext
  DB_CONNECTION_STRING=mysql+pymysql://username:password@finalprojectmysql.mysql.database.azure.com:3306/finalproject_db
  FLASK_ENV=production
  ```

---

## **🐳 Running with Docker**
You can start the project using **Docker Compose**:

```bash
docker-compose up --build
```
This will:
- Run the **Flask backend** on `http://localhost:5000`
- Run the **React frontend** on `http://localhost:3000`

---

## **🌍 Deployment on Koyeb**
Both **Frontend & Backend** are deployed on [Koyeb](https://www.koyeb.com/).


**Deployment Workflow:**
1. GitHub Actions automatically builds Docker images.
2. The latest images are pushed to DockerHub.
3. Koyeb pulls the images and updates the services.

---

## **📊 Model Versioning with DagsHub**
Machine learning models are stored on **DagsHub** for versioning.
- The best-performing model is stored in:
  ```plaintext
  mlruns/0/<model-id>/artifacts/KNN/model.pkl
  ```
- Models are logged using **MLflow**.

---

## **🛠️ CI/CD Pipeline**
This project uses **GitHub Actions** for automated testing and deployment.
- 🚀 **On push to `dev`** → Runs integration tests.
- ✅ **On merge to `staging`** → Builds Docker images.
- ☁️ **On merge to `main`** → Deploys to **Koyeb**.

---

## **📬 API Endpoints**
| Endpoint              | Method | Description              |
|----------------------|--------|--------------------------|
| `/predict`           | POST   | Predicts cancer type    |
| `/train`             | POST   | Trains a new ML model   |
| `/health`            | GET    | Health check for API    |
