# github_amp (Assignment Implementation)

This repository contains code and step-by-step Git workflow instructions for all 3 questions.

## Screenshots

All execution screenshots are provided below in their respective sections.

## Repository Files

- `src/calculator_plus.py` -> Q1 app with `square_root` and divide-by-zero bug fix.
- `src/geometry_calculator.py` -> Q3 app with circle and rectangle area features.
- `tests/test_calculator_plus.py` -> Q1 test script.
- `tests/test_geometry_calculator.py` -> Q3 test script.
- `docs/submission_link.txt` -> Put your private GitHub repository link here for Vlearn upload.

## Prerequisites

- Python 3.9+
- Git
- Git LFS (for Q2)

## Q1: CalculatorPlus Workflow

### 1) Create private GitHub repo

Manual:

1. Create private repository named `github_amp` on GitHub.
2. Add this project code to that repository.

### 2) Initialize and push main branch

```bash
cd github_amp
git init
git add .
git commit -m "Initial assignment scaffold"
git branch -M main
git remote add origin <YOUR_PRIVATE_REPO_URL>
git push -u origin main
```

### 3) Create `dev` branch and add calculator code

```bash
git checkout -b dev
git add src/calculator_plus.py tests/test_calculator_plus.py
git commit -m "Add CalculatorPlus base code"
git push -u origin dev
```

### 4) Merge `dev` to `main` and create release v1

```bash
git checkout main
git merge dev
git push origin main
git tag -a v1.0 -m "Version 1 release"
git push origin v1.0
```

Manual on GitHub:

1. Open Releases -> Draft a new release.
2. Select tag `v1.0` and publish release notes.

### 5) Add classmate as collaborator

Manual on GitHub:

1. Repo `Settings` -> `Collaborators and teams`.
2. Invite your classmate by GitHub username.

### 6) Create feature branch `feature/sqrt`

```bash
git checkout dev
git checkout -b feature/sqrt
# Verify square_root exists in src/calculator_plus.py
git add src/calculator_plus.py tests/test_calculator_plus.py
git commit -m "Implement square_root feature"
git push -u origin feature/sqrt
```

### 7) Critical bug fix on `dev` (divide by zero)

```bash
git checkout dev
# Ensure divide uses:
# if b == 0: raise ValueError("Cannot divide by zero.")
git add src/calculator_plus.py tests/test_calculator_plus.py
git commit -m "Fix divide by zero bug"
git push origin dev
```

### 8) Keep `feature/sqrt` up to date with `dev`

```bash
git checkout feature/sqrt
git merge dev
# Resolve conflicts if any
git push origin feature/sqrt
```

### 9) Create PR, review, update, merge to `dev`

Manual on GitHub:

1. Create PR: `feature/sqrt` -> `dev`.
2. Request classmate review.
3. Apply feedback commits on `feature/sqrt`.
4. Merge PR after approval.

### 10) Test in `dev`, merge to `main`, create v2 release

```bash
git checkout dev
python3 src/calculator_plus.py
python3 tests/test_calculator_plus.py


git checkout main
git merge dev
git push origin main
git tag -a v2.0 -m "Version 2 release"
git push origin v2.0
```

Manual on GitHub:

1. Publish release for tag `v2.0`.

### Q1 Workflow Screenshots

![Q1 Step 1 - Create Repository](images/image-1d.png)
*Creating the private GitHub repository*

![Q1 Step 2 - Initialize and Push](images/image-2d.png)
*Initializing and pushing the main branch*

![Q1 Step 3 - Create Dev Branch](images/image-3d.png)
*Creating and setting up the dev branch*

![Q1 Step 4 - Merge and Release v1](images/image-4d.png)
*Merging dev to main and creating v1.0 release*

![Q1 Step 5 - Add Collaborator](images/image-5d.png)
*Adding classmate as collaborator*

![Q1 Step 6 - Feature Branch](images/image-6d.png)
*Creating feature/sqrt branch*

![Q1 Step 7 - Bug Fix](images/image-7d.png)
*Critical bug fix on dev branch*

![Q1 Step 8 - Update Feature Branch](images/image-8d.png)
*Keeping feature branch up to date with dev*

![Q1 Step 9 - PR and Merge](images/image-9d.png)
*Creating PR, reviewing, and merging to dev*

## Q2: Git LFS for Large Binary File

Create and use branch `lfs`.

```bash
git checkout -b lfs
git lfs install
git lfs track "*.bin"
git add .gitattributes
git commit -m "Configure Git LFS for binary files"
```


Create a 210MB sample file and push with LFS:

```bash
mkdir -p large_files
fallocate -l 210M large_files/sample_210mb.bin
# If fallocate is unavailable, use: dd if=/dev/zero of=large_files/sample_210mb.bin bs=1M count=210

git add large_files/sample_210mb.bin
git commit -m "Add 210MB binary file tracked by Git LFS"
git push -u origin lfs
```


Verify LFS tracking:

```bash
git lfs ls-files
cat .gitattributes
```

Clone verification on another machine (manual):

```bash
git clone <YOUR_PRIVATE_REPO_URL>
cd github_amp
git checkout lfs
git lfs pull
ls -lh large_files/sample_210mb.bin
```

### Q2 Git LFS Screenshots

![Q2 Step 1 - LFS Setup](images/image-1.png)
*Setting up Git LFS*

![Q2 Step 2 - Track Binary Files](images/image-8.png)
*Configuring LFS to track binary files*

![Q2 Step 3 - Create Large File](images/image-9.png)
*Creating 210MB sample file*

![Q2 Step 4 - Push with LFS](images/image-10.png)
*Pushing large file with LFS*

![Q2 Step 5 - Verify LFS](images/image-11.png)
*Verifying LFS tracking*

![Q2 Step 6 - Clone Verification](images/image-12.png)
*Cloning and pulling LFS files*

## Q3: Geometry Calculator + Git Stash Workflow

### 1) Create base branch

```bash
git checkout dev
git checkout -b geometry-calculator
git add src/geometry_calculator.py tests/test_geometry_calculator.py
git commit -m "Add geometry calculator base"
git push -u origin geometry-calculator
```

### 2) Circle feature branch with stash

```bash
git checkout -b feature/circle-area
# Start editing circle-area related lines
git stash push -m "WIP circle area"
git status
```

### 3) Rectangle feature branch with stash

```bash
git checkout geometry-calculator
git checkout -b feature/rectangle-area
# Start editing rectangle-area related lines
git stash push -m "WIP rectangle area"
git status
```

### 4) Complete circle feature

```bash
git checkout feature/circle-area
git stash list
git stash pop
# Complete circle area implementation
git add src/geometry_calculator.py tests/test_geometry_calculator.py
git commit -m "Complete circle area feature"
git push -u origin feature/circle-area
```

### 5) Complete rectangle feature

```bash
git checkout feature/rectangle-area
git stash list
git stash pop
# Complete rectangle area implementation
git add src/geometry_calculator.py tests/test_geometry_calculator.py
git commit -m "Complete rectangle area feature"
git push -u origin feature/rectangle-area
```

### 6) Create PRs and merge

Manual on GitHub:

1. Create PR `feature/circle-area` -> `dev`.
2. Create PR `feature/rectangle-area` -> `dev`.
3. Request review from teammate/classmate.
4. Merge both after approval.

Then merge `dev` -> `main` and push.

### Q3 Geometry Calculator Screenshots

![Q3 Step 1 - Create Base Branch](images/image-13.png)
*Creating geometry-calculator base branch*

![Q3 Step 2 - Circle Feature Branch](images/image-14.png)
*Creating feature/circle-area branch with stash*

![Q3 Step 3 - Rectangle Feature Branch](images/image-15.png)
*Creating feature/rectangle-area branch with stash*

![Q3 Step 4 - Complete Circle Feature](images/image-16.png)
*Completing circle area feature*

![Q3 Step 5 - Complete Rectangle Feature](images/image-17.png)
*Completing rectangle area feature*

![Q3 Step 6 - Create PRs](images/image-18.png)
*Creating pull requests*

![Q3 Step 7 - Merge PRs](images/image-19.png)
*Merging pull requests*

## Commands to Capture Terminal Outputs for Report

Run these and save screenshots/output:

```bash
cd github_amp
python3 src/calculator_plus.py
python3 tests/test_calculator_plus.py
python3 src/geometry_calculator.py
python3 tests/test_geometry_calculator.py
git log --oneline --decorate --graph --all -n 25
git branch -a
git tag
git lfs ls-files
```

### Terminal Output Screenshot

![Terminal Output - Final Results](images/image-20.png)
*Final terminal output summary showing git log, branches, tags, and LFS files*

# Thus concluding the assignment git operations on github
