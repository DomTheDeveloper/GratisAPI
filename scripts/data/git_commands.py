"""Common Git commands grouped by workflow category."""

META = {
    "name": "git_commands",
    "title": "Git Commands",
    "description": "Common Git version control commands grouped by workflow stage.",
    "emoji": "\U0001F500",
}

ITEMS = [
    # --- Setup ---
    {
        "id": "git-init",
        "command": "git init",
        "category": "Setup",
        "description": "Create an empty Git repository or reinitialize an existing one in the current directory.",
    },
    {
        "id": "git-clone",
        "command": "git clone",
        "category": "Setup",
        "description": "Clone a repository into a new directory, copying its full history and setting up remote tracking.",
    },
    {
        "id": "git-config",
        "command": "git config",
        "category": "Setup",
        "description": "Get and set repository or global configuration options such as user name and email.",
    },
    # --- Snapshot ---
    {
        "id": "git-add",
        "command": "git add",
        "category": "Snapshot",
        "description": "Stage changes in the working directory for inclusion in the next commit.",
    },
    {
        "id": "git-status",
        "command": "git status",
        "category": "Snapshot",
        "description": "Show the working tree status, including staged, unstaged, and untracked files.",
    },
    {
        "id": "git-commit",
        "command": "git commit",
        "category": "Snapshot",
        "description": "Record the staged changes to the repository along with a descriptive message.",
    },
    {
        "id": "git-diff",
        "command": "git diff",
        "category": "Snapshot",
        "description": "Show changes between commits, the working tree, and the staging area.",
    },
    {
        "id": "git-reset",
        "command": "git reset",
        "category": "Snapshot",
        "description": "Unstage files or move the current branch to a different commit, optionally altering the working tree.",
    },
    {
        "id": "git-rm",
        "command": "git rm",
        "category": "Snapshot",
        "description": "Remove files from the working tree and the staging area.",
    },
    {
        "id": "git-mv",
        "command": "git mv",
        "category": "Snapshot",
        "description": "Move or rename a file, directory, or symlink while staging the change.",
    },
    {
        "id": "git-stash",
        "command": "git stash",
        "category": "Snapshot",
        "description": "Temporarily shelve uncommitted changes so you can work on something else, then reapply them later.",
    },
    {
        "id": "git-restore",
        "command": "git restore",
        "category": "Snapshot",
        "description": "Restore working tree files to a previous state or unstage changes.",
    },
    # --- Branching ---
    {
        "id": "git-branch",
        "command": "git branch",
        "category": "Branching",
        "description": "List, create, or delete branches.",
    },
    {
        "id": "git-checkout",
        "command": "git checkout",
        "category": "Branching",
        "description": "Switch branches or restore working tree files.",
    },
    {
        "id": "git-switch",
        "command": "git switch",
        "category": "Branching",
        "description": "Switch to an existing branch or create a new one, a modern alternative to checkout.",
    },
    {
        "id": "git-merge",
        "command": "git merge",
        "category": "Branching",
        "description": "Join two or more development histories together into the current branch.",
    },
    {
        "id": "git-rebase",
        "command": "git rebase",
        "category": "Branching",
        "description": "Reapply commits on top of another base tip to produce a linear history.",
    },
    {
        "id": "git-tag",
        "command": "git tag",
        "category": "Branching",
        "description": "Create, list, or delete tags that mark specific points in history, such as releases.",
    },
    {
        "id": "git-cherry-pick",
        "command": "git cherry-pick",
        "category": "Branching",
        "description": "Apply the changes introduced by one or more existing commits onto the current branch.",
    },
    # --- Sharing ---
    {
        "id": "git-fetch",
        "command": "git fetch",
        "category": "Sharing",
        "description": "Download objects and refs from a remote repository without merging them.",
    },
    {
        "id": "git-pull",
        "command": "git pull",
        "category": "Sharing",
        "description": "Fetch from a remote repository and integrate the changes into the current branch.",
    },
    {
        "id": "git-push",
        "command": "git push",
        "category": "Sharing",
        "description": "Upload local commits and refs to a remote repository.",
    },
    {
        "id": "git-remote",
        "command": "git remote",
        "category": "Sharing",
        "description": "Manage the set of tracked remote repositories.",
    },
    # --- Inspection ---
    {
        "id": "git-log",
        "command": "git log",
        "category": "Inspection",
        "description": "Show the commit history for the current branch.",
    },
    {
        "id": "git-show",
        "command": "git show",
        "category": "Inspection",
        "description": "Display details about a commit, tag, or other Git object, including its diff.",
    },
    {
        "id": "git-blame",
        "command": "git blame",
        "category": "Inspection",
        "description": "Show what revision and author last modified each line of a file.",
    },
    {
        "id": "git-reflog",
        "command": "git reflog",
        "category": "Inspection",
        "description": "Show a log of where the branch tips and HEAD have pointed, useful for recovering lost commits.",
    },
    {
        "id": "git-bisect",
        "command": "git bisect",
        "category": "Inspection",
        "description": "Use binary search through the commit history to find the commit that introduced a bug.",
    },
    {
        "id": "git-grep",
        "command": "git grep",
        "category": "Inspection",
        "description": "Search tracked files in the working tree or a commit for lines matching a pattern.",
    },
    {
        "id": "git-clean",
        "command": "git clean",
        "category": "Snapshot",
        "description": "Remove untracked files from the working tree.",
    },
]
