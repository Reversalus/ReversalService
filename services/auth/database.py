from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError
import os 
import random
from datetime import datetime, timedelta


# create the .env path manually
envpath = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path=envpath)


aws_region = os.getenv('AWS_REGION')

dynamodb = boto3.resource('dynamodb', region_name=aws_region)

# inst a table.
otp_table = dynamodb.Table('otp')

# generates a random otp.
def generate_otp():
    return random.randint(100000,999999)

# inserts a new otp into the table.
def storeOTP(mobile_number):
    otp = generate_otp()
    now = datetime.now()
    expiry_time = now + timedelta(minutes=5)
    try:
        # first check if the otp is already generated
        response = otp_table.get_item(
            Key={
                'mobile_number': mobile_number
            }
        )
        item = response.get('Item',{})

        if item:
            last_resend_time = datetime.fromisoformat(item['last_resend_at'])
            resend_count = item['resend_count']

            # check resend limit (max 2 tries per hour)
            if resend_count >= 2 and now - last_resend_time < timedelta(hours=1):
                return {"error": "Too many OTP requests. Please wait."}

            # update the user table
            response = otp_table.update_item(
                Key={'mobile_number': mobile_number},
                UpdateExpression="set otp = :otp, otp_expiry_at = :expiry_time, resend_count = resend_count + :val, last_resend_at = :now",
                ExpressionAttributeValues={
                    ':otp': otp,
                    ':expiry_time': expiry_time.isoformat(),
                    ':val': 1,
                    ':now': now.isoformat()
                },
                ReturnValues="UPDATED_NEW"
                )
        else:
            # insert new user and otp in table
            response = otp_table.put_item(
                Item={
                    'mobile_number': mobile_number,
                    'otp': otp,
                    'created_at': now.isoformat(),
                    'otp_expiry_at': expiry_time.isoformat(),
                    'resend_count': 1,
                    'last_resend_at': now.isoformat()
                }
            )
        
        print(f'insertion in table ${response}')

    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    finally:
        return True

# fetches the otp from the table. 
def getOTP(mobile_number):
    response = otp_table.get_item(
        Key={
            'mobile_number': mobile_number
        }
    )
    return response['Item']

# used for deleting the otp.
def deleteOTP(mobile_number):
    response = otp_table.delete_item(
        Key={
            'mobile_number': mobile_number
        }
    )
    return response

# verify the otp.
def verifyOTP(otpPayload):
    response = otp_table.get_item(
        Key={
            'mobile_number': otpPayload.phone_number
        }
    )
    item = response.get('Item',{})
    if item and item['otp'] == otpPayload.otp:
        deleteOTP(otpPayload.phone_number)
        return True
    return False