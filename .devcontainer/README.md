# .devcontainer notes

This devcontainer is configured to use the official TypeScript devcontainer image:

```json
{
  "image": "mcr.microsoft.com/devcontainers/typescript-node"
}
```

If you want to build a custom image using the included Dockerfile, build it from the *workspace root* (so the `Main/src/test-node.js` file is available to COPY):

```powershell
# run from project root (C:\kyaserver)
docker build -f .devcontainer/Dockerfile -t kyaserver:latest .
```

The Dockerfile will use the same TypeScript devcontainer base image and copy `Main/src/test-node.js` into `/app`.

Note: `devcontainer.json` uses the prebuilt image by default to keep the development environment fast and consistent. Use the manual build only if you need a standalone Docker image.

# Собрать образ (запускать из корня репозитория C:\kyaserver)
docker build -f .devcontainer\Dockerfile -t kyaserver:latest .

# Запустить контейнер и пробросить порт
docker run --rm -p 3010:3010 kyaserver:latest

# Или в фоне, с проверкой логов:
docker run --rm -d -p 3010:3010 --name kyaserver-test kyaserver:latest
docker logs kyaserver-test
docker stop kyaserver-test