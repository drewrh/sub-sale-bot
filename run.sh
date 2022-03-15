COMPOSE_PATH=/volume1/GithubProjects/sub-sale-bot/docker-compose.yml
PROJECT_PATH=/volume1/GithubProjects/sub-sale-bot

cd ${PROJECT_PATH} && git pull
docker-compose -f ${COMPOSE_PATH} up --build --abort-on-container-exit && docker-compose -f ${COMPOSE_PATH} down
