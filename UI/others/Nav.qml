import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

ToolBar {
    width: parent.width
    height: parent.height

    background: Rectangle {
        color: "#191b1f"
    }

    ColumnLayout {
        width: parent.width
        height: parent.height

        NavButton {
            anchors.top: parent.top
            text: "+"

            onClicked: picker.open()

        }

        NavButton {
            anchors.bottom: parent.bottom
            text: "Quit"
        }

    }

}
