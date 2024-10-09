# Conda/Mamba Setup

## Install Micromamba:

- https://github.com/mamba-org/mamba
- https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html

### Linux and macOS

```bash
# Linux Intel (x86_64):
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
# Linux ARM64:
curl -Ls https://micro.mamba.pm/api/micromamba/linux-aarch64/latest | tar -xvj bin/micromamba
# Linux Power:
curl -Ls https://micro.mamba.pm/api/micromamba/linux-ppc64le/latest | tar -xvj bin/micromamba
# macOS Intel (x86_64):
curl -Ls https://micro.mamba.pm/api/micromamba/osx-64/latest | tar -xvj bin/micromamba
# macOS Silicon/M1 (ARM64):
curl -Ls https://micro.mamba.pm/api/micromamba/osx-arm64/latest | tar -xvj bin/micromamba
```

### Shell completion (bash, zsh)

```bash
micromamba shell completion
```

### Update micromamba

```bash
micromamba self-update
```

---

### Personal condarc

`$XDG_CONFIG_HOME/conda/condarc`:

```yaml
channels:
  - conda-forge
  - nodefaults
channel_priority: strict
changeps1: false
# vim: set ft=yaml :
```

---

## Resources

- Search anaconda pkgs: https://anaconda.org/search?q=
- Search conda-forge pkgs: https://conda-forge.org/search/
- [Conda Common Tasks](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/index.html)
  - Managing Conda
  - Managing environments, including `updating an env`, `setting env vars`, `saving env vars`
- [Conda Configuration](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/index.html)
  - Using the `.condarc` conda configuration file
  - Settings
  - Pip interoperability (experimental)
- https://github.com/matbinder/secure-multi-user-conda
