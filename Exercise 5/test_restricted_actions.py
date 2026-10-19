import docker


IMAGE = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-restrictions"


def main():
    client = docker.from_env()
    container = client.containers.run(
        IMAGE,
        name=CONTAINER_NAME,
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
    )

    try:
        print(f"Container started: {container.short_id}")
        for command, description in (
            ("cat /etc/passwd", "read /etc/passwd"),
            ("/bin/sh", "execute /bin/sh"),
        ):
            exit_code, output = container.exec_run(command)
            print(
                f"Attempt to {description}: "
                f"Exit Code {exit_code}, Output: {output.decode(errors='replace')}"
            )
    finally:
        container.stop()
        container.remove()
        print("Container stopped and removed")


if __name__ == "__main__":
    main()
