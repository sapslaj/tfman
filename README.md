# `tfman`

(currently PoC) of console documentation for Terraform

## Usage

```shell
tfman {type} {identifier}
```

Example:

```shell
$ tfman resource aws_instance
────────────────────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════════════════════╗
║                            Resource: aws_instance                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

Provides an EC2 instance resource. This allows instances to be created, updated,
and deleted. Instances also support provisioning.
```

Using shorthand for the type is allowed, e.g. `r` for `resource`, `d` for `data-source`.

### Supported lookups

- `a` - _N/A_
- `b` - _N/A_
- `c` - _N/A_
- `d` - data source
- `e` - expression
- `f` - function
- `g` - google
- `h` - _N/A_
- `i` - _N/A_
- `j` - _N/A_
- `k` - _N/A_
- `l` - _N/A_
- `m` - meta-arguments
- `n` - _N/A_
- `o` - _N/A_
- `p` - _N/A_
- `q` - _N/A_
- `r` - resource
- `s` - _N/A_
- `t` - _N/A_
- `u` - _N/A_
- `v` - _N/A_
- `w` - _N/A_
- `x` - _N/A_
- `y` - _N/A_
- `z` - _N/A_
