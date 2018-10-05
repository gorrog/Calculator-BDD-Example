#!/bin/bash

docker build -t calculator-bdd-example .

docker run --rm calculator-bdd-example /bin/bash -c "cd calculator; python manage.py test"
