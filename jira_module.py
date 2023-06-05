import jira

# Install the Jira Python API library
# pip install jira

# Create a Jira object
jira = jira.Jira()

# Set the Jira object's base URL and credentials
jira.base_url = "https://your-jira-server.com"
jira.username = "your-jira-username"
jira.password = "your-jira-password"

# Use the Jira object's get_user_stories() method to get a list of user stories
user_stories = jira.get_user_stories()

# Loop through the list of user stories and print the title and status of each user story
for user_story in user_stories:
    print(user_story.title, user_story.status)
