import QtQuick
import QtQuick.Controls

ToolButton {
    id: ctrl

    background: Rectangle {
        id: i
        implicitWidth: 48
        implicitHeight: 48
        color: (ctrl.enabled == false) ? "transparent" : ctrl.hovered ? "#212121" : "transparent"
    }

    contentItem: Text {
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: __main__font__.name
        font.pixelSize: 16
        text: ctrl.text
        color: (ctrl.enabled == false) ? "#ccc" : "white"
    }

}
