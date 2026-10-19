# Exercise 8: Create a Hello World Jenkins Job

Publish a shell script to GitHub and configure a Jenkins Freestyle job to run
it.

## Phases

1. Create and commit the `hello-world.sh` script locally.
2. Publish the script to GitHub using a secure Personal Access Token.
3. Configure and run the Jenkins Freestyle job, then verify the console output.

## Phase 1: Create the Script Locally

The script is located at [hello-world.sh](hello-world.sh) and prints:

```text
Hello, Jenkins!
```

From the Exercise 8 directory, initialize a Git repository and commit the
script:

```bash
git init
git add hello-world.sh
git update-index --chmod=+x hello-world.sh
git status
git commit -m "Add hello-world.sh"
```

Configure your Git identity first if required:

```bash
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

## Phase 2: Publish the Script to GitHub

Create a public GitHub repository named `devops-sample-code` from your GitHub
account. Create a fine-grained Personal Access Token with the minimum
repository contents permission needed to push to that repository.

From the Exercise 8 directory, connect the local repository to GitHub:

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/devops-sample-code.git
git remote -v
```

Push the commit:

```bash
git push -u origin main
```

When Git prompts for credentials, enter your GitHub username and use the PAT
as the password. Do not place the PAT in the remote URL, script files, or
repository contents.

Verify that `hello-world.sh` is visible in the GitHub repository before moving
to Phase 3.

