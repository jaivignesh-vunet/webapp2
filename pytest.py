import github

# Get the GitHub API client
client = github.Github()

# Get the current user
user = client.get_user()

# Get the organization name
organization_name = user.organization.login

# Get the repository name
repository_name = user.get_repo("my-repository").name

# Print the organization name and repository name
print(f"Organization name: {organization_name}")
print(f"Repository name: {repository_name}")
