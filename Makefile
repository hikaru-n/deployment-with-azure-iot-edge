export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

build:
	docker-compose build

up:
	docker-compose up -d

client-test:
	docker-compose run --rm --no-deps --entrypoint=pytest client tests

serving-test:
	docker-compose run --rm --no-deps --entrypoint=pytest serving tests

unit-test: client-test serving-test

integration-test: up
	docker-compose run --rm --no-deps --entrypoint=pytest client -s /app/tests

test: unit-test integration-tests

down:
	docker-compose down --remove-orphans

all: down build up test
