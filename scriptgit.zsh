#!/bin/zsh

# Prompt user for commit message
echo "Enter commit message:"
read commit_message

# Add all changes
git add .

# Commit with the user-provided message
git commit -m "$commit_message"

echo "Changes committed successfully."
