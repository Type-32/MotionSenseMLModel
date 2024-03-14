# MotionSense Posture Sensing Machine Learning Model

Made by **Type-32**

**All Rights Reserved, CRTL Prototype Studios 2023~2025**

***

## Current Models

Currently we have a basic posture sensing model based off of only 1.1k gyroscopic data with two node points (i.e. double MPU-5060 recorded data).

It is sufficient enough to produce a Squat-or-Lift ML Prediction Model based off of the _Random Forest Classifier_ Algorithm. We chose to use this algorithm is because of it is fast and quick in training, while being necessarily precise enough to generate good test results.

***

### motionsense_sor_model_1.1k.pkl (2024-03-15)

The 1.1k parameter prediction model that predicts whether the two-node-point gyroscopic data recorded is a squat motion or lifting motion.

> ### Metrics (0~1)
> 
> Accuracy: 0.7156
> 
> Precision: 0.7054
> 
> Recall: 0.7182
> 
> F1-score: 0.7117