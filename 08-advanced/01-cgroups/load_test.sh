#!/bin/bash

# Цвета для вывода
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Docker Resource Limits Test ===${NC}"
echo -e "${BLUE}This script will help you test resource limits on your containers${NC}"
echo

# Тест 1: Проверка ограничений CPU
echo -e "${YELLOW}Test 1: Checking CPU limits${NC}"
echo "Running 'docker stats' for 10 seconds to observe CPU usage..."
docker stats --no-stream &
STATS_PID=$!
sleep 10
kill $STATS_PID
echo

# Тест 2: Проверка ограничений памяти
echo -e "${YELLOW}Test 2: Checking memory limits${NC}"
echo "Starting a simple memory usage test..."

for container in api-service data-processor background-service limited-db; do
    echo -e "${BLUE}Container: $container${NC}"
    docker exec $container bash -c "cat /sys/fs/cgroup/memory/memory.limit_in_bytes" 2>/dev/null || \
    docker exec $container sh -c "cat /sys/fs/cgroup/memory/memory.limit_in_bytes" 2>/dev/null || \
    echo -e "${RED}Could not access memory limits for $container${NC}"
    echo
done

# Тест 3: Проверка ограничений I/O
echo -e "${YELLOW}Test 3: Checking I/O limits for limited-db${NC}"
echo "I/O limits are harder to verify directly, but we can check the configuration:"
docker inspect --format='{{json .HostConfig.BlkioDeviceReadBps}}' limited-db
docker inspect --format='{{json .HostConfig.BlkioDeviceWriteBps}}' limited-db
echo

echo -e "${GREEN}=== Tests completed ===${NC}"
echo -e "${BLUE}Для более детального мониторинга вы можете использовать 'docker stats'${NC}"
echo -e "${BLUE}Remember to observe resource usage under load for a realistic assessment.${NC}"
