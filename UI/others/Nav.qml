import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ToolBar {
    width: parent.width
    height: parent.height

    background: Rectangle {
        color: "#191b1f"
    }

    ColumnLayout {
        width: parent.width
        //height: parent.height
        spacing: 0

        NavButton {
            Layout.alignment: Layout.Top
            Layout.topMargin: 0
            text: "\uE710"

            onClicked: picker.open()

        }

        /*NavButton {
            Layout.alignment: Layout.Bottom
            text: "\uE738"

            onClicked: mainWindow.showMinimized()

        }

        NavButton {
            Layout.alignment: Layout.Bottom
            text: "Quit"

            onClicked: mainWindow.close()

        }*/

    }

}
