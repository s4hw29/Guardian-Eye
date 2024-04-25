import pymongo
from pymongo import MongoClient

# Function to perform face recognition and object detection using TensorFlow
def recognize_person_and_object(image):
    # Your TensorFlow code for face recognition and object detection here
    person_detected = True  # Set to True if a person is recognized
    object_detected = True  # Set to True if an object is recognizeds
    return person_detected, object_detected

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Replace 'localhost' and '27017' with your MongoDB host and port if they are different

# Access your database
db = client['your_database_name']

# Access your collection
collection = db['your_collection_name']

# Function to insert data into MongoDB
def insert_data(data):
    insert_result = collection.insert_one(data)
    print("Data inserted with ID:", insert_result.inserted_id)

# Global variable to track the state of person detection
person_detected_last_frame = False

# Main function to process images and update the database
def process_image(image):
    global person_detected_last_frame

    person_detected, object_detected = recognize_person_and_object(image)

    if person_detected and object_detected:
        # Both person and object detected
        data_to_insert = {
            'person': 'person_info_here',
            'object': 'object_info_here',
            # Other fields related to the recognition results
        }
        insert_data(data_to_insert)
    elif not person_detected and object_detected and person_detected_last_frame:
        # Person left but object is still there
        print("Person left but object is still detected.")

    # Update the state for the next frame
    person_detected_last_frame = person_detected

# Example usage
image = "path_to_your_image.jpg"
process_image(image)

# Close the MongoDB connection
client.close()
