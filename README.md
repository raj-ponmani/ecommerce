# e-commerce
This is the new e-commerce project code repository.

## Setup

The first thing to do is to fork/clone the repository:
[From here](https://github.com/raj-ponmani/ecommerce.git)

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv venv
$ venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd ecommerce
(venv)$ python manage.py runserver
```

[comment]: <> (#####Jump Ahead)

need to create your superuser by `createsuperuser` command

```sh
(venv)$ python manage.py createsuperuser
```
To run `test` command

```sh
(venv)$ python manage.py test
```

### Project Structure.
Follow the below project

```tree
ecommerce/                    <- project root
├── ecommerce/                <- Django root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   ├── urls.py
│   └── wsgi.py
├── products/
│   └── __init__.py
├── manage.py
├── README.md
├── .gitignore
└── requirements.txt
```

# REST API ENDPOINTS

The REST API to the e-commerce app is described below.

## Get list of Products

### Request

`GET /api/product-list/`

### Response
    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    []

## Create a new Thing

### Request

`POST /api/product-list/`

### Response

    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "name": "Product Name",
        "description": "Product Description",
        "price": "250.00"
    }


### Project Code Guidelines
- Observe pep 8 rules https://www.python.org/dev/peps/pep-0008/
- Observe standard rules of a django project https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
- Keep functionality in separate files, e.g. signals to go to signals.py,
forms in forms.py etc.
- Use class based views while writing your views. Try as much as possible
to use django built in class based generic views. https://ccbv.co.uk/
- Comment on your code when you build custom functionality.
- Keep all functionality related to one app in the app only (unless otherwise).
- keep all templates in the templates/[app_name] directory.
- keep all static files in the static directory and in their respective
directory if css, js or media.
- Always supply an `upload_to` to a file field.
- Avoid repeating yourself.
- Use hyphens `(-)` in separating long names in urls.py e.g. `product-list/` not `product_list`  

### Debugging and Automated Testing
- Use django debug toolbar to optimize your queries.
- Write tests in the `tests` module under each app.
- Tests will be split into `test_forms.py`, `test_models.py`, `test_urls.py`, `test_views.py`
and test_[any_custom_extended_functionality].py for any custom functionality e.g for
custom `middleware` it will be `test_middleware.py`. These files will be in each `[app]/tests.`


- Use coverage as a guide to writing tests.
- Run tests using coverage:
```shell
$ coverage run --source='.' manage.py test
```
- Use coverage to check test coverage percentage:
```shell
$ coverage html
```
Then check the `htmlcov` folder in the project root as your guide to testing.

- Check code formatting issues using the following command in your terminal:
```shell
flake8
```


### File Naming.
- app_name should have short, all-lowercase names. Underscores can be
used in the module name if it improves readability. also should have a 
short name and it can be a plural and singular name.
- Use underscore `(_)` when separating template name. e.g. blog_list.html
- Templates should try as much as possible to describe the view they are 
linked with. E.g. for a create view, template name can be `blog_create.html`,
for a list view `blog_list.html` and update view `blog_update.html`.


### Contribution & Code Reviews
- Fork the project.
- Make contributions by creating well detailed pull requests on functions
worked on.
- Ensure all code formatting (flake8 linter) are running.
- Ensure you have written tests for your contribution and tests are running.
- Github workflows will help in checking for linter checks and tests before contributing.
- All code will be thoroughly reviewed before being merged.
- You may be expected to show up for a review process.
