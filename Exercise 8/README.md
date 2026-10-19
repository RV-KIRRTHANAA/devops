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

