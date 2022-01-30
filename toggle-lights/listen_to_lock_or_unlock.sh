#!/bin/bash
dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | while read x; do
    case "$x" in
        *"boolean true"*) /home/rotsen/bins/toggle_lights.rb 'Off';; # Lock
        *"boolean false"*) /home/rotsen/bins/toggle_lights.rb 'On';; # Unlock
    esac
done
