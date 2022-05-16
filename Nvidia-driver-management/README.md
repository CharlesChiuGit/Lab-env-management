# Nvidia Driver Management

## Reinstall CUDA & Nvidia driver

0. List all PCI device to check if there is any hardware failure, i.e. gpu lost.

   ```bash
   lspci | grep -i nvidia
   ```

1. Completely remove cuda & nvidia driver

   ```bash
   sudo apt --purge remove "*cublas*" "cuda*" "nsight*" -y
   sudo apt remove --purge '^nvidia-.*' -y
   # (Optional, Prefer) Remove all CUDA to avoid possible confilication with new driver
   sudo rm -rf /usr/local/cuda*
   sudo apt --purge autoremove -y
   ```

2. Check if there is anything related packages leaft, then manually remove them via "sudo apt --purge remove sth".

   ```bash
   dpkg -l | grep -i nvidia
   dpkg -l | grep nvidia-driver
   ```

3. Install nvidia driver

   ```bash
   # Add PPA's graphics drivers repository to your Ubuntu-based Distos
   sudo add-apt-repository ppa:graphics-drivers/ppa
   # Update all package
   sudo apt update
   # (Optional) Some packages u might need
   sudo apt install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev -y
   # Install ubuntu-drivers-common package
   sudo apt install ubuntu-drivers-common
   # Install the nvidia driver u need. Press "tab" to see all available options, then finish the command
   sudo apt install nvidia-driver-
   ```

   - PPA stands for [Personal Package Archives](https://launchpad.net/ubuntu/+ppas), builded & provided by community.
     - [Are PPAs safe to add to my system and what are some "red flags" to watch out for?](https://askubuntu.com/questions/35629/are-ppas-safe-to-add-to-my-system-and-what-are-some-red-flags-to-watch-out-for)

4. Restart and check nvidia driver with **nvidia-smi**. (prefer)

   - If u want to reload gpu mods while keeping server alive, use following commands. **However this may sriously slow down the gpu process, restart will fix it.**

     ```bash
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

   - If nvidia-modprobe is broken or missing, use following commands.

     ```bash
     # Install nvidia-modprobe
     sudo apt install nvidia-modprobe
     # Check nvidia-modprobe version
     nvidia-modprobe -v
     ```

5. Install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) & [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive) via network.

   - CUDA: It is always prefer to walk through all the [Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) first.

     ```bash
     # Set the "OS" alias based on your Ubuntu version
     export OS='ubuntu2004' or 'ubuntu1804'
     wget https://developer.download.nvidia.com/compute/cuda/repos/${OS}/x86_64/cuda-${OS}.pin
     sudo mv cuda-${OS}.pin /etc/apt/preferences.d/cuda-repository-pin-600
     sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/${OS}/x86_64/7fa2af80.pub
     sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/${OS}/x86_64/ /"
     sudo apt-get update
     # Install the latest CUDA
     sudo apt-get -y install cuda
     # Unset the "OS" alias
     unset OS
     ```

   - cuDNN: It is always prefer to walk through all the [Installation Guide](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#cudnn-package-manager-installation-overview) first.

     ```bash
     # Set the "cudnn_version" alias based on the version, u can find the latest version in Installation Guide
     export cudnn_version='8.3.2.*'
     # Set the "cuda_version" alias based on corresponding CUDA version u installed previously
     export cuda_version='cuda10.2' or 'cuda11.5'
     sudo apt install zlib1g
     sudo apt-get install libcudnn8=${cudnn_version}-1+${cuda_version}
     sudo apt-get install libcudnn8-dev=${cudnn_version}-1+${cuda_version}
     # Unset the "cudnn_version" alias
     unset cudnn_version
     # Unset the "cuda_version" alias
     unset cuda_version
     ```

6. Set the CUDA's path to system PATH.

   - Open **/home/{user}/.bashrc** with your text editer.

     ```bash
     vim ~/.bashrc
     ```

   - Put these line at the bottom of the bashrc.

     ```bash
     # Your cuda-version should look like this 'cuda-11.5'
     export PATH=/usr/local/{cuda-version}/bin${PATH:+:${PATH}}
     export LD_LIBRARY_PATH=/usr/local/{cuda-version}/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
     ```

   - Reload the system path.

     ```bash
     source ~/.bashrc
     ```

7. (Optional) If gpus keep burning out when usage is too high, try the following command to limite gpu power.

   - **Important!!** Following command will be restored to default after restart.

     ```bash
     # Check persistence mode status
     nvidia-smi -q | grep 'Persistence Mode'
     # Enable it if it's off. It is enabled after nvidia-driver-319 by default
     sudo nvidia-smi -pm 1

     # Determine the current, default and maximum power limit
     nvidia-smi -q | grep 'Power Limit'
     # Set power cap (maximum wattage the GPU will use)
     sudo nvidia-smi -pl 170
     ```

   - Auto apply the setting after reboot.

     - Watch this guide: [Running a sudo command automatically on startup](https://unix.stackexchange.com/questions/645914/running-a-sudo-command-automatically-on-startup).

   - For more about persistence mode, see [Persistence Daemon](https://docs.nvidia.com/deploy/driver-persistence/index.html#persistence-daemon)
   - For some useful nvidia-smi options, see [Useful nvidia-smi Queries](https://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries)
   - For full details, please refer to the [nvidia-smi documentation](https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf).
