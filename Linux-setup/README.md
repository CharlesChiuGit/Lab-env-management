# Linux setup (Ubuntu)

## Keep things up to date

```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove --purge -y
```

## The must-have package in linux

```bash
sudo apt update
sudo apt install ssh vim tmux htop git make python3-setuptools python3-pip curl -y
```

#

## [Bashtop](https://github.com/aristocratos/bashtop):

### Resource monitor that shows usage and stats for processor, memory, disks, network and processes.

```bash
sudo snap install bashtop
```

## [Ranger](https://github.com/ranger/ranger):

### ranger is a console file manager with VI key bindings. It provides a minimalistic and nice curses interface with a view on the directory hierarchy. It ships with **rifle**, a file launcher that is good at automatically finding out which program to use for what file type.

```bash
git clone https://github.com/ranger/ranger.git
cd ranger && sudo make install
```

## [nvtop](https://github.com/Syllo/nvtop):

### Nvtop stands for NVidia TOP, a (h)top like task monitor for NVIDIA GPUs. It can handle multiple GPUs and print information about them in a htop familiar way.

```bash
git clone https://github.com/Syllo/nvtop.git
sudo apt install cmake libncurses5-dev libncursesw5-dev git -y
mkdir -p nvtop/build && cd nvtop/build && cmake ..
make && sudo make install
```

## [gdown](https://pypi.org/project/gdown/):

Download a large file from Google Drive.

```bash
pip install gdown
```

See usage in [this doc](https://pypi.org/project/gdown/).

#

## Frequently-used apt commands

- Remove package:
  ```bash
  # Keep configuration file
  sudo apt-get remove vsftpd
  ```
- Remove package & configuration file:
  ```bash
  # Remove configuration file
  sudo apt-get purge vsftpd
  ```
  or
  ```bash
  sudo apt-get remove --purge texlive-full
  ```
- Remove un-used dependencies
  ```bash
  sudo apt autoremove
  ```
- Remove all package files(installation files/ **\*.deb**)
  ```bash
  sudo apt clean
  ```
- Remove package files which is not installed in PC
  ```bash
  sudo apt autoclean
  ```
- If some package was autoremoved/removed, yet haven't purged, use **dpkg** to list it.
  ```bash
  dpkg -l | grep ^rc
  ```
  - **^rc** means only remove but no purge.
- Combind with **grep+awk**.
  ```bash
  sudo apt-get purge `dpkg -l | grep ^rc | awk '{ print $2 }'`
  ```
