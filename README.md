#Incling Django Test

My submission for the Django Test:

> The task is to therefore create a three model Django project that contains school objects, classroom objects, and student objects. A student can belong only to one classroom and a classroom only relates to a single school.

> We do not need to know subjects that pupils might be taking, or any results, grades, or exams they might be associated with, so these should not be included within the above models.

> You can build the project using just Django with the above models CRUD being managed by the Django Admin. No frontend work is required on this task.


##Features

0. The imports in the code are all sorted alphabetially using `isort`.

0. The code is PEP8 compliant. Checked using `flake8`.

##Installation

    git clone https://github.com/JRodDynamite/incling-test
    cd incling-test
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py runserver
