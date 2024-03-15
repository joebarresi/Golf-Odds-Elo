import boto3
import requests

# Create a new event using the CloudWatch event template (cloudwatch-scheduled-event)
def lambda_handler(event : any, context: any):

    # Create DynamoDB Client and open table
    dynamodb = boto3.resource("dynamodb")
    table_name = "min_odds"
    table = dynamodb.Table(table_name)

    # Convert each row of Json as item to put in DB


    # Group item in batches of 25 (Max amount you can put at a time)

    # Perform batch write operations

   

    return {"message" : "Success"}


if __name__ == "__main__" : 
    print(lambda_handler(None, None))