How to contribute to ModelServe Pro, the GitHub repository?
The client library, huggingface_hub

Follow these steps to start contributing:

Fork the repository by clicking on the 'Fork' button on the repository's page. This creates a copy of the code under your GitHub user account.

Clone your fork to your local disk, and add the base repository as a remote. The following command assumes you have your public SSH key uploaded to GitHub. See the following guide for more information.

$ git clone git@github.com:<your Github handle>/Gen-AI-SEM.git
$ cd modelserve_pro
$ git remote add upstream https://github.com/modelserve_pro/Gen-AI-SEM.git
Create a new branch to hold your development changes, and do this for every new PR you work on.

Start by synchronizing your main branch with the upstream/main branch (more details in the GitHub Docs):

$ git checkout main
$ git fetch upstream
$ git merge upstream/main
Once your main branch is synchronized, create a new branch from it:

$ git checkout -b a-descriptive-name-for-my-changes
Do not work on the main branch.
