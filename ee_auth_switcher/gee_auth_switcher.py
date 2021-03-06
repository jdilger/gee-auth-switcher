# gee_auth_switcher.py
'''WorkPLAN!

    select users *
    show users
    show current account
    add user
    change config path
    '''
import os
import shutil
import typer
import subprocess

home_folder = os.path.expanduser(os.getenv('USERPROFILE'))
CONFIG_PATH = f"{home_folder}\\.config\\earthengine"
CREDENTIALS = f"{CONFIG_PATH}\\credentials"
USERS = [f for f in os.listdir(
    CONFIG_PATH) if os.path.isdir(f"{CONFIG_PATH}\\{f}")]


app = typer.Typer()


def select_user(name: str) -> None:
    new_credentials = f"{CONFIG_PATH}\\{name}\\credentials"
    assert os.path.isfile(
        new_credentials), f"Credentials for {name} do not exist"
    shutil.copyfile(new_credentials, CREDENTIALS)


def return_users(config_path: str = USERS) -> list:
    return USERS


def read_file(path: str):
    with open(path, 'r') as f:
        lines = f.read()
    return lines


def search_users():

    activated_user = 'UNKNOWN'
    crds = read_file(CREDENTIALS)

    for user in USERS:
        user_path = f"{CONFIG_PATH}\\{user}\\credentials"
        user_crds = read_file(user_path)

        if crds == user_crds:
            activated_user = user
            break

    return activated_user


@app.command()
def authenticate_user():
    '''authenticate an earth engine account. overrides any current credentials
    '''
    subprocess.call(['earthengine', 'authenticate'])


@app.command()
def make_new_user():
    """
    Add a new user account to select from
    """
    account_short_hand = typer.prompt("short hand name for account:")
    os.makedirs(f"{CONFIG_PATH}\\{account_short_hand}")
    authenticate_user()
    new_credentials = f"{CONFIG_PATH}\\{account_short_hand}\\credentials"
    shutil.copyfile(CREDENTIALS, new_credentials)


@app.command()
def check_activated_user():
    ''' 
        Check to see which GEE account is activated
    '''
    activated_user = search_users()

    if activated_user in USERS:
        typer.echo(f"Activated account is: {activated_user}")
    else:
        typer.echo(
            f"Unknown account credentials. Try adding the account with make-new-user")


@app.command()
def activate_user(name: str):
    """
        The GEE account to active
    """
    if name:
        select_user(name)
        typer.echo(f"Activated user account: {name}")
    else:
        typer.echo("No account selected. Try running --help")


@app.command()
def list_users():
    """
    See a list of all current users
    """
    current_users = return_users()
    typer.echo("Avalible accounts to select are:")
    for i in current_users:
        typer.echo(i)


if __name__ == "__main__":

    app()
