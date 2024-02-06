# walking-detection
* This is a project to demonstrate how to create "walking detection" models with various approaches. 
	* By Kevin Chao (kevinchao@gmail.com)
	* Latest updated on 2024-02-05

* Purpose:
	* The purpose of this project is to demonstrate how to create Machine Learning Models from raw accelerometer dataset. I use Walking Detection as an example.
	* The whole process aims to be simple and easy to understand the end-to-end pipeline of Data Science project.    

* Data:
	* The raw accelerometer data was download from: 
		* https://physionet.org/content/accelerometry-walk-climb-drive/1.0.0/
	* The sampling rate of the Acc data is 100 Hz 
	* Data including labeled activities of walking, stair climbing, and driving.
	* Types of activities:
		* 1=walking; 
		* 2=descending stairs; 
		* 3=ascending stairs; 
		* 4=driving; 
		* 77=clapping; 
		* 99=non-study activity
	* Device positions:
		* lw: left wrist
		* rw: right wrist
		* lh: left hip
		* rg: right hip
		* la: left ankle
		* ra: right ankle
	* The unit of accelerometer is in g (9.8 m/s^2)

* Source:
	* 01\_data\_understanding.ipynb
		* Jupyter notebook to show how to understand the raw accelerometer data, conduct simple quality control, and show data visualization.
	* 02\_data\_preparation\_time\_series\_analysis.ipynb
		* Show basic signal process steps to analize high-friquency  accelerometer data. 
		* Show algorithm to compute Step Count in both time and frequency domains
	* 03\_data\_preparation\_features\_creation.ipynb
		* Show how to create a dataframe with various features
	* 04\_modeling\_evaluation.ipynb
		* Run Scikit-learn models and evaluate the model. 
* Outputs:
	* Format of acc file:
		* **Columns:** 'subject\_id', 'device\_loc', 'act\_id', 'act\_name', 'event\_num', 'walk\_or\_not', 'unique\_id', 'time', 'acc\_x', 'acc\_y', 'acc\_z' 
		*  **Row:** idf1ce9a0f,	AnkleL,	1,	Walking,	1,	1,	idf1ce9a0f\_AnkleL\_1\_Walking\_1\_1,	354.05,	-0.070,	-0.973,	0.078
		*  .....
		*  **Row:** idf1ce9a0f,	AnkleL,	99,	NonStudyAct,	547,	0,	idf1ce9a0f\_AnkleL\_99\_NonStudyAct\_547\_0,	3282.01,	-0.059,	0.043,	0.992
