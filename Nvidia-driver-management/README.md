# Nvida Driver Management (CUDA Toolkit 12.3 Update 1 and higher)

## Clean up old CUDA & Nvidia driver (prefered, if their is an old one installed)

- Check if there's any hardware failure by listing all gpus, i.e. gpu lost

  ```sh
  lspci | grep -i nvidia
  ```

- Completely remove CUDA & nvidia driver:

  ```sh
  sudo apt --purge remove "*cublas*" "cuda*" "nsight*" "*cudnn*" "libnvidia*" -y
  sudo apt remove --purge '^nvidia-.*' -y
  # (Optional, Prefer) Remove all CUDA to avoid possible confilication with new driver
  sudo rm -rf /usr/local/cuda*
  sudo apt --purge autoremove -y
  sudo apt autoclean
  ```

- Check if there is anything related packages leaft and remove them:

  ```sh
  dpkg -l | grep -i nvidia
  dpkg -l | grep nvidia-driver
  sudo apt --purge remove {some-pkg}
  ```

## Install CUDA Toolkit, nvidia driver and cuDNN

- Check [CUDA Toolkit Archive List](https://developer.nvidia.com/cuda-toolkit-archive) to find prefered version and follow the instructions.
  - If you want versions lower 12.3, then check [this doc](./deprecated.md).
- Check [cuDNN Archive List](https://developer.nvidia.com/cudnn-archive) to find prefered version and follow the instuctions.
- An example if you use `Ubuntu 24.04(x86_64)` and `deb(network)` for [CUDA 12.5 Update 1](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_network)

  - Base Installer:

  ```sh
  wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
  sudo dpkg -i cuda-keyring_1.1-1_all.deb
  sudo apt update
  sudo apt install cuda-toolkit-12-5 -y
  ```

  > [!IMPORTANT]  
  > Check [this offical blog](https://developer.nvidia.com/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/#supported_gpus) to check what flavor of driver does your gpu need.

  - Driver Installer, open kernel module flavor:

  ```sh
  sudo apt install nvidia-driver-555-open -y
  sudo apt install cuda-drivers-555 -y
  ```

  - Driver Installer, legacy kernel module flavor:

  ```sh
  sudo apt install cuda-drivers -y
  ```

- Set CUDA `PATH` and `LD_LIBRARY_PATH` to your `[ba/z]shrc`:

  ```sh
  # set cuda path if nvidia-smi works
  if command -v nvidia-smi &>/dev/null; then
  	add_path "/usr/local/cuda/bin"
        [[ ":$path:" == *":/usr/local/cuda/bin:"* ]] ||
            export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
  	[[ ":$LD_LIBRARY_PATH:" == *":/usr/local/cuda/lib64:"* ]] ||
            export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
  fi
  ```

- Reload the system path:
  ```sh
  source ~/.[ba/z]shrc
  ```
- Reboot and check gpu info with `nvidia-smi`.(prefered)

  - If you want to reload gpu mods while keeping machine alive, use following commands.

    > [!CAUTION]
    > However this may sriously slow down the gpu process until you reboot your machine.

  ```sh
  # Change to CLI only mode
  sudo systemctl isolate multi-user.target
  # Kill processes using nvidia devices if any
  sudo lsof /dev/nvidia*
  sudo lsof -t /dev/nvidia* | xargs sudo kill -9
  # Remove nvidia module
  # "rmmod" shows the dependencies, remove them recursively and manually with "sudo rmmod sth"
  sudo rmmod nvidia
  # Reload nvidia module
  sudo modprobe nvidia
  # Set to default target
  sudo systemctl default
  ```

  - If `nvidia-modprobe` is broken or missing, fix it via following commands:

  ```sh
  # Install nvidia-modprobe
  sudo apt install nvidia-modprobe
  # Check nvidia-modprobe version
  nvidia-modprobe -v
  ```

## Post-installation Actions

- Check if `Persistence Daemon` is active:

  ```sh
  sudo systemctl status nvidia-persistenced.service
  ```

  - If it's active, it should shows:

  ```
  ● nvidia-persistenced.service - NVIDIA Persistence Daemon
     Loaded: loaded (/usr/lib/systemd/system/nvidia-persistenced.service; static)
     Active: active (running) since Sun 2024-07-21 07:31:57 UTC; 5h 53min ago
   Main PID: 1331 (nvidia-persiste)
      Tasks: 1 (limit: 38220)
     Memory: 368.0K (peak: 844.0K)
        CPU: 1ms
     CGroup: /system.slice/nvidia-persistenced.service
             └─1331 /usr/bin/nvidia-persistenced --user nvidia-persistenced --no-persistence-mode --verbose

  Jul 21 07:31:57 {hostname} systemd[1]: Starting nvidia-persistenced.service - NVIDIA Persistence Daemon...
  Jul 21 07:31:57 {hostname} nvidia-persistenced[1331]: Verbose syslog connection opened
  Jul 21 07:31:57 {hostname} nvidia-persistenced[1331]: Now running with user ID 116 and group ID 120
  Jul 21 07:31:57 {hostname} nvidia-persistenced[1331]: Started (1331)
  Jul 21 07:31:57 {hostname} nvidia-persistenced[1331]: device 0000:01:00.0 - registered
  Jul 21 07:31:57 {hostname} nvidia-persistenced[1331]: device 0000:02:00.0 - registered
  Jul 21 07:31:57 {hostname} nvidia-persistenced[1331]: Local RPC services initialized
  Jul 21 07:31:57 {hostname} systemd[1]: Started nvidia-persistenced.service - NVIDIA Persistence Daemon.
  ```

  - If it's not active, enable the daemon via:

  ```sh
  sudo systemctl enable nvidia-persistenced.service
  sudo systemctl start nvidia-persistenced.service
  ```

  > [!NOTE] > `Persistence Daemon` is prefered than `Persistence Mode` after nvida driver R319.

- Verify the installation:

  - For CUDA Toolkit, follow the [steps](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#install-writable-samples) of [cuda-samples](https://github.com/NVIDIA/cuda-samples).

  - > [!NOTE]
    > You might need to install third-party libraries for compiling cuda-samples, check [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#install-third-party-libraries) to install the libs.

  - For cuDNN, follow the [steps in the doc](https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html#verifying-the-install-on-linux).

## Tips, Tricks and Tools

- [CUDA FAQ](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#frequently-asked-questions)
- [Useful nvidia-smi Queries](https://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries)
- [R367.38 nvidia-smi.txt](https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf)
- [nvtop - GPU & Accelerator process monitoring for AMD, Apple, Huawei, Intel, NVIDIA and Qualcomm](https://github.com/Syllo/nvtop)
- [nvitop - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.](https://github.com/XuehaiPan/nvitop)
- [gpustat - A simple command-line utility for querying and monitoring GPU status](https://github.com/wookayin/gpustat)
- [nvidia-htop - A tool for enriching the output of nvidia-smi.](https://github.com/peci1/nvidia-htop)

### References

- CUDA Toolkit:
  - [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive)
  - [CUDA Toolkit 12.5 Update 1 Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_network)
  - [CUDA Toolkit Documentation 12.5 Update 1](https://docs.nvidia.com/cuda/)
  - [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- cuDNN
  - [cuDNN Archive](https://developer.nvidia.com/cudnn-archive)
  - [cuDNN 9.2.1 Downloads](https://developer.nvidia.com/cudnn-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_network)
  - [NVIDIA cuDNN](https://docs.nvidia.com/deeplearning/cudnn/latest/)
  - [Installing cuDNN on Linux](https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html)
- GitHub repo
  - [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples)
  - [NVIDIA/nvidia-persistenced](https://github.com/NVIDIA/nvidia-persistenced)
- Docs and Blogs
  - [GPU Management and Deployment](https://docs.nvidia.com/deploy/index.html)
    - [Driver Persistence](https://docs.nvidia.com/deploy/driver-persistence/index.html)
  - [NVIDIA Transitions Fully Towards Open-Source GPU Kernel Modules](https://developer.nvidia.com/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/#supported_gpus)
