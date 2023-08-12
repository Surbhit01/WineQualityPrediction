# Wine Quality Prediction

End to End implementation of wine prediction web app.

## CONTENTS
1) Dataset Information[#DATASET INFORMATION]
2) Data Exploration[#DATA EXPLORATION]
3) Implementation [#IMPLEMENTATION]
4) How to run[#HOW TO RUN]

## DATASET INFORMATION
Dataset source - https://archive.ics.uci.edu/dataset/186/wine+quality <br>
This data set contains records related to red variant of the Portuguese Vinho Verde wine. It contains information from 1599 red wine samples. 

### **Input variables**

1) **Fixed acidity** - most acids involved with wine or fixed or nonvolatile (do not evaporate readily) <br>

2) **Volatile acidity** - the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste<br>

3) **Citric acid** - found in small quantities, citric acid can add 'freshness' and flavor to wines<br>

4) **Residual sugar** - the amount of sugar remaining after fermentation stops, it's rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet <br>

5) **Chlorides** - the amount of salt in the wine <br>

6) **Free sulfur dioxide** - the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine <br>

7) **Total sulfur dioxide** - amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine <br>

8) **Density** - the density of water is close to that of water depending on the percent alcohol and sugar content <br>

9) **pH** - describes how acidic or basic wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale <br>

10) **Sulphates** - a wine additive that can contribute to sulfur dioxide gas (S02) levels, which acts as an antimicrobial and antioxidant <br>

### **Output variable**

**Quality** - a value between 0 (very bad) and 10 (very excellent). This output indicates the quality of the wine.

## DATA EXPLORATION

* No null values are present <br>
* All input features have float values <br> 
* Output feature is an integer between 0 and 10 <br>

### **Relationship between input feature and Quality**

* Volatile acidity ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/218a684b-7ee6-42a5-bcb4-baad19b01c6e)

* Citric acid ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/151c1662-32cd-4d6e-ab95-b40446a13993)

* Residual sugar ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/ef46a810-686a-47c8-b9cd-8be0980c66de)


* Chlorides ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/3cd1b8e1-b426-489e-9aef-5c8df12dfd8c)


* Free sulfur dioxide ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/826038ff-7784-4b8f-a2ac-f6a72627ff62)


* Total sulfur dioxide ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/e0983e9e-01b4-4b05-ad4a-30736b792331)


* Density ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/91d2c410-c385-4b0d-b9ad-617857c79241)


* pH ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/66dca592-156e-44b9-9eae-5a7145abd5fa)


* Sulphates ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/fcf25b65-4115-4016-8a4c-5ed972d7e244)


* Alcohol ~ Quality

![image](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/3f30c0f0-84bc-4669-8c62-bfb1b41f9bec)

## IMPLEMENTATION

The following steps are involved in this end-to-end implementation:
* **Data Ingestion** - Downloading the zipped data from [here](https://github.com/Surbhit01/Datasets/raw/main/winequality-data.zip). The data is then unzipped and stored at a particular location

* **Data Validation** - The downloaded data is then validated using a predefined schema. The validation success result (true/false) is stored in a text file
  
* **Data Transformation** - If the data validation stage is successful, the data transformation stage will be executed. Here the data is divided into input and output features and then into train and test sets. If the data validation is not successful, this stage will throw an appropriate error message

* **Model Trainer** - ElasticNet has been used for training the model. The hyperparameters (l1_ratio and alpha) are read from a config file. The final model is then stored. Model training is tracked using MLFlow. 

*  **Model Evaluation** - The test set is then evaluated on the model

*  **Model Deployment** -  The web app has been deployed locally as a flask service and on AWS E2 instance with Github actions. The */train* route will automatically execute data ingestion, data transformation, model trainer and model evaluation stages. The default */* route will give the user the page to enter the input values.

**Sample Images**

Homepage

![HomePage](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/d7a48eac-f47a-4406-acfe-725b5a146bf0)


Result

![Result](https://github.com/Surbhit01/WineQualityPrediction/assets/24591039/c0c3748b-baf3-4324-987b-113895048933)

## HOW TO RUN

Step 1: Clone the repository
```
git clone https://github.com/Surbhit01/WineQualityPrediction.git
```

Step 2: Open the cloned repository and create a conda environment. Activate the new environment
```
conda create -n wineprediction python=3.9
```
```
conda activate wineprediction
```

Step 3: Install the requirements file
```
pip install -r requirements.txt
```

Step 4: Run the app
```
python app.py
```

The web app will be available on port 8080. */train* route will be for training the model. To make a prediction, go to the default route */*



