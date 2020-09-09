run-app:
	cd webapp && python manage.py runserver

pull-and-deploy-prod:
	docker rmi kleinkauff/nexttune-webapp:latest --force && docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up --build -d