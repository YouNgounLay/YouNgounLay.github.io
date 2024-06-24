MSG=$1
git commit -am "${MSG}"
git push origin main

#!/bin/bash
# Turn off the Wi-Fi interface on macOS

# Command to turn off Wi-Fi
networksetup -setairportpower airport off

# Notify the user that Wi-Fi has been turned off
echo "Wi-Fi has been turned off."
