# `gee_auth`

**Usage**:

```console
$ gee_auth [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `activate-user`: The GEE account to active
* `authenticate-user`: authenticate an earth engine account.
* `list-users`: See a list of all current users
* `make-new-user`: Add a new user account to select from

## `gee_auth activate-user`

The GEE account to active

**Usage**:

```console
$ gee_auth activate-user [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `gee_auth authenticate-user`

authenticate an earth engine account. overrides any current credentials
    

**Usage**:

```console
$ gee_auth authenticate-user [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `gee_auth list-users`

See a list of all current users

**Usage**:

```console
$ gee_auth list-users [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `gee_auth make-new-user`

Add a new user account to select from

**Usage**:

```console
$ gee_auth make-new-user [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
