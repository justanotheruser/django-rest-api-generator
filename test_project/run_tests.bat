call .\install_rag.bat
copy .\player\default_urls.py .\player\urls.py
python manage.py generateapi player
python manage.py test