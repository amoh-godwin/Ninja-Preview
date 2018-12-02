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
            text: "\uE710"

            onClicked: picker.open()

        }

        NavButton {
            text: "-"

            onClicked: mainWindow.showMinimized()

        }

        NavButton {
            anchors.bottom: parent.bottom
            text: "Quit"

            onClicked: mainWindow.close()

        }

    }

}
