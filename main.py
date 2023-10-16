#!/usr/bin/env python3
import click
import models
import logging

LOGGER = logging.getLogger("main")


@click.group()
def main():
    pass


@main.command()
def create_table():
    with models.DATABASE:
        models.DATABASE.create_tables(models.MODELS)
    LOGGER.info("Tables created")


@main.command()
@click.argument("username")
@click.option("--email", "-e", default="sao@gmail.com")
@click.option(
    "--password",
    "-p",
    prompt="Enter password",
    hide_input=True,
    confirmation_prompt=True,
)
@click.option("--active", "-a", is_flag=True, default=True)
def create_user(username, email, password, active):
    user = models.User.create(
        username=username, email=email, password=password, active=active)
    if user.id:
        LOGGER.info("User created")


if __name__ == "__main__":
    main()
