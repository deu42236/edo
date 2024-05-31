# EdoScraper

This is a Python project that interacts with Google Calendar API and Edookit.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- Google Calendar API
- Edookit

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository
2. Install the required packages using pip:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

- You can either use mine instance on Google Cloud. If you want to use mine, contact me on discord: ```danieldeut```
- If you want to create your own, follow this tutorial and replace ```credentials.json```

### Run
- Change ```calID``` to your own, if you want to use your accounts default calendar, set it to ```"primary"```
- Follow instructions in ```keys.py```
- Run ```calendarWriter```