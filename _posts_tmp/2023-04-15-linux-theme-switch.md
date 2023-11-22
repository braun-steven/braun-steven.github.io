---
layout: post
title: "Automate Linux Time-based Theme Switching with Systemd Timers"
description: Discover how to automate theme switching between light and dark modes using a simple bash script and systemd timers.
giscus_comments: true

date: 2023-04-15
assets: assets/posts/2023-04-15-linux-theme-switch
img: assets/posts/2023-04-15-linux-theme-switch/screenshot.png

authors:
  - name: Steven Braun
    affiliations:
      name: TU Darmstadt
---

## Introduction
Alacritty, a fast and highly customizable terminal emulator, offers users the flexibility to switch between light and dark themes. However, manually changing the configuration file can be time-consuming, especially if you frequently switch themes throughout the day. In this blog post, we will demonstrate how to automate this process using a bash script and systemd timers. This way, the Alacritty theme will automatically change based on predefined times without any manual intervention.

## Motivation
Many developers and terminal users prefer to switch between light and dark themes depending on their environment, time of day, or personal preferences. Automating this process can save time and streamline the user experience. By leveraging a simple bash script and systemd timers, we can set specific times for theme changes, such as switching to the light theme at 8:00 am and the dark theme at 9:00 pm.

## Requirements
Before proceeding, ensure you have the following requirements:

1. Alacritty terminal emulator installed and configured.
2. A light and dark theme configured in your `alacritty.yml` file.

## The Script
We will use a bash script called `change_theme.sh` that changes the Alacritty theme based on the current time when no argument is provided. The script checks if the current time is between 8:00 am and 9:00 pm and sets the theme to light. Otherwise, it sets the theme to dark.

Here's the `change_theme.sh` script:

```bash
#!/bin/bash

# Define the config file path
CONFIG_FILE="$HOME/.config/alacritty/alacritty.yml"

# Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Config file not found at $CONFIG_FILE"
    exit 1
fi

# Function to set the theme
set_theme() {
    if [ "$1" == "light" ]; then
        sed -i 's/doom_one.yaml/papertheme.yaml/g' "$CONFIG_FILE"
    elif [ "$1" == "dark" ]; then
        sed -i 's/papertheme.yaml/doom_one.yaml/g' "$CONFIG_FILE"
    else
        echo "Invalid argument. Use 'light' or 'dark'."
        exit 1
    fi

    echo "Theme changed to $1."
}

# Check if an argument is provided
if [ "$#" -eq 1 ]; then
    set_theme "$1"
else
    # Get the current hour
    current_hour=$(date +%H)

    # Set the theme based on the current hour
    if [ "$current_hour" -ge 8 ] && [ "$current_hour" -lt 21 ]; then
        set_theme "light"
    else
        set_theme "dark"
    fi
fi
```

Save the script to a location accessible by the user, such as `~/.local/bin/`, and make it executable with `chmod +x change_theme.sh`.

## Creating a Systemd Timer
To create a systemd timer that runs the `change_theme.sh` script at 8:00 am and 9:00 pm, follow these steps:

1. Create a service file called `alacritty-auto-theme.service` with the following contents:

    ```ini
    [Unit]
    Description=Set Alacritty theme based on the time

    [Service]
    Type=oneshot
    Environment="DISPLAY=:0"
    ExecStart=%h/.local/bin/change_theme.sh
    ```

2. Move the service file to the systemd user directory:

    ```bash
    mv alacritty-auto-theme.service ~/.config/systemd/user/alacritty-auto-theme.service
    ```

3. Create a timer file called `alacritty-auto-theme.timer` with the following contents:

    ```ini
    [Unit]
    Description=Set Alacritty theme based on the time at 8:00 am and 9:00 pm

    [Timer]
    OnCalendar=*-*-* 08:00:00
    OnCalendar=*-*-* 21:00:00
    Persistent=true
    Unit=alacritty-auto-theme.service

    [Install]
    WantedBy=default.target
    ```

4. Move the timer file to the systemd user directory:

    ```bash
    mv alacritty-auto-theme.timer ~/.config/systemd/user/alacritty-auto-theme.timer
    ```

5. Reload the systemd user manager to recognize the new timer and service:

    ```bash
    systemctl --user daemon-reload
    ```

6. Enable and start the timer:

    ```bash
    systemctl --user enable --now alacritty-auto-theme.timer
    ```

Now, the Alacritty theme will automatically change based on the current time at 8:00 am and 9:00 pm every day.

## Conclusion
In this blog post, we have demonstrated how to automate Alacritty theme switching using a bash script and systemd timers. By creating a script that changes the theme based on the time of day and a systemd timer that runs the script at specified times, you can effortlessly switch between light and dark themes without manual intervention. This solution saves time and enhances the user experience by automatically adapting the Alacritty theme to your preferences or environmental conditions.
