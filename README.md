
# Laptop Price Prediction App 💻💰

This project is a machine learning regression app that predicts the price of a laptop based on various features such as the company, product type, CPU, GPU, RAM, memory, and more.

## Project Overview 📊

The main goal of this app is to provide users with an estimated laptop price based on their selected features. The model was trained using GradientBoostingRegressor with hyperparameter tuning to ensure the best performance.

## Features 🔑

- **Input Features:**
  - Company name
  - Product name
  - Type of product
  - RAM
  - Memory
  - GPU
  - CPU
  - Weight
  - Operating system
  - Inches
  - Screen resolution

- **Output:**
  - The app predicts the laptop price in **Euros**, and also provides conversions to **INR**, **NPR**, and **USD**.

## Project Pipeline 🛠️

1. **Data Ingestion**: 
   - Loads the data from an SQL database.
   - Splits the data into training and testing sets.
   - Saves the datasets to a folder.
   
2. **Data Transformation**:
   - Performs feature engineering and transformations on the training and testing data.
   - Saves the transformed data and the preprocessor for future use.

3. **Model Building**:
   - Trains the GradientBoostingRegressor model using the transformed data.
   - Performs hyperparameter tuning for optimal performance.
   - Saves the trained model.

4. **Prediction Pipeline**:
   - Uses the saved preprocessor and model to predict the laptop prices based on input features.

## Technologies Used 🧰

- **Programming Language**: Python
- **Libraries**: Sklearn, Streamlit
- **Database**: MySQL (Data sourced from [Kaggle](https://www.kaggle.com/datasets/muhammetvarl/laptop-price))
- **Deployment**: Docker, GitHub Actions, Amazon EC2, and ECR
- **Version Control**: GitHub

## How to Run the App Locally 🖥️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ayushach007/laptop_price_prediction
   ```

2. **Create a virtual environment**:
   Using `python`:
   ```bash
   python -m venv venv
   ```

   Or using `conda`:
   ```bash
   conda create --name laptop_price_pred python=3.11
   conda activate laptop_price_pred
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run training pipeline**
    ```bash
    python main.py
    ```

5. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## AWS Continuous Deployment with GitHub Actions :technologist:
   

#### 1. Login to AWS console.

#### 2. Set up an **IAM User** in AWS

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
#### 3. Create an **ECR repository** to store the Docker image
    - Save the URI: 

	
#### 4. Set up an **EC2 instance**

#### 5. Open **EC2** and Install docker in **EC2** Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
#### 6. Configure the EC2 instance as a **Self-Hosted Runner**
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


#### 7. Set up **GitHub Secrets** for secure deployment

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION= us-east-1

    AWS_ECR_LOGIN_URI= demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME= laptop_price_predictor

## Future Improvements 🚀

- Implementing **DVC** and **MLflow** for better version control of the data and model.
- Exploring **deep learning algorithms** to improve the model's performance.

## License 📜

This project is licensed under the **GNU General Public License**.

