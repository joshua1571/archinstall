import archinstall, getpass

# Select a harddrive and a disk password
harddrive = archinstall.select_disk(archinstall.all_disks())
disk_password = getpass.getpass(prompt='Disk password (won\'t echo): ')
root_password = getpass.getpass(prompt='Root password (won\'t echo): ')
user_password = getpass.getpass(prompt='User password (won\'t echo): ')
__packages__ = [
	"zsh",
	"git",
    "wget",
	"tmux",
	"docker",
	"flatpak",
	"neovim"
]

# Unmount and close previous runs (Mainly only used for re-runs, but won't hurt.)
archinstall.sys_command(f'umount -R /mnt', suppress_errors=True)
archinstall.sys_command(f'cryptsetup close /dev/mapper/luksloop', suppress_errors=True)

#harddrive = archinstall.all_disks()['/dev/sda']
harddrive = archinstall.all_disks()['/dev/vda']

# We disable safety precautions in the library that protects the partitions
harddrive.keep_partitions = False

# First, we configure the basic filesystem layout
with archinstall.Filesystem(harddrive, archinstall.GPT) as fs:
    # We create a filesystem layout that will use the entire drive
    # (this is a helper function, you can partition manually as well)
    fs.use_entire_disk(root_filesystem_type='btrfs')

    boot = fs.find_partition('/boot')
    root = fs.find_partition('/')

    boot.format('vfat')

    # Set the flag for encrypted to allow for encryption and then encrypt
    root.encrypted = True
    root.encrypt(password=disk_password)

with archinstall.luks2(root, 'luksloop', disk_password) as unlocked_root:
    unlocked_root.format(root.filesystem)
    unlocked_root.mount('/mnt')

    boot.mount('/mnt/boot')

with archinstall.Installer('/mnt') as installation:
    if installation.minimal_installation():
        installation.set_hostname('arch')
        installation.add_bootloader()

        installation.add_additional_packages(__packages__)

        # Optionally, install a profile of choice.
        # In this case, we install a minimal profile that is empty
        installation.install_profile('minimal')

        installation.user_set_pw('root', 'root_password')
        installation.user_create('jrh', 'user_password')
        
