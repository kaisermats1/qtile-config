# this script install all of the necessary apps for me

# update all
pacman -Syyu

# apps

## timeshift
pacman -Syyu timeshift timeshift-autosnap btrfs-assistant

## editors
pacman -Syyu emacs visual-studio-code-bin obsidian copyq

# fonts
yay -S ttf-meslo-nerd-font-powerlevel10k ttf-jetbrains-mono