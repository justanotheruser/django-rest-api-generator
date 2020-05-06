pushd ..
python setup.py sdist bdist_wheel
pip uninstall -y django-rag
pip install dist/django-rag-0.1.tar.gz
popd