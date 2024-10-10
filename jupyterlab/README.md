# JupyterLab v4

ENVs:

- Python : 3.12.7
- IPython : 8.28.0
- ipykernel : 6.29.5
- ipywidgets : 8.1.5
- jupyter_client : 8.6.3
- jupyter_core : 5.7.2
- jupyter_server : 2.14.2
- jupyterlab : 4.2.5

## JupyterLab Setup

### Setup JupyterLab conda venv

```bash
conda env create --file ./env.yml
```

> [!IMPORTANT]
> I deliberately remove `pip` in the venv to avoid multiple pkg manager to manage the same venv.
> Read this [section](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment) before you use `pip` in `conda` venv!

### Build the extensions & check if it's heathly or not

```bash
jupyter lab build
jupyter labextension list --verbose
```

> [!WARNING]
> Check if those unhealthly extensions are working porperly, or you might need to find alternative one.

## ipykernel management

https://jupyter-client.readthedocs.io/en/latest/

### Install ipykernel to other conda venv

```bash
conda activate another_env
conda install ipykernel
python -m ipykernel install --user --name another_env --display-name "whatever"
```

### List all ipykernels

```bash
jupyter kernelspec list
```

### Remove unwanted ipykernel

```bash
jupyter kernelspec uninstall unwanted-kernel
```

## [Updating an environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment)

```bash
conda env update --file env.yml --prune
```

## Installed jupyterlab extensions in `env.yml`

[Extension Compatibility with JupyterLab 4.0 - jupyterlab/jupyterlab#14590](https://github.com/jupyterlab/jupyterlab/issues/14590)

### File Manager

- https://github.com/jupyterlab-contrib/jupyterlab-unfold
- https://github.com/jupyterlab-contrib/jupyter-archive
- https://github.com/jupyterlab-contrib/jupyterlab-favorites

### Monitoring Tools

- https://github.com/rapidsai/jupyterlab-nvdashboard
  - conda install -c rapidsai-nightly -c conda-forge jupyterlab-nvdashboard
- https://github.com/jupyter-server/jupyter-resource-usage

### IDE-utils

- https://github.com/jupyter-lsp/jupyterlab-lsp
  - conda install jupyterlab-lsp jupyter-lsp jedi-language-server
- https://github.com/jupyterlab-contrib/jupyterlab-variableInspector
  - conda install lckr_jupyterlab_variableinspector
- https://github.com/jupyterlab-contrib/jupyterlab_code_formatter
  - conda install jupyterlab_code_formatter black isort
- https://github.com/jupyterlab-contrib/search-replace
  - conda install jupyterlab-search-replace ripgrep
- https://github.com/jupyterlab-contrib/jupyterlab-vim
- https://github.com/jupyterlab-contrib/spellchecker
- https://github.com/jupyter/nbdime
- https://github.com/timkpaine/jupyterlab_autoversion
- https://github.com/deshaw/jupyterlab-execute-time

### Layouts

- https://github.com/trungleduc/jupyter_app_launcher
  - https://jupyter-app-launcher.readthedocs.io/en/latest/usage.html
- https://github.com/jupyter-widgets/jupyterlab-sidecar

### Extra filetype supports

- https://github.com/silx-kit/jupyterlab-h5web
- https://github.com/jupyterlab/jupyterlab-latex
- https://github.com/mwouts/jupytext

### Themes

- https://github.com/catppuccin/jupyterlab
