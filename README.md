# `ee_auth`

**Install**:

```console
$ pip install -m setup.py
```

**Usage**:

```console
$ ee_auth [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `activate-user`: The GEE account to active
- `authenticate-user`: authenticate an earth engine account.
- `check-activated-user`: Check to see which GEE account is activated
- `list-users`: See a list of all current users
- `make-new-user`: Add a new user account to select from

## `ee_auth activate-user`

The GEE account to active

**Usage**:

```console
$ ee_auth activate-user [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]

**Options**:

- `--help`: Show this message and exit.

## `ee_auth authenticate-user`

authenticate an earth engine account. overrides any current credentials

**Usage**:

```console
$ ee_auth authenticate-user [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `ee_auth check-activated-user`

Check to see which GEE account is activated

**Usage**:

```console
$ ee_auth check-activated-user [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `ee_auth list-users`

See a list of all current users

**Usage**:

```console
$ ee_auth list-users [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `ee_auth make-new-user`

Add a new user account to select from

**Usage**:

```console
$ ee_auth make-new-user [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.
