# 🛡️ AI vs Human Content Detection System

A **Flask-based machine learning** application designed to detect whether uploaded content — **images**, **videos**, or **text** — is **human-generated** or **AI-generated**.

---

## 🚀 Features

- 🔍 Detects AI vs Human-generated:
  - 🖼 **Images**
  - 🎥 **Videos**
  - 📝 **Text**
- 🧠 ML Techniques:
  - Logistic Regression
  - TF-IDF Vectorization (for text)
- 📦 Built With:
  - Python
  - Flask
  - OpenCV
  - Scikit-learn
- 🧪 Trained on real-world datasets

---

## 🧱 Project Structure

- **app.py:** Main Flask application which manages routing and server functions.
- **templates/index.html:** Frontend upload form allowing users to upload files for prediction.
- **models/:** Contains trained machine learning models and dataset used for training.
- **utils/:** Python scripts that contain logic to process different data types (image, video, text) and make predictions.
- **uploads/:** Temporary directory for storing files uploaded by users.
- **requirements.txt:** List of Python dependencies required to run the project.
- **README.md:** This documentation file.

---

## 📂 Datasets Used

| Type   | Source |
|--------|--------|
| **Image** | [ThisPersonDoesNotExist](https://thispersondoesnotexist.com/), CelebA, Kaggle Subsets |
| **Video** | Mixed synthetic and real-world video clips |
| **Text** | Manually labeled sentences in `AI_Human.csv` |

---

# Project Policy and Contributions

## 📜 Policy

- **Content Authenticity Policy:**  
  The project includes a document titled [Content_Authenticity_Policy.pdf](Content_Authenticity_Policy.pdf) that outlines the system’s usage policies and guidelines for AI-generated content detection. Please review this document to understand the ethical and responsible use of the system.

---

## 👨‍💻 Authors

- **Haider Abbas**  
  GitHub: [haider14-9abbaas](https://github.com/haider14-9abbaas)

- **Hamza Kamran**  
  GitHub: [Hamza-hani](https://github.com/Hamza-hani)

---

## 📘 License

This project is intended for **research and educational use only**. Users are encouraged to ensure responsible and ethical use when applying content detection methods.

---

## 🙌 Contributions

We welcome contributions to improve the system! Feel free to:

- Fork the repository
- Open issues for bugs or feature requests
- Submit pull requests with your improvements

Your contributions help enhance the project and foster a collaborative environment!

---

## ⚙️ Run Locally

```bash
# Step 1: Create virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# Or: source venv/bin/activate  # For Linux/Mac

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Train models (only once)
python train_image_model_from_your_dataset.py
python train_video_model.py
python train_text_model.py

# Step 4: Launch the Flask app
python app.py

# Open your browser:
http://127.0.0.1:5000

---

