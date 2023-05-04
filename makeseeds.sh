python manage.py dumpdata products --output products/seeds.json --indent=2;
python manage.py dumpdata categories --output categories/seeds.json --indent=2;
python manage.py dumpdata reviews --output reviews/seeds.json --indent=2;
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;