
# LLMOps Pipeline – Anime Recommender 🎌

A production-ready **LLMOps** project demonstrating an **end-to-end AI-powered recommendation pipeline** — from data processing to vector search, LLM integration, and scalable deployment via **Docker** and **Kubernetes**.

This project uses **LangChain**, **ChromaDB**, **Hugging Face embeddings**, and **Groq LLM** to deliver **personalized anime recommendations** via a **Streamlit** web app.

---

## 📌 Features

* 🎯 **Personalized Recommendations** – Tailored anime suggestions based on user preferences.
* 🔍 **Semantic Search** – Vector similarity matching for accurate results.
* 🚀 **Interactive UI** – Built with Streamlit.
* 🤖 **LLM-Powered** – Uses Groq LLM with custom prompt templates.
* 📊 **Vector Database** – Efficient retrieval using ChromaDB.
* ☁ **Cloud-Ready** – Deployable with Docker and Kubernetes.
* 📈 **Monitoring** – Optional Grafana Cloud setup for Kubernetes metrics.

---

## 📂 Project Structure

```
llmops-pipeline/
├── app/                      # Streamlit web application
├── config/                   # API keys and environment configs
├── data/                     # Anime datasets
├── pipeline/                 # Main recommendation pipeline
├── src/                      # Data loader, vector store, recommender, prompts
├── utils/                    # Logging & custom exceptions
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
├── Dockerfile                # For containerization
├── llmops-k8s.yaml           # Kubernetes deployment file
└── README.md                 # This file
```

---

## 🔧 1. Local Setup

### **Clone the Repository**

```bash
git clone https://github.com/0Xuser100/AnimeRecommender.git
cd AnimeRecommender
```

### **Create and Activate a Virtual Environment**

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### **Install Dependencies**

```bash
pip install --upgrade pip
pip install -e .
```

### **Set Environment Variables**

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

### **Run Locally**

```bash
streamlit run app/app.py
```

Access the app at: [http://localhost:8501](http://localhost:8501)

---

## 🐳 2. Run with Docker

### **Build Docker Image**

```bash
docker build -t llmops-app:latest .
```

### **Run Container**

```bash
docker run -p 8501:8501 --env-file .env llmops-app:latest
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## ☸ 3. Deploy on Kubernetes (Minikube / GKE)

### **Start Minikube**

```bash
minikube start
```

### **Point Docker to Minikube**

```bash
# Linux / Mac:
eval $(minikube docker-env)

# Windows (PowerShell):
& minikube -p minikube docker-env | Invoke-Expression

# Windows (Command Prompt):
@FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env') DO @%i
```

### **Build Image for Minikube**

```bash
docker build -t llmops-app:latest .
```

### **Create Secrets**

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="your_groq_key" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN="your_hf_token"
```

### **Apply Kubernetes Manifest**

```bash
kubectl apply -f llmops-k8s.yaml
```

### **Access Service**

```bash
minikube tunnel
# In another terminal:
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

Open: [http://<external-ip>:8501](http://<external-ip>:8501)

---

## 📊 4. Optional: Grafana Cloud Monitoring

1. Create a **Grafana Cloud** account.
2. Install **Helm** and add the Grafana repo:

   ```bash
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   ```
3. Deploy Kubernetes monitoring charts with:

   ```bash
   helm upgrade --install grafana-k8s-monitoring grafana/k8s-monitoring \
     --namespace monitoring --create-namespace --values values.yaml
   ```
4. View Kubernetes metrics in Grafana dashboards.

---

## 💡 Example Queries

* `"light hearted anime with school settings"`
* `"dark fantasy anime with complex storylines"`
* `"romantic comedy anime similar to Your Name"`

---

## 🛠 Tech Stack

* **LangChain** – LLM orchestration
* **ChromaDB** – Vector store
* **Hugging Face** – Embeddings
* **Groq LLM** – Fast inference
* **Streamlit** – Frontend
* **Docker + Kubernetes** – Deployment
* **Grafana** – Monitoring

---

## 👨‍💻 Author

**Mahmoud Abdulhamid**

