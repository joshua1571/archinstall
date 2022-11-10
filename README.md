# Personal Arch Install Configuration #

### Installation using archiso media ###

```
archinstall --config https://raw.githubusercontent.com/joshua1571/archinstall/master/config.json \
            --disk_layouts https://raw.githubusercontent.com/joshua1571/archinstall/master/disk-layout.json
```

Will still need to manually set the following:  
    - filesystem encryption for the btrfs root filesystem  
    - root password  
    - create user and set user password  

note: Github raw is cached for 5 minutes. Have to wait to test new changes
## TODO ##
- [x] Get working config files off of vm
  - [x] disk-layout.json
  - [x] config.json
  - [ ] packages needed to complete installation
    -  [x] git
    -  [x] flatpak
- [ ] install ansible python container
  - [ ] clone from separate repo
- [ ] custom commands use ansible playbook
  - [ ] Install flatpak packages
    - [x] org.mozilla.firefox
    - [x] io.neovim.nvim
    - [x] com.visualstudio.code
    - [x] com.discordapp.Discord 
    - [x] com.github.tchx84.Flatseal
    - [x] com.spotify.Client
    - [x] com.transmissionbt.Transmission
    - [x] io.mpv.Mpv 
    - [x] org.chromium.Chromium
    - [x] org.mozilla.Thunderbird
    - [x] org.libreoffice.LibreOffice
    - [x] io.github.shiftey.Desktop
  - [ ] pacman/aur packages
    - [ ] python3-pip
    - [x] tmux
    - [x] git
    - [x] neovim
    - [x] youtube-dl
    - [x] docker
    - [x] docker-compose
    - [x] github-cli
    - [x] rclone
    - [x] rsync
    - [x] wireguard-tools
    - [x] flatpak
  - [ ] Configuration files
    - [ ] git config
    - [ ] tmux config
    - [ ] neovim config
    - [ ] wireguard tunnel config

