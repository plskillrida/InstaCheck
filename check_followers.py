import json

# Replace 'following.json' and 'followers_1.json' with your actual file names if they are different.
with open('following.json', 'r') as f_following, open('followers_1.json', 'r') as f_followers:
    following_data = json.load(f_following)
    followers_data = json.load(f_followers)

# Extract usernames from the following list
following_list = [user['string_list_data'][0]['value'] for user in following_data['relationships_following']]

# Extract usernames from the followers list
followers_list = [user['string_list_data'][0]['value'] for user in followers_data]

# Convert lists to sets for efficient comparison
following_set = set(following_list)
followers_set = set(followers_list)

# Find the users you follow who are not in your followers list
not_following_back = following_set.difference(followers_set)

# Print the result
print("Users you follow who are not following you back:")
for username in sorted(list(not_following_back)):
    print(username)
print(f"\nTotal users not following you back: {len(not_following_back)}")