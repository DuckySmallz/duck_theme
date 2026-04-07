
import os
import subprocess

USER = os.getenv("USER")
THEMES = {
    "blue": ["rgba(1c36fcee)", "rgba(1026ccee)", "Yaru-Blue-dark", "rgba(16, 38, 204, 0.45)", "rgba(28, 54, 252, 0.45)", "#f53c3c", "#1c36fc1e", "#1026cc73"],
    "cyan": ["rgba(00ffffee)", "rgba(00ababee)", "Yaru-Teal-dark", "rgba(12, 211, 211, 0.45)", "rgba(0, 255, 225, 0.45)", "#f53c3c", "#00ffff1e", "#00abab73"],
    "green": ["rgba(41c82dee)", "rgba(2eac1bee)", "Yaru-Green-dark", "rgba(46, 172, 27, 0.45)", "rgba(65, 200, 45, 0.45)", "#f53c3c", "#2eac1b1e", "#41c82d73"],
    "orange": ["rgba(ff4d00ee)", "rgba(e25c23ee)", "Yaru-Orange-dark", "rgba(226, 92, 35, 0.45)", "rgba(255, 77, 0, 0.45)", "#f53c3c", "#e25c231e", "#ff4d0073"],
    "pink": ["rgba(f364e0ee)", "rgba(ff1ba7ee)", "Yaru-Pink-dark", "rgba(206, 95, 191, 0.45)", "rgba(243, 100, 224, 0.45)", "#f53c3c", "#ff1ba71e", "#f364e073"],
    "purple": ["rgba(8c2debee)", "rgba(751bcfee)", "Yaru-Purple-dark", "rgba(117, 27, 207, 0.45)", "rgba(140, 45, 235, 0.45)", "#f53c3c", "#8c2deb1e", "#751bcf73"],
    "red": ["rgba(ff0000ee)", "rgba(991515ee)", "Yaru-Red-dark", "rgba(153, 21, 21, 0.45)", "rgba(255, 0, 0, 0.45)", "#ff00e1", "#ff00001e", "#99151573"],
    "yellow": ["rgba(f4b114ee)", "rgba(cfa92bee)", "Yaru-Yellow-dark", "rgba(207, 169, 43, 0.45)", "rgba(224, 177, 20, 0.45)", "#f53c3c", "#cfa92b1e", "#f4b11473"]
}
CONF_FILES = [
    f"/home/{USER}/.config/hypr/hyprland.conf",
    f"/home/{USER}/.config/rofi/config.rasi",
    f"/home/{USER}/.config/waybar/style.css"
    ]

color_selected = False
gpu_selected = False

print("Select a theme color \n 1.Blue \n 2.cyan \n 3.Green \n 4.Orange \n 5.Pink \n 6.Purple \n 7.Red \n 8.Yellow")
color = input("Select [1-8]: ")
while color_selected == False:
    if color == "1":
        color = "blue"
        color_selected = True
    elif color == "2":
        color = "cyan"
        color_selected = True
    elif color == "3":
        color = "green"
        color_selected = True
    elif color == "4":
        color = "orange"
        color_selected = True
    elif color == "5":
        color = "pink"
        color_selected = True
    elif color == "6":
        color = "purple"
        color_selected = True
    elif color == "7":
        color = "red"
        color_selected = True
    elif color == "8":
        color = "yellow"
        color_selected = True
    else:
        print("Invalid input")

print("Select Primary GPU: \n 1.NVIDIA \n 2.Other(AMD/INTEL/NONE)")
gpu = input("Select [1-2]: ")
while gpu_selected == False:
    if gpu == "1":
        gpu = "nvidia"
        gpu_selected = True
    elif gpu == "2":
        gpu = "amd"
        gpu_selected = True
    else:
        print("Invalid input")


if not os.path.isdir(f"/home/{USER}/.config/ducktheme"):
    os.system(f"mkdir /home/{USER}/.config")
    os.system(f"mkdir /home/{USER}/.config/ducktheme")
    os.system(f"cp -r src/* /home/{USER}/.config/")
    os.system(f"mkdir /home/{USER}/.icons")
    os.system(f"tar -xf depends/candy-icons.tar.xz -C /home/{USER}/.local/share/icons/")
    os.system(f"mkdir /home/{USER}/.system_images")
    os.system(f"mkdir /home/{USER}/.system_images/wallpaper")
    os.system(f"mkdir /home/{USER}/.system_images/lock_pic")
    os.system(f"cp img/wallpaper/minimal_{color}_wallpaper.jpg /home/{USER}/.system_images/wallpaper/wallpaper.jpg")
    os.system(f"cp img/lock_pic/lockpic.png /home/{USER}/.system_images/lock_pic/lockpic.png")
    if not os.path.isdir("/usr/share/themes/Yaru-Aqua"):
        os.system("mkdir depends/yaru")
        os.system(f"tar -xf depends/Complete-Yaru-Colors--v21.04.tar.xz -C depends/yaru/")
        os.system("depends/yaru/install.sh")
        os.system("rm -r depends/yaru")
    if gpu == "nvidia":
        os.system(f"rm /home/{USER}/.config/waybar/config.jsonc")
        os.system(f"mv /home/{USER}/.config/waybar/config_nvidia.jsonc /home/{USER}/.config/waybar/config.jsonc")
    else:
        os.system(f"rm /home/{USER}/.config/waybar/config_nvidia.jsonc")
        os.system(f"rm /home/{USER}/.config/waybar/nvidiagpu.sh")
        os.system(f"rm /home/{USER}/.config/waybar/nvidiagpu.py")

    for x in CONF_FILES:
        with open(x) as f:
            contents = f.read()
            modified = contents.replace("[PISSKEY]", THEMES[color][0])
            modified = modified.replace("[PISSKEY1]", THEMES[color][1])
            modified = modified.replace("[PISSKEY2]", THEMES[color][2])
            modified = modified.replace("[PISSKEY3]", THEMES[color][3])
            modified = modified.replace("[PISSKEY4]", THEMES[color][4])
            modified = modified.replace("[PISSKEY5]", THEMES[color][5])
            modified = modified.replace("[PISSKEY6]", THEMES[color][6])
            modified = modified.replace("[PISSKEY7]", THEMES[color][7])
        with open(x, "w") as f:
            f.write(modified)
        
    os.system("sudo pacman -Syy hyprland wayland gdm gtk3 wireplumber pipewire-pulse xdg-desktop-portal-hyprland hyprlock hyprpaper hypridle hyprshot nautilus kitty rofi waybar hyprpolkitagent fastfetch fish --noconfirm")
    os.system("sudo systemctl enable gdm")
    os.system(f"echo 'gtk-icon-theme-name = candy-icons' >> /home/{USER}/.config/gtk-4.0/settings.ini")
    os.system(f"echo 'gtk-icon-theme-name = candy-icons' >> /home/{USER}/.config/gtk-3.0/settings.ini")
    os.system(f"echo 'gtk-application-prefer-dark-theme = true' >> /home/{USER}/.config/gtk-4.0/settings.ini")
    os.system(f"echo 'gtk-application-prefer-dark-theme = true' >> /home/{USER}/.config/gtk-3.0/settings.ini")
    os.system(f"sudo usermod -s /bin/fish {USER}")
else:
    os.system(f"rm -r /home/{USER}/.config/hypr")
    os.system(f"rm -r /home/{USER}/.config/waybar")
    os.system(f"rm -r /home/{USER}/.config/rofi")
    os.system(f"rm -r /home/{USER}/.config/fastfetch")
    os.system(f"rm -r /home/{USER}/.config/kitty")
    os.system(f"rm -r /home/{USER}/.config/fish")
    os.system(f"rm -r /home/{USER}/.system_images/wallpaper/*")
    os.system(f"rm -r /home/{USER}/.system_images/lock_pic/*")
    os.system(f"cp img/wallpaper/minimal_{color}_wallpaper.jpg /home/{USER}/.system_images/wallpaper/wallpaper.jpg")
    os.system(f"cp img/lock_pic/lockpic.png /home/{USER}/.system_images/lock_pic/lockpic.png")
    os.system(f"cp -r src/* /home/{USER}/.config/")
    if gpu == "nvidia":
        os.system(f"rm /home/{USER}/.config/waybar/config.jsonc")
        os.system(f"mv /home/{USER}/.config/waybar/config_nvidia.jsonc /home/{USER}/.config/waybar/config.jsonc")
    else:
        os.system(f"rm /home/{USER}/.config/waybar/config_nvidia.jsonc")
        os.system(f"rm /home/{USER}/.config/waybar/nvidiagpu.sh")
        os.system(f"rm /home/{USER}/.config/waybar/nvidiagpu.py")
    for x in CONF_FILES:
        with open(x) as f:
            contents = f.read()
            modified = contents.replace("[PISSKEY]", THEMES[color][0])
            modified = modified.replace("[PISSKEY1]", THEMES[color][1])
            modified = modified.replace("[PISSKEY2]", THEMES[color][2])
            modified = modified.replace("[PISSKEY3]", THEMES[color][3])
            modified = modified.replace("[PISSKEY4]", THEMES[color][4])
            modified = modified.replace("[PISSKEY5]", THEMES[color][5])
            modified = modified.replace("[PISSKEY6]", THEMES[color][6])
            modified = modified.replace("[PISSKEY7]", THEMES[color][7])
        with open(x, "w") as f:
            f.write(modified)
        

input("INSTALLATION COMPLETE. Press any key to exit.")
