import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the data from CSV files
print('Loading data...')
lift_data = pd.read_csv('mpu_data.csv')
squat_data = pd.read_csv('mpu_data_squat.csv')
print('Data loaded.')

print('Preparing data...')
# Add labels to the data
lift_data['label'] = 0  # 0 represents lift
squat_data['label'] = 1  # 1 represents squat

# Combine the datasets
combined_data = pd.concat([lift_data, squat_data], ignore_index=True)

# Separate features and labels
X = combined_data.drop(['label', 'mpu_address'], axis=1)
y = combined_data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print('Training...')
# Create a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

print('Calculating Eval Metrics...')
# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")

print('Saving model...')
# Save the trained model to a file
joblib.dump(rf_model, 'motionsense_squad_or_lift_model.pkl')
print('Model saved.')
