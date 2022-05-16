# JupyterLab Setup

## Install jupyterlab in (base) env

1. Install latest node.js(sudoer mode)

   ```bash
   curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. Install jupyterlab & related packages in **conda env:base**(user mode)

   ```bash
   pip install jupyterlab==3.0.14
   pip install nbresuse==0.3.4 jupyterlab-system-monitor jupyterlab-git JLDracula pandas
   conda install -c plotly plotly -y
   conda install -c conda-forge ipympl=0.7.0 -y
   conda install -c conda-forge matplotlib -y
   conda install -c conda-forge ipywidgets jupyterlab_widgets -y
   ```

3. Install jupyterlab extensions

   ```bash
   jupyter labextension install jupyterlab-plotly@4.14.3
   jupyter nbextension enable --py widgetsnbextension
   ```

4. Build the extensions & check it

   ```bash
   jupyter lab build
   jupyter labextension list
   ```

## Add other conda env's kernel to jupyterlab

1. Activate the env

   ```bash
   conda activate my_env
   ```

2. Install ipykernel

   ```bash
   conda install ipykernel
   ```

3. Add kernel to jupyterlab

   ```bash
   python -m ipykernel install --user --name my_env --display-name "whatever"
   ```
