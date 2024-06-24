# Conda Environment Setup

## Create from scratch

1. Go to [Anaconda](https://www.anaconda.com/), get the latest bash file link.
2. Download the bash file

   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
   ```

3. Run the bash file.
4. (Optional) Set conda auto activate to false.

   ```bash
   conda config --set auto_activate_base false
   ```

5. Create new conda env

   ```bash
   conda create -n ENV_NAME python=3.10
   ```

   - Noted: Before installing any new packages, do once **conda deactivate** & **conda activate**. This will ensure u r in the right conda env.
   - For details see [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

6. Install new packages via **conda install sth.** or **pip install sth.**

   - Edit **.condarc** file to install certain package everytime u create new env, i.e.

     ```txt
     create_default_packages:
       - pip
       - ipython
       - scipy=0.15.0
     ```

     For details see [Using the .condarc conda configuration file](https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#config-add-default-pkgs).

## Creating an environment from an environment.yml file

1. Create the environment from the **environment.yml** file:

   ```bash
   conda env create -f environment.yml
   ```

   - For details see [Creating an environment file manually](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually)

2. Activate the new environment:

   ```bash
   conda activate myenv
   ```

3. Verify that the new environment was installed correctly:

   ```bash
   conda env list
   ```

   or

   ```bash
   conda info --envs
   ```

4. Export your active environment to a new file:

   ```bash
   conda env export > environment.yml
   ```

5. Updating environment.yml

   ```bash
   conda env update --prefix ./env --file environment.yml  --prune
   ```

## Removing an environment

```bash
conda env remove --name myenv
```

## Cloning an environment

```bash
conda create --name myclone --clone myenv
```

## Setting environment variables

- Set environment variables just for this conda env

1. Locate the directory for the conda environment:

   ```bash
   echo $CONDA_PREFIX
   ```

2. Create these subdirectories and files:

   ```bash
   cd $CONDA_PREFIX
   mkdir -p ./etc/conda/activate.d
   mkdir -p ./etc/conda/deactivate.d
   touch ./etc/conda/activate.d/env_vars.sh
   touch ./etc/conda/deactivate.d/env_vars.sh
   ```

3. Edit **./etc/conda/activate.d/env_vars.sh** as follows:

   ```bash
   #!/bin/sh

   export MY_KEY='secret-key-value'
   export MY_FILE=/path/to/my/file/
   ```

4. Edit **./etc/conda/deactivate.d/env_vars.sh** as follows:

   ```bash
   #!/bin/sh

   unset MY_KEY
   unset MY_FILE
   ```

---

## Often used python package and format

```bash
conda install scipy Pillow numpy plotly pandas nbformat -y
conda install -c conda-forge ipywidgets -y

pip install pytorch-lightning importlib
pip install hydra-core wandb --upgrade
python -m pip install ninja
```

---

## Useful commands
https://github.com/matbinder/secure-multi-user-conda
