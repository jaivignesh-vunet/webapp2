import os

# Get organization and repository details from environment variables
organization_name = os.environ["ORG_NAME"]
repository_name = os.environ["REPO_NAME"]

# Print organization and repository details
print("Organization: ", organization_name)
print("Repository: ", repository_name)
