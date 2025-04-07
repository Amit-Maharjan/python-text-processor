# 📝 Python Text Processor

This is a simple Python application that reads input from a text file, processes it, and writes the output to another file. The app supports Continuous Integration (CI), GitHub Releases, and Docker-based deployment.

---

## 📦 Features

- Reads input from `input.txt`
- Processes content (Count number of words & transforms text to upper case)
- Outputs results to `output.txt`
- Includes tests and linting
- Dockerized for easy deployment
- GitHub Actions workflows:
  - CI (test, lint)
  - Release (zip + GitHub release)
  - Docker deploy (build and push to GitHub Container Registry)