=====
RAG (REST API Generator)
=====

RAG app allows to generate basic JSON REST API for every model in your project

Quick start
-----------

1. Add "rag" and its dependencies to your INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_filters',
        'rag',
    ]

2. Run ``python manage.py generateapi <your_app_with_models>`` to create code for serializers and views

3. In the root of your project add the following to urls.py:

urlpatterns = [
    ...   
    path('api/', include('your_app_with_models.urls')),
    ]

4. Start the server and checkout http://127.0.0.1:8000/api/your_app_with_models


For developers
--------------

test_project folder contains demo project and tests (both for command and for generated API). Because tests for API need, well, generated API, use ``.\run_tests.bat`` instead of usual ``python manage.py`` - it will run ``python manage.py generateapi player`` first