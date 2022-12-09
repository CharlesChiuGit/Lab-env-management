# JupyterLab Setup

## Install JupyterLab in (base) env

1. Install JupyterLab & related packages in **Conda env:base**(user mode)

   ```bash
   conda install -c anaconda git -y
   conda install -c conda-forge nodejs jupyterlab nbresuse pandas -y
   conda install -c conda-forge jupyterlab-system-monitor jupyterlab-git plotly -y
   conda install -c conda-forge ipympl matplotlib ipywidgets jupyterlab_widgets -y
   ```

2. Install JupyterLab extensions

   ```bash
   jupyter labextension install jupyterlab-plotly
   ```

3. Build the extensions & check if all extensions are listed

   ```bash
   jupyter lab build
   jupyter labextension list
   ```

4. JupyterLab theme

   ```bash
   jupyter labextension install jupyterlab-tailwind-theme
   jupyter labextension install @konodyuk/theme-ayu-mirage
   ```

## Add other Conda env's kernel to JupyterLab

1. Activate the env

   ```bash
   conda activate my_env
   ```

2. Install ipykernel

   ```bash
   conda install ipykernel
   ```

3. Add kernel to JupyterLab

   ```bash
   python -m ipykernel install --user --name my_env --display-name "whatever"
   ```
