# Proxmox VE

- PVE: pve-manager/8.2.7/3e0176e6bb2ade3b (running kernel: 6.8.12-2-pve)
- CPU: i9-10980XE
- RAM: 128GB DDR4 3200MHz
- GPU: NVIDIA TITAN Xp \* 2 (with SLI)
- MOBO: ROG Rampage VI Extreme Encore

## Cleanup `/etc/apt` source lists

```bash
rm /etc/apt/sources.list.d/pve-enterprise.list
rm /etc/apt/sources.list.d/ceph.list
```

- Add `non-free`, `non-free-firmware` to debian source list

```bash
deb https://deb.debian.org/debian/ bookworm main contrib non-free non-free-firmware
deb https://deb.debian.org/debian/ bookworm-updates main contrib non-free non-free-firmware
deb http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
deb https://deb.debian.org/debian/ bookworm-backports main contrib non-free non-free-firmware
deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription
```

## Nvidia driver for PVE

- `apt install nvidia-driver-full`

### Some bugs after installing nvidia-driver

- `NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.`
  1. `apt install pve-headers-6.8.12-2-pve`: linux header is needed when using `dkms` later, don't forget to add `deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription` apt source.
  2. `dkms status`: list all registered dkms.
  - `dkms remove --force XXX/XXX` to remove unneeded one.
  - `dkms install --force XXX/XXX` to reinstall.
  3. `dkms install -m nvidia-current -v 535.183.01` to rebuild nvida-driver with correct kernel header files.

### References:

- [\[TUTORIAL\] Developer Workstation (Proxmox-VE 8) with cinnamon (LMDE6)](https://forum.proxmox.com/threads/developer-workstation-proxmox-ve-8-with-cinnamon-lmde6.133736/)
- [\[TUTORIAL\] Developer Workstation for Laptop](https://forum.proxmox.com/threads/developer-workstation-for-laptop.148660/)
- [dkms usage](https://askubuntu.com/questions/1457570/ubuntus-dkms-v3-0-6-breaks-drivers-with-enabled-secureboot)
- [install pve-headers](https://github.com/strongtz/i915-sriov-dkms/issues/85#issuecomment-1606528570)
- [Nvidia-smi 連不到 driver 的自救方法](https://medium.com/@yt.chen/nvidia-smi-%E9%80%A3%E4%B8%8D%E5%88%B0-driver-%E7%9A%84%E8%87%AA%E6%95%91%E6%96%B9%E6%B3%95-69cbed16171d)
