run:
	@uvicorn main:app --reload

create-migration:
	@PYTHONPAH=$PYTHON:$(pwd) alembic revision --autogenerate -m "$(d)"

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head