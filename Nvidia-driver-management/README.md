# Nvidia Driver Management

## Reinstall CUDA & Nvidia driver

1. Completely remove cuda & nvidia driver
   ```bash
   sudo apt-get --purge remove "*cublas*" "cuda*" "nsight*" -y
   sudo apt-get remove --purge '^nvidia-.*' -y
   sudo rm -rf /usr/local/cuda*
   sudo apt-get --purge autoremove -y
   ```
2. Check it there is anything related leaft
   ```bash
   dpkg -l | grep -i nvidia
   dpkg -l | grep nvidia-driver
   ```
3. Install nvidia driver
   ```bash
   - sudo add-apt-repository ppa:graphics-drivers/ppa
   - sudo apt update
   - sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev -y
   - sudo apt install ubuntu-drivers-common
   - sudo apt install nvidia-driver-
   ```
4. Restart and check nvidia driver with **nvidia-smi**. (prefer)
   - If u want reload gpu mods while keeping server alive, use following commands. **However this may sriously slow down the gpu process, restart will fix it.**
   ```bash
   # change to CLI only mode
   sudo systemctl isolate multi-user.target
   # kill processes using nvidia devices if any
   sudo lsof /dev/nvidia*
   sudo lsof -t /dev/nvidia* | xargs sudo kill -9
   # remove nvidia module
   # rmmod shows the dependencies, remove them recursively and manually
   sudo rmmod nvidia
   # reload nvidia module
   sudo modprobe nvidia
   # set to default target
   sudo systemctl default
   ```
   - If nvidia-modprobe is broken or missing, use following commands.
   ```bash
   #install nvidia-modprobe
   sudo apt install nvidia-modprobe
   #check nvidia-modprobe version
   nvidia-modprobe -v
   ```
5. Install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) & [cudnn]()

   - CUDA: It is always prefer to walk through all the [Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) first.

   ```bash
   export OS='ubuntu2004' or 'ubuntu1804'
   wget https://developer.download.nvidia.com/compute/cuda/repos/${OS}/x86_64/cuda-${OS}.pin
   sudo mv cuda-${OS}.pin /etc/apt/preferences.d/cuda-repository-pin-600
   sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/${OS}/x86_64/7fa2af80.pub
   sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/${OS}/x86_64/ /"
   sudo apt-get update
   sudo apt-get -y install cuda
   unset OS
   ```

   - CUDNN: It is always prefer to walk through all the [Installation Guide](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#cudnn-package-manager-installation-overview) first.

   ```bash
   export cudnn_version='8.3.2.*'
   export cuda_version='cuda10.2' or 'cuda11.5'
   sudo apt install zlib1g
   sudo apt-get install libcudnn8=${cudnn_version}-1+${cuda_version}
   sudo apt-get install libcudnn8-dev=${cudnn_version}-1+${cuda_version}
   unset cudnn_version
   unset cuda_version
   ```

6. (Optional) If gpus keep burning out when usage is too high, try the following command to limite gpu power.
   ```bash
   # Enable persistence mode
   sudo nvidia-smi -pm 1
   # Set power cap (maximum wattage the GPU will use)
   sudo nvidia-smi -pl 170
   ```
   - For some useful nvidia-smi options, see [Useful nvidia-smi Queries](https://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries)
   - For full details, please refer to the [nvidia-smi documentation](https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf).
