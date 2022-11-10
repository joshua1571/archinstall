# Personal Arch Install Configuration

### Installation using archiso media

archinstall --confifg https://raw.githubusercontent.com/joshua1571/archinstall/master/config.json \
            --disk_layouts https://raw.githubusercontent.com/joshua1571/archinstall/master/disk-layout.json

note: Github raw is cached for 5 minutes. Have to wait to test new changes
## TODO
- [x] Get working config files off of vm
    - [x] disk-layout.json
    - [x] config.json
    - [ ] creds.json
- [ ] packages needed to complete installation
   -  [x] git
   -  [z] ansible
   -  [x] flatpak
- [ ] custom commands use ansible playbook
    - [ ] Install flatpak packages
        - [ ] org.mozilla.firefox
        - [ ] io.neovim.nvim
        - [ ] com.visualstudio.code
        - [ ] com.discordapp.Discord 
        - [ ] com.github.tchx84.Flatseal
        - [ ] com.spotify.Client
        - [ ] com.transmissionbt.Transmission
        - [ ] io.mpv.Mpv 
        - [ ] org.chromium.Chromium
        - [ ] org.mozilla.Thunderbird
        - [ ] org.libreoffice.LibreOffice
        - [ ] io.github.shiftey.Desktop
    - [ ] pacman packages
        - [ ] python3-pip
        - [ ] youtube-dl
        - [ ] docker
        - [ ] docker-compose
        - [ ] gh
        - [ ] rclone
        - [ ] rsync
        - [ ] wireguard-tools
    - [ ] Configuration files
        - [ ] git config
        - [ ] tmux config
        - [ ] neovim config
        - [ ] wireguard tunnel config

