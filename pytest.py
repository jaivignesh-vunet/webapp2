import os
from mailjet_rest import Client

# Get organization and repository details from environment variables
organization_name = os.environ["ORG_NAME"]
repository_name = os.environ["REPO_NAME"]

# Print organization and repository details
print("Organization: ", organization_name)
print("Repository: ", repository_name)

# Mailjet API credentials
api_key = 'a3b5cc403bfafe0015e8ed624eebe264'
api_secret = '5d83255794ebdaf095f1837f72d8c37c'

# Instantiate the Mailjet client
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

# Email parameters
sender_email = 'jaivignesh@vunetsystems.com'
sender_name = 'Jay'
recipient_email = '20pc17@psgtech.ac.in'
subject = 'A commit is made with the organization code'
text_part = 'Organization: '+organization_name+' Repository: '+repository_name

# Create the email body
email = {
    'Messages': [
        {
            'From': {
                'Email': sender_email,
                'Name': sender_name
            },
            'To': [
                {
                    'Email': recipient_email
                }
            ],
            'Subject': subject,
            'TextPart': text_part,
        }
    ]
}

# Send the email
response = mailjet.send.create(data=email)
print(response.status_code)
print(response.json())
print ("hello")
