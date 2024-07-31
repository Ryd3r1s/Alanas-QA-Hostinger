# Alanas-QA-Hostinger

This project is designed for automated testing using `Selenium` and `pytest` with Python. Below is a step-by-step guide on how to set up the environment, install dependencies, and run tests.

## Dependencies

This project requires the following Python libraries:
- `selenium`
- `faker`
- `pytest`

All dependencies are listed in the `requirements.txt` file.

## Installation

1. **Clone the repository**

   First, clone the repository to your local machine:

   ```sh
   git clone https://github.com/Ryd3r1s/Alanas-QA-Hostinger.git
   cd Alanas-QA-Hostinger
   
2. **Create and activate a virtual environment**

    Create and activate a virtual environment:

   -`Windows`

    ```sh
    python -m venv venv
    .\venv\Scripts\activate 
   ```
   
   -`Mac/Linux`
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies**
   
   Install all required libraries using the requirements.txt file:
   ```sh
   pip install -r requirements.txt
   
4. **Run tests**

   To run tests, use the following command in the terminal:

   ```sh
   pytest
   ```

   **Authors**

   Alanas Šulskis