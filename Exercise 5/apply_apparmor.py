from pathlib import Path

import docker


IMAGE = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-sdk"


def main():
    client = docker.from_env()
    project_dir = Path(__file__).resolve().parent

    print("Building image from Dockerfile...")
    client.images.build(path=str(project_dir), tag=IMAGE)

    container = client.containers.run(
        IMAGE,
        name=CONTAINER_NAME,
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
    )

    try:
        print(f"Container started: {container.short_id}")
        container_info = client.api.inspect_container(container.id)
        security_options = container_info["HostConfig"].get("SecurityOpt", [])
        print(f"AppArmor profile applied: {security_options}")
    finally:
        container.stop()
        container.remove()
        print("Container stopped and removed")


if __name__ == "__main__":
    main()
