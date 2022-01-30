# Toggle smart switch on login/logout

# Install
- `cp listen_to_lock_or_unlock.sh toggle_lights.rb ~/bins/`
- Change user/pass & device_id in toggle_lights.rb
- `cp toggle-lights.service ~/.config/systemd/user/toggle-lights.service`
- `systemctl --user enable toggle-lights.service`
- `systemctl --user start toggle-lights.service`
