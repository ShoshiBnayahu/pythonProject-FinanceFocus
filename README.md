# FinanceFocus: Advanced Financial Management System in Python

FinanceFocus is a comprehensive financial management application designed to empower users to manage their monthly budget wisely. Developed in Python, FinanceFocus offers a user-friendly interface, powerful backend, and insightful features tailored for investors and individuals alike.

## Project Overview:

FinanceFocus serves as an essential tool for individuals looking to gain better control over their finances. With its intuitive design and robust functionalities, FinanceFocus simplifies financial management tasks, making it easier for users to track expenses, analyze trends, and make informed financial decisions.

### System Specification:

- **Database**: FinanceFocus utilizes MongoDB for efficient data management.
- **Server-side**: The backend development is powered by Python, ensuring reliability and scalability.

### Key Routes:

- **User Routes**: Register, login, update profile, and fetch user data seamlessly.
- **User Action Routes**: Create, update, delete user actions, and fetch action data effortlessly.
- **Visual Routes**: Retrieve data in visualization-friendly formats using matplotlib.

### Quality Assurance:

- **Testing**: FinanceFocus is rigorously tested to ensure optimal performance and reliability.
- **Logging**: A custom decorator logs system activities, providing valuable insights for troubleshooting.

## Installation and Usage:

To get started with FinanceFocus:

1. Clone the repository: `git clone https://github.com/ShoshiBnayahu/pythonProject-FinanceFocus.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## File Tree:

├── app
│   ├── models
│   │   ├── user.py                      # Defines the models of the application for users.
│   │   └── user_action.py               # Defines the models of the application for user actions.
│   ├── routes
│   │   ├── user_router.py               # Routes for users: registration, login, profile update, and fetching user objects.
│   │   ├── user_action_router.py        # Routes for user actions: creation, update, deletion, and fetching data of user actions.
│   │   └── visual_router.py             # Route for visualization: Option to retrieve data in a format suitable for visualization using matplotlib.
│   └── services
│       ├── Db_service.py                # Initializes a connection to the MongoDB server and accesses specific collections within the database.
│       ├── User_service.py              # Provides functions for managing users and access to the database for user_router.
│       ├── User_action_service.py       # Provides functions for managing user actions and access to the database for user_action_router.
│       └── Visual_service.py            # Provides functions for visual_router.
├── tests
│   ├── user_test.py                     # Defines unit tests for functions related to users in the application.
│   └── user_action_test.py              # Defines unit tests for functions related to user actions in the application.
├── utils
│   └── decorators.py                    # Defines a decorator for registration function.
├── main.py                              # Includes routes for various functions and is run using Uvicorn on localhost.
├── README.md
└── requirements.txt


## Feedback:

We welcome feedback and suggestions from users and developers. If you have any comments, questions, or ideas for improvement, please feel free to raise them. Your input helps us enhance FinanceFocus and deliver a better experience for all users.
