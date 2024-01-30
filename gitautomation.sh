#!/bin/bash

# Script to automate git add, commit, and push

# Run git add
git add .

# Run git commit with a specified commit message
echo -n "Enter your commit message: "
read commit_message
git commit -m "$commit_message"

# Prompt the user for the branch name
echo -n "Enter the branch name: "
read branch_name

# Run git push with the specified branch
git push origin "$branch_name"
