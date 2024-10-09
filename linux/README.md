# Linux setup (Ubuntu)

## Keep system packages up to date

```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove --purge -y
```

## Linux utility

### Configure Password-Based SSH Authentication

- Edit the **/etc/ssh/sshd_config** and add the following line:

  ```bash
  PasswordAuthentication yes
  ```

- Restart the SSH server for the new configuration to take effect:

  ```bash
  sudo /etc/init.d/ssh force-reload
  ```

### Execute sudo without Password

- Open terminal and type:

  ```bash
  sudo visudo
  ```

- At the bottom of the file, add the following line:

  ```bash
  <username> ALL=(ALL) NOPASSWD: ALL
  ```

## Interesting packages in Linux

```bash
### cool apps
sudo apt install neofetch hollywood cmatrix jp2a speedtest-cli thefuck -y
```

---

## [nvtop](https://github.com/Syllo/nvtop)

nvtop stands for Nvidia TOP, a (h)top like task manager for NVIDIA GPUs. It can handle multi-GPUs and print information about them in a htop familiar way.

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

## [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter#debian-or-ubuntu-based-distros)

ascii-image-converter is a command-line tool that converts images into ASCII art and prints them out onto the console.

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

````

## [ntfy](https://github.com/dschep/ntfy)

ntfy brings desktop notification from your shell.

[Linux Desktop Notifications](https://github.com/dschep/ntfy#linux-desktop-notifications---linux)

```sh
$ sudo apt install python-dbus # on ubuntu/debian
````

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

- Remove unused dependencies

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

- If some packages got autoremoved/removed, yet haven't purged, use **dpkg** to list it.

  ```bash
  dpkg -l | grep ^rc
  ```

  - **^rc** means remove but no purge.

- Combine with **grep+awk**.

  ```bash
  sudo apt-get purge `dpkg -l | grep ^rc | awk '{ print $2 }'`
  ```
