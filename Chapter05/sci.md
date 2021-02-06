sudo apt update
apt-cache show python3-scipy
sudo apt install -y python3-scipy

pip install cython

sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
sudo /sbin/mkswap /var/swap.1
sudo chmod 600 /var/swap.1
sudo /sbin/swapon /var/swap.1
which will give you 1GB of swap space.

Then one can finally build and install with

python3 setup.py build

python3 setup.py install --user
(you can drop the --user flag if you want to install it system-wide, but you'll need root privilege).

Finally, one remove the extra swap and restore the default:

sudo swapoff /var/swap.1
sudo rm /var/swap.1