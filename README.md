

## Install
1. Clone this repository and navigate to LLaVA folder
```bash
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
```

1. Install Package
```Shell
conda create -n llava python=3.11 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
pip install -e .
```

1. Install additional packages for training cases
```
pip install -e ".[train]"
pip install flash-attn==2.7.3 --no-build-isolation
```

### Upgrade to latest code base

```Shell
git pull
pip install -e .
```
## Restart  GNOME/KDE Session
```
sudo systemctl restart gdm
# gnome-shell --replace &
```
