import pymongo
from pymongo import MongoClient
from twilio.rest import Client

# Function to perform face recognition and object detection using TensorFlow
def recognize_person_and_object(image):
    # Your TensorFlow code for face recognition and object detection here
    person_detected = True  # Set to True if a person is recognized
    object_detected = True  # Set to True if an object is recognized
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

# Function to send SMS using Twilio
def send_sms(body):
    # Twilio account SID and authentication token
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    # Twilio phone number and recipient's phone number
    from_number = 'your_twilio_phone_number'
    to_number = 'recipient_phone_number'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to_number
    )

    print("SMS sent with SID:", message.sid)

# Global variables to track the state of person and object detections
person_detected_last_frame = False
object_detected_last_frame = False

# Main function to process images and update the database
def process_image(image):
    global person_detected_last_frame, object_detected_last_frame

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
        send_sms("Person left but object is still detected.")

    # Update the state for the next frame
    person_detected_last_frame = person_detected
    object_detected_last_frame = object_detected

# Example usage
image = "path_to_your_image.jpg"
process_image(image)

# Close the MongoDB connection
client.close()
