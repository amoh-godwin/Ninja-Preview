#!/bin/bash

DESKTOP_FILE="$HOME/.local/share/applications/ninja-preview.desktop"
mkdir -p "$HOME/.local/share/applications"
cat << EOF > "$DESKTOP_FILE"
[Desktop Entry]
Type=Application
Name=Ninja-Preview
Comment=Preview your Qml files
Exec=ninja-preview %f
Icon=ninja-preview
Terminal=false
Categories=Development;
EOF
echo "Shortcut created at $DESKTOP_FILE"
