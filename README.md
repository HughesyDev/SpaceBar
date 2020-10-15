# SpaceBar

SpaceBar is my personal take on the "BrewApp" mini-project I was assigned to build during my Junior Data Engineering Bootcamp.

---

#### My Environment

My development machine runs Windows, if you use another OS such as a Mac or Linux system then the below commands may differ. 

#### Virtual Environment
  - To create the virtual environment after pulling this project run the below from the root of the app:
  `python -m venv .venv`

  - Then, to activate the virtual environment, run the below from the project root:
  `source .venv/Scripts/activate`


#### Requirements
  - To install the requirements run the below from the root of the app:
    - Ensure the virtual environment is activated beforehand.
  `pip -m install requirements.txt`
    - An unknown factor sometimes causes an error that the "cryptography" package is missing when running the app. This doesn't always appear but can be installed using the below command:
  `pip install cryptography`

#### Running the app
  -  To begin running the app, run the below from the root of the project:
  `python -m src.app`