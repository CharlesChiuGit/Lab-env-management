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
sudo apt install nala # ubuntu22.04+
sudo apt install ssh vim tmux htop git make python3-setuptools python3-pip curl -y
sudo apt install ranger highlight bat -y
sudo apt install zoxide fzf -y

### snap install
sudo snap install cpufetch gdu-disk-usage-analyzer ascii-image-converter lolcat

### pip install
pip3 install gdown ntfy[emoji]

### pixilated image in terminal
sudo apt install termimage

### cool stuff
sudo apt install neofetch hollywood cmatrix jp2a speedtest-cli thefuck -y
```

---

## [Bashtop](https://github.com/aristocratos/bashtop)

Resource monitor that shows usage and stats for processor, memory, disks, network and processes.

```bash
sudo snap install bashtop
```

## [Ranger](https://github.com/ranger/ranger)

ranger is a console file manager with VI key bindings. It provides a minimalistic and nice curses interface with a view on the directory hierarchy. It ships with **rifle**, a file launcher that is good at automatically finding out which program to use for what file type.

```bash
sudo pip3 install ranger-fm
sudo apt install ranger
```

### Syntax highlight in ranger preview

```bash
sudo apt install highlight
```

Plugin: Install [ranger_devicons](https://github.com/alexanderjeurissen/ranger_devicons)

### Add icon to ranger

```bash
git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons
```

Set in `rc.conf`.

```bash
echo "default_linemode devicons" >> $HOME/.config/ranger/rc.conf
```

### Set image preview

```bash
pip install ueberzug
```

Set in `rc.conf`.

```bash
set preview_images true
set preview_images_method ueberzug
```

## [nvtop](https://github.com/Syllo/nvtop)

Nvtop stands for NVidia TOP, a (h)top like task monitor for NVIDIA GPUs. It can handle multiple GPUs and print information about them in a htop familiar way.

```bash
git clone https://github.com/Syllo/nvtop.git
sudo apt install cmake libncurses5-dev libncursesw5-dev git -y
mkdir -p nvtop/build && cd nvtop/build && cmake ..
make && sudo make install
```

## [gdown](https://pypi.org/project/gdown/)

Download a large file from Google Drive.

```bash
pip install gdown
```

See usage in [this doc](https://pypi.org/project/gdown/).

## [nala](https://gitlab.com/volian/nala)

A more prettier `apt`.

Install the Volian Scar repo.

```bash
echo "deb http://deb.volian.org/volian/ scar main" | sudo tee /etc/apt/sources.list.d/volian-archive-scar-unstable.list
wget -qO - https://deb.volian.org/volian/scar.key | sudo tee /etc/apt/trusted.gpg.d/volian-archive-scar-unstable.gpg > /dev/null
```

For Ubuntu 22.04 / Debian Sid and newer.

```bash
sudo apt update && sudo apt install nala
```

For older distributions like Ubuntu 21.04 / Debian Stable and older.

```bash
sudo apt update && sudo apt install nala-legacy
```

## [gdu-disk-usage-analyzer](https://snapcraft.io/install/gdu-disk-usage-analyzer/ubuntu)

Pretty fast disk usage analyzer written in Go.

## [bat](https://github.com/sharkdp/bat)

A syntax highlighted version of `cat`.

## [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter#debian-or-ubuntu-based-distros)

ascii-image-converter is a command-line tool that converts images into ascii art and prints them out onto the console.

```bash
ascii-image-converter XXX.png --color
```

## [jp2a](https://github.com/cslarsen/jp2a)

jp2a is a simple JPEG to ASCII converter.

## [speedtest-cli](https://github.com/sivel/speedtest-cli)

Command line interface for testing internet bandwidth using speedtest.net

```bash
speedtest
```

## [lolcat](https://github.com/busyloop/lolcat)

Add rainbow to your command line.

## [lsd](https://github.com/Peltoche/lsd)

This project is a rewrite of GNU ls with lot of added features like colors, icons, tree-view, more formatting options etc. The project is heavily inspired by the super [colorls](https://github.com/athityakumar/colorls) project.

```bash
sudo dpkg -i lsd_0.21.0_amd64.deb
```

get .deb file from [release page](https://github.com/Peltoche/lsd/releases)

## [batcat](https://github.com/sharkdp/bat)

```bash
batcat ~/.bashrc
```

## [zoxide](https://github.com/ajeetdsouza/zoxide)

For Ubuntu 21.04+:

```bash
sudo apt install zoxide
```

For Ubuntu 21.04-:

```bash
curl -sS https://webinstall.dev/zoxide | bash
```

Add to bashrc

```bash
# zoxide
eval "$(zoxide init bash)"
```

## [thefuck](https://github.com/nvbn/thefuck)

Fix cli command typo with `fuck`.

```bash
sudo apt update
sudo apt install python3-dev python3-pip python3-setuptools
sudo apt install thefuck
```

## [termimage](https://github.com/nabijaczleweli/termimage)

#### From Debian repository

The following line in `/etc/apt/sources.list`:

```apt
deb https://debian.nabijaczleweli.xyz stable main
```

With [my PGP key](https://debian.nabijaczleweli.xyz/nabijaczleweli.gpg.key) (the two URLs are interchangeable):

```sh
wget -O- https://debian.nabijaczleweli.xyz/nabijaczleweli.gpg.key | sudo apt-key add
# or
sudo wget -O/etc/apt/trusted.gpg.d/nabijaczleweli.asc https://nabijaczleweli.xyz/pgp.txt
```

Then the usual

```sh
sudo apt update
sudo apt install termimage
```

will work on x86_64, i686, and x32.

See the [repository README](https://debian.nabijaczleweli.xyz/README) for more information.

## [FiraCode (nerdfonts)](https://www.nerdfonts.com/font-downloads)

```sh
mkdir ~/.local/share/fonts && cd ~/.local/share/fonts
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/FiraCode.zip
unzip FiraCode.zip
```

## [ntfy](https://github.com/dschep/ntfy)

ntfy brings desktop notification from your shell.

[Linux Desktop Notifications](https://github.com/dschep/ntfy#linux-desktop-notifications---linux)

```sh
$ sudo apt install python-dbus # on ubuntu/debian
```

Quick start

```sh
$ sudo pip install ntfy
$ ntfy send test
# send a notification when the command `sleep 10` finishes
# this sends the message '"sleep 10" succeeded in 0:10 minutes'
$ ntfy done sleep 10
$ ntfy -b pushover -o user_key t0k3n send 'Pushover test!'
$ ntfy -t 'ntfy' send "Here's a custom notification title!"
$ echo -e 'backends: ["pushover"]\npushover: {"user_key": "t0k3n"}' > ~/.ntfy.yml
$ ntfy send "Pushover via config file!"
$ ntfy done --pid 6379  # pid extra
$ ntfy send ":tada: ntfy supports emoji! :100:"  # emoji extra
# Enable shell integration
$ echo 'eval "$(ntfy shell-integration)"' >> ~/.bashrc
```

---

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

- Combine with **grep+awk**.

  ```bash
  sudo apt-get purge `dpkg -l | grep ^rc | awk '{ print $2 }'`
  ```
