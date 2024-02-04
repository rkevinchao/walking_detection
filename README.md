# walking-detection
* This is a project to demonstrate how to create "walking detection" models with various approaches. 
	* By Kevin Chao (kevinchao@gmail.com)
	* Latest updated on 2024-02-03

* Purpose:
	* The purpose of this project is to demonstrate how to create Machine Learning Models from raw accelerometer dataset. I use Walking Detection as an example.
	* The whole process aims to be simple and easy to understand the end-to-end pipeline of Data Science project.    

* Data:
	* the raw accelerometer data was download from: 
	* https://physionet.org/content/accelerometry-walk-climb-drive/1.0.0/
	* The sampling rate of the Acc data is 100 Hz 
	* Data including labeled activities of walking, stair climbing, and driving. 

* Source:
	* 01_data_understanding.ipynb
		* Jupyter notebook to show how to understand the raw accelerometer data and conduct simple quality control.
	* 02_data_preparation.ipynb
		* Show basic signal process steps to analize high-friquency accelerometer data. 
		* Show how to create a dataframe with various features
	* 03_modeling_evaluation.ipynb
		* Run Scikit-learn models and evaluate the model. 	
