export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

build:
	docker-compose build

up: build
	docker-compose up -d

client-test: up
	docker-compose run --rm --no-deps --entrypoint=pytest client -s tests

serving-test: up
	docker-compose run --rm --no-deps --entrypoint=pytest serving -s tests

unit-test: client-test serving-test

integration-test: up
	docker-compose run --rm --no-deps --entrypoint=pytest integration -s tests

test: unit-test integration-test

down:
	docker-compose down --remove-orphans

all: down build up test
